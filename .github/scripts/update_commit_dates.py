#!/usr/bin/env python3
"""
Script to update last commit dates for GitHub repositories in README.md
"""
import re
import requests
from datetime import datetime
import sys

def get_last_commit_date(repo_url):
    """Get the last commit date from GitHub API"""
    # Extract owner/repo from GitHub URL
    match = re.search(r'github\.com/([^/]+)/([^/\)]+)', repo_url)
    if not match:
        return None

    owner, repo = match.groups()

    # Call GitHub API
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('pushed_at')
        elif response.status_code == 404:
            return "404"
        return None
    except Exception as e:
        print(f"Error fetching {owner}/{repo}: {e}", file=sys.stderr)
        return None

def format_time_diff(date_str, today):
    """Format the time difference in a human-readable way"""
    if not date_str or date_str == "404":
        return None

    commit_date = datetime.fromisoformat(date_str.replace('Z', '+00:00')).replace(tzinfo=None)
    diff = today - commit_date
    days = diff.days

    if days < 30:
        time_str = f"{days}d"
    elif days < 365:
        months = days // 30
        time_str = f"{months}mo"
    else:
        years = days // 365
        months = (days % 365) // 30
        if months > 0:
            time_str = f"{years}yr {months}mo"
        else:
            time_str = f"{years}yr"

    # Add warning flag for repos > 1 year old
    warning = "⚠️ " if days > 365 else ""
    return f"({warning}{time_str})"

def update_readme(readme_path):
    """Update README.md with latest commit dates"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all GitHub links with or without existing timestamps
    # Pattern matches: [name](url) or [name](url) (timestamp)
    pattern = r'\[([^\]]+)\]\((https://github\.com/[^)]+)\)(?:\s*\([^)]*\))?'

    today = datetime.utcnow()
    updated_content = content
    changes_made = False

    matches = list(re.finditer(pattern, content))
    print(f"Found {len(matches)} GitHub links to check")

    # Process in reverse to avoid offset issues
    for match in reversed(matches):
        name = match.group(1)
        url = match.group(2)

        print(f"Checking {name}...")

        # Get last commit date
        last_commit = get_last_commit_date(url)
        if last_commit == "404":
            print(f"  Repository not found (404)")
            continue
        elif not last_commit:
            print(f"  Could not fetch commit date")
            continue

        # Format the time difference
        time_str = format_time_diff(last_commit, today)
        if not time_str:
            continue

        print(f"  Last commit: {time_str}")

        # Create the replacement string
        new_text = f"[{name}]({url}) {time_str}"

        # Replace the old text (with or without existing timestamp)
        start = match.start()
        end = match.end()
        old_text = updated_content[start:end]

        # Check if there's already a timestamp
        timestamp_match = re.search(r'\s*\([^)]*\)$', old_text)
        if timestamp_match:
            # Update existing timestamp
            old_text_without_timestamp = old_text[:timestamp_match.start()]
            if old_text_without_timestamp + " " + time_str != old_text:
                updated_content = updated_content[:start] + new_text + updated_content[end:]
                changes_made = True
                print(f"  Updated timestamp")
        else:
            # Add new timestamp
            updated_content = updated_content[:start] + new_text + updated_content[end:]
            changes_made = True
            print(f"  Added timestamp")

    if changes_made:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("\nREADME.md updated successfully!")
        return True
    else:
        print("\nNo changes needed.")
        return False

if __name__ == "__main__":
    readme_path = "README.md"
    if len(sys.argv) > 1:
        readme_path = sys.argv[1]

    try:
        changes = update_readme(readme_path)
        sys.exit(0 if changes else 1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)
