# Contributing to Global Countries Data 🌍

Thank you for your interest in contributing to the world's most comprehensive open dataset for AI agents! This repository provides structured YAML data about countries for multi-agent systems, AI applications, and LLM-powered tools.

## 🎯 How to Contribute

### 1. Add a New Country
Want to add a country that's not yet in the repository? Great! Follow these steps:

#### Step 1: Check if the country already exists
```bash
# List all countries
find . -name "COUNTRY.md" | sort
```

#### Step 2: Create the directory structure
```bash
# Replace COUNTRY_CODE with the ISO 3166-1 alpha-2 code (e.g., us, br, jp)
# Replace CONTINENT with: africa, asia, europe, north-america, south-america, oceania
mkdir -p CONTINENT/COUNTRY_CODE/{legal,fiscal,financial,telecom,demographics,business/software,tech,marketing}
```

#### Step 3: Create the 13 required files
Each country **must** have these 13 files:

1. **COUNTRY.md** - Country overview (see template below)
2. **README.md** - AI-ready summary with data file links
3. **legal/internet-law.yaml** - Internet laws, data protection, AI regulations
4. **legal/labor-law.yaml** - Employment laws, contracts, working conditions
5. **fiscal/tax-codes.yaml** - VAT, corporate tax, tax IDs, fiscal year
6. **financial/banks.yaml** - Banking system, payment methods, fintech
7. **telecom/phone-formats.yaml** - Phone formats, mobile operators, ISPs
8. **demographics/population.yaml** - Population, languages, demographics
9. **tech/ai-cloud-services.yaml** - AI strategy, cloud providers, tech ecosystem
10. **business/company-sizes.yaml** - SME definitions, business counts by sector
11. **business/real-estate.yaml** - Property market, rental prices, legal framework
12. **business/import-export.yaml** - Trade agreements, export/import data
13. **marketing/digital-marketing.yaml** - Digital ad spend, social media, platforms

#### Step 4: Follow the YAML schema
All YAML files must:
- Include `country:` field with ISO 3166-1 alpha-2 code
- Include `last_updated:` field in YYYY-MM-DD format
- Use consistent indentation (2 spaces)
- Include comments explaining fields
- Use `[]` for empty arrays, not `null`

**Example YAML header:**
```yaml
# Country Name Legal Framework
# AI-Ready: Structured for multi-agent systems

country: us
last_updated: "2024-12-15"
jurisdiction: US
```

#### Step 5: Validate your files
```bash
# Run validation (requires Python 3.8+)
python scripts/validate_country.py --country CONTINENT/COUNTRY_CODE

# Or use the online validator (coming soon)
```

#### Step 6: Submit a Pull Request
1. Fork the repository
2. Create a branch: `git checkout -b add/COUNTRY_CODE`
3. Commit your changes: `git commit -m "Add COUNTRY_NAME (13 files) 🇨🇴"`
4. Push: `git push origin add/COUNTRY_CODE`
5. Open a Pull Request with the template below

---

### 2. Improve Existing Country Data
Found outdated or incorrect information? Help us keep the data accurate!

- **Fix errors:** Submit a PR with corrections and cite your sources
- **Add new fields:** Extend existing YAML files with new data points
- **Update statistics:** Keep population, GDP, and other metrics current
- **Fix YAML syntax:** Correct formatting issues

---

### 3. Improve Documentation & Tooling
Help make this repository more useful for the community:

- **Update README.md:** Improve examples, add use cases
- **Enhance validation scripts:** Add new checks in `scripts/`
- **Create new schemas:** Propose new YAML structures for additional data
- **Improve docs:** Fix typos, clarify instructions

---

## 📋 Pull Request Template

When submitting a PR, please use this template:

```markdown
## 🌍 Country Added/Updated

- **Country:** [Country Name]
- **ISO Code:** [XX]
- **Continent:** [Africa/Asia/Europe/North America/South America/Oceania]
- **Files Added:** [X/13]

## ✅ Checklist

- [ ] All 13 required files created
- [ ] YAML files pass validation (`python scripts/validate_country.py`)
- [ ] No sensitive/credential data included
- [ ] Sources cited (official government/central bank websites preferred)
- [ ] Data is recent (within last 12 months)
- [ ] YAML syntax is correct (no tabs, 2-space indentation)

## 📊 Data Sources

- [List your sources here, preferably official government websites]

## 🤖 AI/LLM Context

[Brief description of how this data can be used by AI agents]
```

---

## 🏗️ File Templates

### COUNTRY.md Template
```markdown
# 🇨🇴 Country Name

**Capital:** [Capital City]  
**Population:** [Number] ([Year])  
**Currency:** [Currency Name] ([Code], [Symbol])  
**Official Language:** [Language(s)]  
**Government:** [Government Type]  
**GDP (Nominal):** $[Amount] ([Year]) – [Rank] globally  
**GDP Per Capita:** $[Amount]  
**HDI:** [Score] ([Level]) – [Rank] globally  
**Time Zones:** [Time Zone(s)]  

## 🌐 Quick Facts

- **ISO 3166-1:** [XX] (Alpha-2), [XXX] (Alpha-3), [NNN] (Numeric)
- **Internet TLD:** .[tld]
- **Calling Code:** +[code]
- **[Regional Bloc]:** [Yes/No]

## 🏢 Business Environment

[Brief description of key industries and business climate]

**Key Industries:**
- [Industry 1]
- [Industry 2]

## 🤖 AI Readiness

[Description of AI strategy, regulations, and ecosystem]

## 📊 Economic Highlights

- **Unemployment Rate:** [X]%
- **Inflation Rate:** [X]%
- **Corporate Tax Rate:** [X]%
- **Minimum Wage:** [Amount] ([Year])

## 🔗 Useful Links

- [Government Portal](https://...)
- [Tax Authority](https://...)
- [Central Bank](https://...)
```

---

## 🏷️ Branch Naming Convention

- **Add new country:** `add/COUNTRY_CODE` (e.g., `add/co` for Colombia)
- **Update country:** `update/COUNTRY_CODE` (e.g., `update/us` for USA)
- **Fix bug:** `fix/description` (e.g., `fix/spain-vat-rate`)
- **Docs:** `docs/description` (e.g., `docs/improve-contributing`)

---

## 🧪 Testing & Validation

Before submitting your PR, run:

```bash
# Validate all YAML files
python scripts/validate_yaml.py

# Validate a specific country
python scripts/validate_country.py --country europe/spain

# Check for sensitive data
python scripts/check_sensitive.py
```

All PRs are automatically validated via GitHub Actions.

---

## 💡 Tips for Quality Contributions

1. **Use official sources:** Government websites, central banks, UN data
2. **Keep it current:** Data should be within the last 12 months
3. **Be comprehensive:** Fill all fields; use `null` only when data is truly unavailable
4. **Think AI-first:** Include context that helps LLMs understand the data
5. **No credentials:** Never include API keys, passwords, or tokens
6. **Cite sources:** Add comments like `# Source: https://...` in YAML files

---

## 🏆 Recognition

All contributors are added to our [Contributors List](README.md#contributors) in the README!

---

## 📞 Questions?

- **Open an issue:** Use the "Question" template
- **Join discussions:** [Link to discussions, if available]
- **Email maintainers:** [Contact info, if desired]

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

**Thank you for helping build the world's best open dataset for AI agents! 🚀**
