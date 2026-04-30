#!/usr/bin/env python3
"""
Add disclaimer field to all YAML files in the repository.
This ensures legal protection across all country data files.
"""

import os
import re

def add_disclaimer_to_yaml(file_path):
    """Add disclaimer field after last_updated in YAML files."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if disclaimer already exists
        if 'disclaimer:' in content:
            print(f"  SKIP (already has disclaimer): {file_path}")
            return False
        
        # Pattern to find 'last_updated:' line and add disclaimer after it
        # This handles the common pattern in our YAML files
        pattern = r'(last_updated:\s*\d{4}-\d{2}-\d{2}\s*\n)'
        
        def replace_func(match):
            return match.group(1) + 'disclaimer: "Data provided AS IS. Verify with official sources before use. See DISCLAIMER.md for full terms."\n'
        
        new_content = re.sub(pattern, replace_func, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ADDED disclaimer: {file_path}")
            return True
        else:
            print(f"  NO MATCH (no last_updated?): {file_path}")
            return False
            
    except Exception as e:
        print(f"  ERROR {file_path}: {e}")
        return False

def main():
    base_path = "/Users/marcostorres/Documents/projetos/global-countries-data"
    
    print("Adding disclaimer to all YAML files...")
    print("=" * 60)
    
    modified = 0
    skipped = 0
    errors = 0
    
    # Walk through all country directories
    for country in ['brazil', 'usa', 'japan', 'germany']:
        country_path = os.path.join(base_path, country)
        if not os.path.exists(country_path):
            continue
            
        print(f"\nProcessing {country}/...")
        for root, dirs, files in os.walk(country_path):
            for file in files:
                if file.endswith('.yaml'):
                    file_path = os.path.join(root, file)
                    if add_disclaimer_to_yaml(file_path):
                        modified += 1
                    else:
                        skipped += 1
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: Modified={modified}, Skipped={skipped}, Errors tracked above")
    print("Done!")

if __name__ == "__main__":
    main()
