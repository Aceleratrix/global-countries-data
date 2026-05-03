# Poland 🇵🇱

**Status:** ✅ 100% COMPLETE  
**Last Updated:** 2026-05-03  
**Files:** 13/13 (All required files complete)

---

## Country Overview

Poland is the world's 20th largest economy by GDP ($800 billion) and a key EU member since 2004. Known for its fast-growing tech sector, dominant BLIK payment system, and strong SME base (2.1M businesses).

- **Capital:** Warsaw
- **Population:** 38,200,000
- **Currency:** PLN (Polish złoty) - zł
- **Official Language:** Polish (Polski)
- **EU Member:** Yes (joined 2004)
- **Eurozone:** No (uses PLN, adoption pending)
- **Primary Language for AI:** Polish (pl-PL), English accepted

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

### 🚨 Critical EU & Local Considerations
- **GDPR:** Full compliance (EU member, UODO enforcement)
- **BLIK:** 60% of online transactions (MANDATORY for Polish e-commerce)
- **EU Funds:** €770B from EU 2021-2027 (drives digital transformation)
- **SME Sector:** 2.1M businesses (99% of all enterprises)
- **Corporate Tax:** 19% flat rate, 9% for small taxpayers
- **VAT:** 23% standard, 8% reduced, 5% super-reduced
- **IBAN:** 28 characters (PL prefix, 2 check digits, 24 account digits)
- **Phone:** +48, 9 digits (no leading zero, 4 major operators)

### Cloud & AI Infrastructure
- **Top Cloud Providers:** AWS (30%), Microsoft Azure (25%), Google Cloud (15%)
- **Local Cloud:** Orange Cloud (8%), T-Mobile Cloud (5%)
- **AI Ecosystem:** 300+ AI startups, VoiceLab (leading Polish AI company)
- **GPU Access:** A100/V100 via AWS/Azure/GCP (Warsaw region)
- **AI Funding:** €500M+ (2025), government support for AI initiatives

### Banking & Finance
- **BLIK:** 60% of online transactions (40M users, instant P2P/c2b)
- **Top Banks:** PKO BP (18%), Bank Pekao (12%), ING Bank Śląski (10%)
- **SEPA:** 1.8B txns/year, instant payments available (€100K limit)
- **Neobanks:** Revolut (3M users), mBank (2M users)
- **Savings:** 35M savings accounts, average interest 4.5% (2025)

### Legal & Compliance
- **Data Protection:** GDPR + UODO (€20M or 4% revenue fines)
- **Corporate Tax:** 19% flat rate, 9% for small taxpayers (<€2M revenue)
- **VAT Registration:** €42K (goods), €21K (services)
- **Labor Law:** 40h/week max, overtime 150-200%, 20-26 days vacation

---

## Important Government Agencies

| Agency | Role |
|--------|------|
| **GUS** (Statistics Poland) | Demographics, GDP, economic data |
| **NBP** (National Bank of Poland) | Central bank, monetary policy |
| **UODO** (Data Protection Office) | GDPR enforcement, privacy complaints |
| **MF** (Ministry of Finance) | VAT, corporate tax, personal tax |
| **UKE** (Telecom Regulator) | Internet, telecom, 5G spectrum |
| **URPL** (Patent Office) | Patents, trademarks, designs |

---

## Sources
- Statistics Poland (GUS): https://stat.gov.pl
- National Bank of Poland: https://www.nbp.pl
- Personal Data Protection Office: https://uodo.gov.pl
- Ministry of Finance: https://www.gov.pl/web/finance
- Official Tourism: https://www.poland.travel

---

## Integration Examples

### Paperclip
```yaml
- name: "Check Polish VAT rate"
  action: "get_tax_rate"
  country: "poland"
  tax_type: "vat_standard"
# Returns: 23
```

### OpenClaw
```json
{
  "country": "poland",
  "data_needed": ["blik_payments", "sme_sector", "eu_funds"],
  "language": "pl-PL"
}
```

### Hermes
```python
from countries import Poland
pl = Poland()
print(pl.financial.banks["payment_systems"][0]["market_share"])  # 60 (BLIK)
print(pl.tech.ai_cloud_services["leading_ai_company"][0]["name"])  # VoiceLab
```

---

**Disclaimer:** All data provided AS IS. Verify with official sources before use. See [DISCLAIMER.md](../DISCLAIMER.md).

**Note:** Poland is a fast-growing Central European EU member with the region's most dynamic tech sector. BLIK is the dominant local payment method (60% of online transactions). Strong SME base (2.1M businesses) drives economic growth. EU funds (€770B 2021-2027) accelerate digital transformation. Warsaw is the region's leading tech hub (Google, Amazon, Microsoft offices). Labor laws require careful HR compliance.
