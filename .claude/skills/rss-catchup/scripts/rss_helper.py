#!/usr/bin/env python3
"""
RSS helper script for fetching feed info and article content.
Used by the rss-catchup skill.
"""

import json
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime
from html.parser import HTMLParser

try:
    import feedparser
    HAS_FEEDPARSER = True
except ImportError:
    HAS_FEEDPARSER = False


class HTMLTextExtractor(HTMLParser):
    """Extract plain text from HTML content."""

    def __init__(self):
        super().__init__()
        self.text = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside'}
        self.current_skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.current_skip += 1

    def handle_endtag(self, tag):
        if tag in self.skip_tags and self.current_skip > 0:
            self.current_skip -= 1

    def handle_data(self, data):
        if self.current_skip == 0:
            text = data.strip()
            if text:
                self.text.append(text)

    def get_text(self):
        return ' '.join(self.text)


def html_to_text(html: str) -> str:
    """Convert HTML to plain text."""
    parser = HTMLTextExtractor()
    try:
        parser.feed(html)
        return parser.get_text()
    except:
        # Fallback: strip tags with regex
        text = re.sub(r'<[^>]+>', ' ', html)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()


def parse_date(entry) -> str:
    """Extract publication date from feed entry."""
    # Try different date fields
    for field in ['published_parsed', 'updated_parsed', 'created_parsed']:
        if hasattr(entry, field) and getattr(entry, field):
            try:
                dt = datetime(*getattr(entry, field)[:6])
                return dt.strftime('%Y-%m-%d')
            except:
                pass

    # Try string date fields
    for field in ['published', 'updated', 'created']:
        if hasattr(entry, field) and getattr(entry, field):
            date_str = getattr(entry, field)
            # Try to extract YYYY-MM-DD
            match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_str)
            if match:
                return match.group(0)

    return None


def get_entry_content(entry) -> str:
    """Extract content from feed entry."""
    # Try content field (often has full HTML)
    if hasattr(entry, 'content') and entry.content:
        for content in entry.content:
            if content.get('value'):
                return html_to_text(content['value'])

    # Try content:encoded (common in WordPress feeds)
    if hasattr(entry, 'content_encoded') and entry.content_encoded:
        return html_to_text(entry.content_encoded)

    # Fall back to summary/description
    if hasattr(entry, 'summary') and entry.summary:
        return html_to_text(entry.summary)

    if hasattr(entry, 'description') and entry.description:
        return html_to_text(entry.description)

    return None


def get_feed_articles(url: str, limit: int = 20, since_date: str = None) -> list:
    """Get recent articles from an RSS feed."""
    if not HAS_FEEDPARSER:
        return {"error": "feedparser not installed. Run: pip install feedparser"}

    try:
        feed = feedparser.parse(url)
    except Exception as e:
        return {"error": f"Failed to parse feed: {e}"}

    if feed.bozo and not feed.entries:
        return {"error": f"Feed error: {feed.bozo_exception}"}

    articles = []
    for entry in feed.entries[:limit]:
        article = {
            'title': entry.get('title', 'Untitled'),
            'url': entry.get('link', ''),
            'author': entry.get('author', entry.get('dc_creator', '')),
            'published': parse_date(entry),
            'summary': get_entry_content(entry),
            'guid': entry.get('id', entry.get('link', ''))
        }

        # Filter by date if specified
        if since_date and article['published']:
            if article['published'] < since_date:
                continue

        articles.append(article)

    return articles


def fetch_article_content(url: str) -> dict:
    """Fetch full article content from URL."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; RSS Reader)'
    }

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            html = response.read().decode('utf-8', errors='ignore')
    except urllib.error.URLError as e:
        return {"error": f"Failed to fetch URL: {e}"}
    except Exception as e:
        return {"error": f"Error: {e}"}

    # Extract main content - look for article tags
    article_patterns = [
        r'<article[^>]*>(.*?)</article>',
        r'<main[^>]*>(.*?)</main>',
        r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>',
        r'<div[^>]*class="[^"]*post[^"]*"[^>]*>(.*?)</div>',
    ]

    content = None
    for pattern in article_patterns:
        match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
        if match:
            content = html_to_text(match.group(1))
            if len(content) > 200:  # Only use if substantial
                break

    # Fallback to body
    if not content or len(content) < 200:
        body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
        if body_match:
            content = html_to_text(body_match.group(1))

    if not content:
        content = html_to_text(html)

    # Extract title
    title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE)
    title = html_to_text(title_match.group(1)) if title_match else ''

    return {
        'url': url,
        'title': title,
        'content': content[:50000] if content else None,  # Limit size
        'content_length': len(content) if content else 0
    }


def main():
    """CLI interface."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  rss_helper.py feed URL [limit] [since_date]")
        print("  rss_helper.py article URL")
        print("")
        print("Examples:")
        print("  rss_helper.py feed 'https://example.com/feed' 10")
        print("  rss_helper.py feed 'https://example.com/feed' 20 2025-01-01")
        print("  rss_helper.py article 'https://example.com/post/123'")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'feed':
        if len(sys.argv) < 3:
            print("Error: URL required", file=sys.stderr)
            sys.exit(1)
        url = sys.argv[2]
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 20
        since = sys.argv[4] if len(sys.argv) > 4 else None
        articles = get_feed_articles(url, limit, since)
        print(json.dumps(articles, indent=2))

    elif command == 'article':
        if len(sys.argv) < 3:
            print("Error: URL required", file=sys.stderr)
            sys.exit(1)
        url = sys.argv[2]
        result = fetch_article_content(url)
        print(json.dumps(result, indent=2))

    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
