#!/usr/bin/env python3
"""
Wattpad AI Prompt Search Workflow
Usage: python search_wattpad_ai_prompt.py <story_url_or_id>
"""

import re
import sys
import urllib.request
import urllib.error

def search_page_for_prompt(url):
    """Fetch page and search for AI prompt patterns."""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        patterns = [
            r'AI prompt',
            r'generated using',
            r'Write with AI',
            r'generation settings',
            r'<script[^>]*type="application/json"[^>]*>(.*?)</script>',
            r'prompt[:\s]+([^\n]+)',
        ]
        
        found = []
        for pat in patterns:
            matches = re.findall(pat, html, re.IGNORECASE | re.DOTALL)
            if matches:
                for m in matches:
                    found.append((pat, m[:500]))
        
        return found, html
    except Exception as e:
        return None, str(e)

def extract_story_id(url):
    """Extract story ID from various Wattpad URL formats."""
    m = re.search(r'/story/(\d+)', url)
    if m:
        return m.group(1)
    m = re.search(r'/myworks/(\d+)', url)
    if m:
        return m.group(1)
    return url

if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://www.wattpad.com/story/413344255'
    story_id = extract_story_id(url)
    
    print(f'Searching: {url}')
    print(f'Story ID: {story_id}')
    print()
    
    found, data = search_page_for_prompt(url)
    
    if found is None:
        print(f'ERROR: {data}')
        sys.exit(1)
    
    if found:
        print(f'Found {len(found)} matches:')
        for pat, match in found:
            print(f'\nPattern: {pat}')
            print(f'Match: {match[:300]}')
    else:
        print('No AI prompt found on this page.')
        print('Try checking:')
        print('  1. Story Summary/Description section')
        print('  2. Author\'s notes at end of chapters')
        print('  3. Wattpad Originals section (if applicable)')
        print('  4. Page source for hidden metadata')
