#!/usr/bin/env python3
"""
Global Countries Data - Automated Country Processor
Continuously processes countries from largest to smallest economy.

Usage:
    python3 process-next-country.py
    
This script:
1. Reads the prioritized country list
2. Finds the next pending country (highest priority, not done)
3. Creates the country directory structure
4. (Placeholder) Would trigger AI agent to fill YAML files
5. Commits and pushes progress
6. Exits (cron job will trigger next run)
"""

import os
import re
import subprocess
from datetime import datetime

# Base path
BASE_PATH = "/Users/marcostorres/Documents/projetos/global-countries-data"
COUNTRIES_LIST = os.path.join(BASE_PATH, "docs/COUNTRIES-LIST.md")
COMPLETED_COUNTRIES = ['brazil', 'usa', 'japan']  # Already done
IN_PROGRESS = ['germany']  # Partially done

def get_next_country():
    """Read COUNTRIES-LIST.md and find next pending country."""
    print("Reading countries list...")
    
    with open(COUNTRIES_LIST, 'r') as f:
        content = f.read()
    
    # Find Tier 1 countries (top 20)
    # Pattern: | N | 🇽🇽 **Country** | $X.XXT | PRIORITY | STATUS |
    pattern = r'\|\s*(\d+)\s*\|\s*([^\|]+)\s*\|\s*\$([0-9.T]+)\s*\|\s*(\w+)\s*\|\s*([^\n]+)\|'
    
    matches = re.findall(pattern, content)
    
    print(f"Found {len(matches)} countries in list")
    
    for rank, country_name, gdp, priority, status in matches:
        # Extract country slug (lowercase, no spaces, no flags)
        # Example: 🇺🇸 **USA** -> usa
        slug_match = re.search(r'\*\*(.+?)\*\*', country_name)
        if slug_match:
            country = slug_match.group(1).strip().lower()
        else:
            continue
        
        # Skip completed
        if country in COMPLETED_COUNTRIES:
            print(f"  SKIP (completed): {country}")
            continue
            
        # Skip in-progress (unless forced)
        if country in IN_PROGRESS:
            print(f"  SKIP (in progress): {country}")
            continue
            
        # Check priority
        if priority.strip() in ['HIGH', 'MEDIUM']:
            print(f"\n🎯 NEXT COUNTRY: {country} (Rank #{rank}, GDP: {gdp})")
            return country, rank, gdp
    
    print("\n✅ ALL TIER 1 COUNTRIES DONE! Check Tier 2...")
    return None, None, None

def create_country_structure(country_slug):
    """Create directory structure for new country."""
    country_path = os.path.join(BASE_PATH, country_slug)
    
    if os.path.exists(country_path):
        print(f"  Directory already exists: {country_path}")
        return False
    
    print(f"Creating structure for: {country_slug}")
    
    # Create directories
    dirs = [
        '',  # country root
        'fiscal',
        'financial',
        'telecom',
        'demographics',
        'business',
        'business/software',
        'legal',
        'tech',
        'marketing'
    ]
    
    for d in dirs:
        full_path = os.path.join(country_path, d)
        os.makedirs(full_path, exist_ok=True)
    
    print(f"  ✓ Created directory structure")
    return True

def copy_templates(country_slug):
    """Copy templates to new country directory."""
    templates_path = os.path.join(BASE_PATH, 'templates')
    country_path = os.path.join(BASE_PATH, country_slug)
    
    # Copy COUNTRY.md.template
    src = os.path.join(templates_path, 'COUNTRY.md.template')
    dst = os.path.join(country_path, 'COUNTRY.md')
    
    if os.path.exists(src):
        with open(src, 'r') as f:
            content = f.read()
        with open(dst, 'w') as f:
            f.write(content)
        print(f"  ✓ Copied COUNTRY.md template")
    
    return True

def commit_progress(country_slug, status="IN PROGRESS"):
    """Commit and push progress to GitHub."""
    os.chdir(BASE_PATH)
    
    # Git add
    cmd = f"git add {country_slug}/"
    subprocess.run(cmd, shell=True, capture_output=True)
    
    # Git commit
    date_str = datetime.now().strftime("%Y-%m-%d")
    commit_msg = f"{country_slug.upper()} {status} (automated - directory structure created)"
    cmd = f'git commit -m "{commit_msg}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"  ✓ Committed: {commit_msg}")
        
        # Push to GitHub
        cmd = "git push origin main"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"  ✓ Pushed to GitHub!")
            return True
        else:
            print(f"  ✗ Push failed: {result.stderr}")
            return False
    else:
        print(f"  ✗ Commit failed: {result.stderr}")
        return False

def main():
    print("=" * 60)
    print("🌍 Global Countries Data - Automated Processor")
    print("=" * 60)
    print()
    
    # Get next country
    country, rank, gdp = get_next_country()
    
    if not country:
        print("\n✅ ALL HIGH/MEDIUM PRIORITY COUNTRIES PROCESSED!")
        print("Check COUNTRIES-LIST.md for remaining LOW priority countries.")
        return
    
    print(f"\n📍 Processing: {country} (Rank #{rank}, GDP: {gdp})")
    print("-" * 60)
    
    # Create structure
    created = create_country_structure(country)
    
    # Copy templates
    copy_templates(country)
    
    # Commit
    if created:
        commit_progress(country, "IN PROGRESS (structure only)")
        print(f"\n✅ Structure created for {country}!")
        print(f"   Next: Fill YAML files manually or via AI agent")
        print(f"   See: {os.path.join(BASE_PATH, country)}/")
    else:
        print(f"\n⚠️  Structure already exists for {country}")
    
    print("\n" + "=" * 60)
    print("Done! Cron job will trigger next country on next run.")
    print("=" * 60)

if __name__ == "__main__":
    main()
