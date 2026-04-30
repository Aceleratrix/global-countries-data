# United Kingdom 🇬🇧

**Status:** ✅ 100% COMPLETE  
**Last Updated:** 2026-04-30  
**Files:** 13/13 (All required files complete)

---

## Country Overview

The United Kingdom is the world's 6th largest economy by GDP ($3.59 trillion) and a global financial hub. Known for its tech ecosystem (London's Silicon Roundabout), strong regulatory framework (GDPR post-Brexit), and innovation-friendly approach to AI (AI Safety Summit legacy).

- **Capital:** London
- **Population:** 67,600,000
- **Currency:** GBP (British Pound Sterling) - £
- **Official Language:** English
- **EU Member:** No (left 2020, post-Brexit)
- **Commonwealth:** Yes (headquartered in London)

---

## Data Structure (13/13 Files Complete)

| Category | File | Status |
|----------|------|--------|
| **Core** | COUNTRY.md | ✅ |
| **Legal** | legal/internet-law.yaml | ✅ |
| **Legal** | legal/labor-law.yaml | ✅ |
| **Fiscal** | fiscal/tax-codes.yaml | ✅ |
| **Financial** | financial/banks.yaml | ✅ |
| **Telecom** | telecom/phone-formats.yaml | ✅ |
| **Demographics** | demographics/population.yaml | ✅ |
| **Tech** | tech/ai-cloud-services.yaml | ✅ |
| **Business** | business/company-sizes.yaml | ✅ |
| **Business** | business/real-estate.yaml | ✅ |
| **Business** | business/import-export.yaml | ✅ |
| **Marketing** | marketing/digital-marketing.yaml | ✅ |
| **Docs** | README.md | ✅ |

---

## Key Facts for AI Agents

### 🚨 Critical Brexit & Regulatory Considerations
- **Brexit:** Left EU Single Market (2020), new UK GDPR, UKCA marking replaces CE
- **Open Banking:** 600+ fintechs via Open Banking (PSD2 equivalent)
- **Faster Payments:** Real-time payments 24/7/365 (3.2B txns/year)
- **London:** Major fintech hub (Silicon Roundabout, 3rd in Europe)
- **AI Safety:** World's first AI Safety Summit (2023, Bletchley Park)
- **Monzo/Starling:** Digital-only banks revolutionizing banking
- **Corporate Tax:** Increased to 25% (April 2023, was 19%)
- **VAT:** 20% standard, £85K registration threshold

### Cloud & AI Infrastructure
- **Top Cloud Providers:** AWS (31%), Microsoft Azure (26%), Google Cloud (11%)
- **AI Models:** DeepMind (Google) HQ in London, world-leading AI research
- **AI Safety Institute:** World's first dedicated AI safety regulator (2023)
- **GPU Access:** A100/V100 via AWS/Azure/GCP (London region)
- **AI Policy:** Risk-based, innovation-friendly (AI Safety Act expected 2026)

### Banking & Finance
- **Faster Payments:** 3.2B txns/year, £1M limit, 24/7/365
- **Top Banks:** HSBC (15%), Barclays (12%), Lloyds (11%), NatWest (10.5%)
- **Digital Banks:** Monzo (5M+), Starling (4M+), Chase UK (3M+)
- **Open Banking:** 600+ fintechs authorized (AIS + PIS services)
- **Crypto:** No ban, FCA registration required (strict advertising rules)

### Legal & Compliance
- **Data Protection:** UK GDPR + Data Protection Act 2018
- **Cybersecurity:** NIS Regulations 2018, Cyber Essentials scheme
- **AI Regulation:** AI Safety Act (draft 2023, expected 2026)
- **Digital Markets Act:** 2024 (interoperability, transparency)
- **Online Safety Act:** 2023 (duty of care, age verification)
- **Corporate Tax:** 25% (main rate), 19% (small profits <£50K)

---

## Important Government Agencies

| Agency | Role |
|--------|------|
| **Companies House** | Company registration, public records |
| **HMRC** (HM Revenue & Customs) | Tax collection, VAT, customs |
| **BoE** (Bank of England) | Central bank, monetary policy |
| **ICO** (Information Commissioner's Office) | Data protection, UK GDPR enforcement |
| **FCA** (Financial Conduct Authority) | Financial services regulation |
| **DSIT** (Dept for Science, Innovation & Tech) | AI policy, digital economy |

---

## Sources
- Companies House: https://www.gov.uk/government/organisations/companies-house
- HM Revenue & Customs: https://www.gov.uk/government/organisations/hm-revenue-customs
- Bank of England: https://www.bankofengland.co.uk
- Information Commissioner's Office: https://ico.org.uk
- Department for Science, Innovation & Tech: https://www.gov.uk/government/organisations/department-for-science-innovation-and-technology

---

## Integration Examples

### Paperclip
```yaml
- name: "Check UK VAT rate"
  action: "get_tax_rate"
  country: "uk"
  tax_type: "vat_standard"
# Returns: 20
```

### OpenClaw
```json
{
  "country": "uk",
  "data_needed": ["faster_payments", "open_banking", "ai_safety"],
  "language": "en-GB"
}
```

### Hermes
```python
from countries import UK
uk = UK()
print(uk.financial.banks["payment_systems"]["faster_payments"]["volume_annual"])  # 3.2B
print(uk.tech.ai_cloud_services["cloud_providers"][0]["name"])  # AWS
```

---

**Disclaimer:** All data provided AS IS. Verify with official sources before use. See [DISCLAIMER.md](../DISCLAIMER.md).

**Note:** The UK is a global financial hub post-Brexit with a pro-innovation AI approach. Faster Payments (3.2B txns/year) and Open Banking (600+ fintechs) are critical for fintech integration. DeepMind (Google) HQ in London represents world-leading AI research. AI agents must comply with UK GDPR (not EU GDPR) and prepare for the AI Safety Act (expected 2026). London's Silicon Roundabout is Europe's largest tech hub (120+ unicorns).
