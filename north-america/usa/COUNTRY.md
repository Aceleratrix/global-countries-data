---
name: "United States of America"
slug: usa
schema: countries-data/v1
version: 1.0.0
license: MIT
last_updated: 2026-04-30
authors:
  - name: "Marcos Torres"
    github: "mtorresbr"

# Basic Data
iso_code: "US"
iso_alpha3: "USA"
phone_prefix: "+1"
currency:
  code: "USD"
  symbol: "$"
  name: "United States Dollar"
language:
  primary: "en-US"
  secondary: ["es-US", "zh-US", "fr-US"]
population: 340110988
area_km2: 9372610

# Useful URLs
government_url: "https://www.usa.gov"
central_bank: "https://www.federalreserve.gov"
tax_authority: "https://www.irs.gov"
privacy_regulator: "https://www.ftc.gov"

# Completeness Status
completeness:
  fiscal: 85%
  telecom: 95%
  legal: 90%
  financial: 95%
  demographics: 100%
  business: 90%
---

# United States of America

The pilot country for AI First business operations in the US market.

## Overview
- **Currency:** US Dollar (USD) - $
- **Language:** English (en-US)
- **Population:** 340 million (2026)
- **GDP:** USD 28.7 trillion (2025)
- **Time Zones:** 6 zones (UTC-10 to UTC-4)
- **Tech Hub:** Silicon Valley, San Francisco Bay Area

## How to Use This Data

For AI multi-agent systems:
```python
import yaml

# Load US tax data
with open('usa/fiscal/tax-codes.yaml') as f:
    tax_data = yaml.safe_load(f)
    print(tax_data['federal_taxes'][0]['name'])  # "Federal Income Tax"

# Validate US phone format
import re
with open('usa/telecom/phone-formats.yaml') as f:
    phone = yaml.safe_load(f)
    pattern = phone['phone']['formats']['standard']['pattern']
    print(bool(re.match(pattern, "+14155552671")))  # True
```

## Data Structure

### [Fiscal/](fiscal/)
Federal and state tax codes (IRS), sales tax, corporate tax, 1099 forms.

### [Financial/](financial/)
Major banks (JPMorgan Chase, Bank of America, Wells Fargo), payment methods (ACH, Credit Cards, PayPal, Stripe, Square).

### [Telecom/](telecom/)
Phone formats (+1-AAA-EEE-XXXX), ZIP codes, address standards, area codes.

### [Demographics/](demographics/)
Population by state, age groups, languages, time zones, income levels.

### [Business/](business/)
Company sizes (Sole Proprietorship, C-Corp, S-Corp, LLC), NAICS codes, business hours, holidays.

### [Legal/](legal/)
**Internet Legal Framework:** Section 230, DMCA, state privacy laws (CCPA/CPRA, etc.).
**Privacy Laws:** Sectoral model (no federal GDPR equivalent), HIPAA, GLBA, COPPA, FTC enforcement.
**Business Law:** Uniform Commercial Code (UCC), employment at-will, incorporation.

### [Tech/](tech/)
**Cloud Regions:** AWS (us-west-1/2, us-east-1/2), Google Cloud, Azure, Oracle.
**AI Services:** OpenAI API, Anthropic API, Google Vertex AI, AWS Bedrock.
**Tech Ecosystem:** Silicon Valley, Silicon Alley (NYC), Austin, Seattle, Boston.

### [Marketing/](marketing/)
Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, email marketing, affiliate marketing.

---

## Highlights for AI First Businesses

1. **No Federal Privacy Law (Yet):** Sectoral approach (HIPAA, GLBA, COPPA) + state laws (CCPA/CPRA, Virginia CDPA, etc.)
2. **Section 230 Protection:** Platforms not liable for user-generated content (key for AI platforms)
3. **ACH Network:** US equivalent to PIX, but slower (1-2 business days)
4. **Sales Tax Complexity:** 10,000+ jurisdictions with different rates
5. **Delaware Incorporation:** 66% of Fortune 500 incorporated in DE (business-friendly)
6. **At-Will Employment:** Either party can terminate employment anytime (no cause needed)
7. **Silicon Valley Ecosystem:** $2.1 trillion tech market cap, 50+ unicorns
8. **Cloud Regions:** 20+ regions across AWS, GCP, Azure (low latency nationwide)

---

## Completeness Status

| Category | Progress |
|-----------|-----------|
| Fiscal | ████████░░ 85% |
| Telecom | ██████████ 95% |
| Legal | █████████░ 90% |
| Financial | ██████████ 95% |
| Demographics | ██████████ 100% |
| Business | ████████░░ 90% |

---

**Maintained by:** [Marcos Torres](https://github.com/mtorresbr) and [Open Source Community](https://github.com/mtorresbr/global-countries-data)
**Last Updated:** April 30, 2026
**Schema:** countries-data/v1
**License:** MIT
**Primary Language:** English (en-US)
**Secondary Languages:** Spanish (es-US), Chinese (zh-US), French (fr-US)
