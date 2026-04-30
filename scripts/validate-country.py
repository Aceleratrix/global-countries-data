#!/usr/bin/env python3
"""
Validate country data against JSON schemas.
Usage: python validate-country.py --country brazil
"""

import os
import sys
import yaml
import json
import argparse
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Please install jsonschema: pip install jsonschema")
    sys.exit(1)

SCHEMA_DIR = Path(__file__).parent.parent / "schemas"
COUNTRIES_DIR = Path(__file__).parent.parent

def load_schema(schema_name):
    """Load a JSON schema file."""
    schema_path = SCHEMA_DIR / f"{schema_name}.json"
    if not schema_path.exists():
        return None
    with open(schema_path) as f:
        return json.load(f)

def validate_yaml_file(yaml_path, schema_name):
    """Validate a YAML file against a schema."""
    schema = load_schema(schema_name)
    if schema is None:
        print(f"⚠️  Schema {schema_name}.json not found, skipping validation")
        return True
    
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
    
    try:
        jsonschema.validate(data, schema)
        print(f"✅ {yaml_path.name} validates against {schema_name}")
        return True
    except jsonschema.ValidationError as e:
        print(f"❌ {yaml_path.name} validation error: {e.message}")
        return False

def validate_country(country_slug):
    """Validate all data for a country."""
    country_dir = COUNTRIES_DIR / country_slug
    
    if not country_dir.exists():
        print(f"❌ Country directory not found: {country_slug}")
        return False
    
    print(f"\n🔍 Validating {country_slug}...\n")
    
    success = True
    
    # Validate COUNTRY.md (extract YAML frontmatter)
    country_md = country_dir / "COUNTRY.md"
    if country_md.exists():
        with open(country_md) as f:
            content = f.read()
            if content.startswith('---'):
                _, fm, _ = content.split('---', 2)
                data = yaml.safe_load(fm)
                schema = load_schema("country-metadata")
                if schema:
                    try:
                        jsonschema.validate(data, schema)
                        print(f"✅ COUNTRY.md frontmatter validates")
                    except jsonschema.ValidationError as e:
                        print(f"❌ COUNTRY.md validation error: {e.message}")
                        success = False
            else:
                print("⚠️  COUNTRY.md has no YAML frontmatter")
    
    # Validate YAML files in subdirectories
    yaml_files = [
        ("fiscal/tax-codes.yaml", "fiscal"),
        ("telecom/phone-formats.yaml", "telecom"),
        ("financial/banks.yaml", "financial"),
    ]
    
    for file_path, schema_name in yaml_files:
        full_path = country_dir / file_path
        if full_path.exists():
            if not validate_yaml_file(full_path, schema_name):
                success = False
        else:
            print(f"⚠️  {file_path} not found (optional)")
    
    return success

def main():
    parser = argparse.ArgumentParser(description="Validate country data")
    parser.add_argument("--country", help="Country slug to validate")
    parser.add_argument("--all", action="store_true", help="Validate all countries")
    
    args = parser.parse_args()
    
    if args.all:
        countries = [d.name for d in COUNTRIES_DIR.iterdir() 
                     if d.is_dir() and not d.name.startswith('.')]
        results = []
        for country in countries:
            results.append(validate_country(country))
        success = all(results)
    elif args.country:
        success = validate_country(args.country)
    else:
        parser.print_help()
        sys.exit(1)
    
    if success:
        print("\n✅ All validations passed!")
    else:
        print("\n❌ Some validations failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
