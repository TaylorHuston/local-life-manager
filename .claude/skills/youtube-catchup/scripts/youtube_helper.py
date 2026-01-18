#!/usr/bin/env python3
"""
YouTube helper script for fetching video info and transcripts.
Used by the youtube-catchup skill.
"""

import subprocess
import json
import re
import sys
import os
from datetime import datetime
from pathlib import Path


def parse_vtt(vtt_content: str) -> str:
    """Parse VTT subtitle content and extract clean text."""
    lines = vtt_content.split('\n')
    text_lines = []
    seen = set()

    for line in lines:
        # Skip metadata and timestamp lines
        if (line.startswith('WEBVTT') or
            line.startswith('Kind:') or
            line.startswith('Language:') or
            '-->' in line or
            line.strip() == '' or
            re.match(r'^\d{2}:\d{2}:\d{2}', line)):
            continue

        # Remove HTML-like tags (VTT formatting)
        clean = re.sub(r'<[^>]+>', '', line).strip()

        # Skip empty and duplicate lines
        if clean and clean not in seen:
            seen.add(clean)
            text_lines.append(clean)

    return ' '.join(text_lines)


def get_channel_videos(handle: str, limit: int = 20, since_date: str = None) -> list:
    """Get recent videos from a YouTube channel.

    Note: since_date is ignored because flat-playlist mode doesn't return
    upload_date. Use processed_videos list in state.json to filter instead.
    """
    url = f"https://www.youtube.com/{handle}/videos"

    cmd = [
        'yt-dlp', '--flat-playlist',
        '--playlist-end', str(limit),
        '--dump-json',
        url
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        return {"error": result.stderr}

    videos = []
    for line in result.stdout.strip().split('\n'):
        if not line:
            continue
        try:
            data = json.loads(line)
            video = {
                'id': data.get('id'),
                'title': data.get('title'),
                'upload_date': data.get('upload_date')  # Will be null in flat-playlist mode
            }
            videos.append(video)
        except json.JSONDecodeError:
            continue

    return videos


def get_video_metadata(video_id: str) -> dict:
    """Get metadata for a single video."""
    url = f"https://www.youtube.com/watch?v={video_id}"

    cmd = [
        'yt-dlp',
        '--dump-json',
        '--skip-download',
        '--js-runtimes', 'node',
        url
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        return {"error": result.stderr}

    try:
        data = json.loads(result.stdout)

        upload_date = data.get('upload_date', '')
        if upload_date and len(upload_date) == 8:
            upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"

        return {
            'title': data.get('title', ''),
            'channel': data.get('channel', data.get('uploader', '')),
            'upload_date': upload_date,
            'duration_seconds': data.get('duration', 0) or 0,
            'url': data.get('webpage_url', url),
            'description': data.get('description', '')
        }
    except json.JSONDecodeError as e:
        return {"error": f"JSON parse error: {e}"}


def get_transcript(video_id: str, temp_dir: str = '/tmp') -> str:
    """Fetch and parse transcript for a video."""
    url = f"https://www.youtube.com/watch?v={video_id}"
    output_path = os.path.join(temp_dir, f"yt_{video_id}")
    vtt_path = f"{output_path}.en.vtt"

    # Clean up any existing file
    if os.path.exists(vtt_path):
        os.remove(vtt_path)

    cmd = [
        'yt-dlp',
        '--write-auto-sub', '--sub-lang', 'en',
        '--skip-download',
        '--js-runtimes', 'node',
        '--output', output_path,
        url
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if not os.path.exists(vtt_path):
        # Try without auto-sub (manual captions)
        cmd = [
            'yt-dlp',
            '--write-sub', '--sub-lang', 'en',
            '--skip-download',
            '--js-runtimes', 'node',
            '--output', output_path,
            url
        ]
        subprocess.run(cmd, capture_output=True, text=True)

    if os.path.exists(vtt_path):
        with open(vtt_path, 'r', encoding='utf-8') as f:
            vtt_content = f.read()
        os.remove(vtt_path)
        return parse_vtt(vtt_content)

    return None


def format_duration(seconds: int) -> str:
    """Format seconds as human readable duration."""
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        return f"{seconds // 60}m {seconds % 60}s"
    else:
        hours = seconds // 3600
        mins = (seconds % 3600) // 60
        return f"{hours}h {mins}m"


def main():
    """CLI interface."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  youtube_helper.py channel @handle [limit]")
        print("  youtube_helper.py video VIDEO_ID")
        print("  youtube_helper.py transcript VIDEO_ID")
        print("  youtube_helper.py full VIDEO_ID  # metadata + transcript")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'channel':
        handle = sys.argv[2]
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 20
        # Note: since_date param is kept for backwards compatibility but ignored
        # because flat-playlist mode doesn't return upload dates
        videos = get_channel_videos(handle, limit)
        print(json.dumps(videos, indent=2))

    elif command == 'video':
        video_id = sys.argv[2]
        metadata = get_video_metadata(video_id)
        print(json.dumps(metadata, indent=2))

    elif command == 'transcript':
        video_id = sys.argv[2]
        transcript = get_transcript(video_id)
        if transcript:
            print(transcript)
        else:
            print("NO_TRANSCRIPT_AVAILABLE", file=sys.stderr)
            sys.exit(1)

    elif command == 'full':
        video_id = sys.argv[2]
        metadata = get_video_metadata(video_id)
        transcript = get_transcript(video_id)

        result = {
            'metadata': metadata,
            'transcript': transcript,
            'has_transcript': transcript is not None
        }
        print(json.dumps(result, indent=2))

    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
