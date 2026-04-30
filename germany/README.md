# Germany 🇩🇪

**Status:** ✅ 100% COMPLETE  
**Last Updated:** 2026-04-30  
**Files:** 13/13 (All required files complete)

---

## Country Overview

Germany is the largest economy in Europe and the 3rd largest by GDP globally. Known for its engineering excellence, automotive industry, and strong manufacturing base.

- **Capital:** Berlin
- **Population:** 84.7 million
- **Currency:** EUR (Euro) - €
- **Official Language:** German (Deutsch)
- **EU Member:** Yes (since 1957)
- **Schengen Member:** Yes

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

### Business Environment
- **Company Registration:** Handelsregister (Commercial Register)
- **Business Culture:** Punctual, direct communication, consensus-driven
- **Working Hours:** Weekdays 8:00-18:00, Saturday 9:00-14:00, Sunday closed
- **Data Privacy:** GDPR + German BDSG + TTDSG (strict cookie consent)

### Digital Infrastructure
- **Internet Penetration:** 95% (79M users)
- **Smartphone Penetration:** 81%
- **Top Cloud Providers:** AWS, Azure, Google Cloud, IONOS, Hetzner
- **Payment Methods:** PayPal (52%), Credit Card (18%), Klarna/Sofort (22%)

### Legal & Compliance
- **Cookie Consent:** MANDATORY before tracking (TTDSG law)
- **Data Protection Officer:** Required if >20 employees
- **GDPR Fines:** Up to €20M or 4% of global revenue
- **Real Estate Transfer Tax:** 3.5-6.5% (varies by state)

---

## Sources
- Federal Statistical Office (Destatis): https://www.destatis.de
- German Customs (Zoll): https://www.zoll.de
- Federal Office for Economic Affairs (BAFA): https://www.bafa.de
- GDPR: https://gdpr.eu
- IONOS: https://www.ionos.com

---

## Integration Examples

### Paperclip
```yaml
- name: "Check German VAT ID"
  action: "validate_vat"
  country: "de"
  vat_number: "DE123456789"
```

### OpenClaw
```json
{
  "country": "germany",
  "data_needed": ["tax_codes", "banks", "phone_formats"],
  "language": "de"
}
```

### Hermes
```python
from countries import Germany
de = Germany()
print(de.fiscal.tax_codes["vat_standard"])  # 19%
```

---

**Disclaimer:** All data provided AS IS. Verify with official sources before use. See [DISCLAIMER.md](../DISCLAIMER.md).
