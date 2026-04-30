# Italy 🇮🇹

**Status:** ✅ 100% COMPLETE  
**Last Updated:** 2026-04-30  
**Files:** 13/13 (All required files complete)

---

## Country Overview

Italy is the world's 8th largest economy by GDP ($2.33 trillion) and a founding EU member. Known for its SME sector (family businesses), luxury/fashion leadership (Gucci, Prada), and unique labor law (no statutory minimum wage in EU).

- **Capital:** Rome (Roma)
- **Population:** 58,900,000
- **GDP:** $2.33 trillion (8th largest globaly)
- **Currency:** EUR (Euro) - €
- **Language:** Italian (Italiano)
- **EU Member:** Yes (founding member)
- **Eurozone:** Yes
- **Primary Language for AI:** Italian (it-IT), English accepted

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

### 🚨 Critical EU & Sovereignty Considerations
- **GDPR:** Standard (€20M or 4% revenue fines, GPDP enforcement)
- **EU AI Act:** Adopted March 2024 (phased to 2027)
- **i-gen:** Italian LLM (CINECA/University of Bari)
- **Satispay:** 10M+ users (Italian P2P, exponential growth)
- **Bancomat:** 95% of POS payments (MANDATORY for shops >€60)
- **SPID:** 38M users (mandatory digital ID for gov services)
- **No Minimum Wage:** Unique in EU (CCNL collective agreements set ~€1,200-1,500)
- **Corporate Tax:** 24% (IRES) + 3.9% (IRAP) = 27.9%
- **VAT:** 22% standard, 10% reduced, 4% super-reduced
- **Codice Fiscale:** 16 chars (surname+name+birthdate+comune)

### Cloud & AI Infrastructure
- **Top Cloud Providers:** AWS (25%), Microsoft Azure (22%), Google Cloud (10%)
- **Italian Cloud:** Aruba (15%, sovereign), Seeweb (8%, sustainability)
- **AI Models:** i-gen (Italian LLM), Mistral available
- **AI Policy:** EU AI Act supporter, 400+ AI startups
- **GPU Access:** A100/V100 via AWS/Azure/GCP/Aruba (Milan region)
- **AI Startups:** 400+ companies, €1.5B+ funding (2025)

### Banking & Finance
- **Bancomat:** 95% of POS payments (mandatory for shops >€60)
- **Top Banks:** Intesa Sanpaolo (18%), UniCredit (15%), MPS (5%)
- **SEPA:** 3.8B txns/year, instant payments available (€100K limit)
- **Neobanks:** FinecoBank (3.5M), Widiba (2M), CheBanca! (1.5M)
- **Savings:** Titoli di Stato (3.8% yield), 25M users
- **Crypto:** Legal, 3.8M users, OAM registration required

### Legal & Compliance
- **Data Protection:** GDPR + GPDP (€20M or 4% revenue fines)
- **AI Regulation:** EU AI Act (phased 2024-2027), GPAI models
- **Digital Services Act:** Feb 2024 (VLOPs need audits)
- **Corporate Tax:** 24% (IRES) + 3.9% (IRAP) = 27.9%
- **VAT Registration:** €85K threshold (goods/services)
- **Tax Credits:** R&D (20% up to €5M), Mezzogiorno (25-45%), Bonus Edilizia (50-110%)
- **Codice Fiscale:** 16 chars (surname+name+birthdate+comune)
- **Partita IVA:** 11 digits (VAT number, same as tax code)

---

## Important Government Agencies

| Agency | Role |
|--------|------|
| **ISTAT** (National Statistics) | Demographics, GDP, economic data |
| **Agenzia Entrate** (Tax Authority) | VAT, corporate tax, personal tax |
| **Banca d'Italia** | Central bank, monetary policy |
| **GPDP** (Data Protection) | GDPR enforcement, privacy complaints |
| **CONSOB** (Market Regulator) | Securities, stock exchange |
| **AGCOM** (Telecom Regulator) | Internet, telecom, content moderation |
| **Camera di Commercio** | Business registration (Registro Imprese) |

---

## Sources
- ISTAT (National Statistics): https://www.istat.it
- Agenzia Entrate (Tax Authority): https://www.agenziaentrate.gov.it
- Banca d'Italia: https://www.bancaditalia.it
- GPDP (Data Protection): https://www.garanteprivacy.it
- CONSOB (Markets): https://www.consob.it

---

## Integration Examples

### Paperclip
```yaml
- name: "Check Italian VAT rate"
  action: "get_tax_rate"
  country: "italy"
  tax_type: "vat_standard"
# Returns: 22
```

### OpenClaw
```json
{
  "country": "italy",
  "data_needed": ["bancomat", "satispay", "i-gen", "spid"],
  "language": "it-IT"
}
```

### Hermes
```python
from countries import Italy
it = Italy()
print(it.financial.banks["payment_systems"][0]["market_share"])  # 95 (Bancomat)
print(it.tech.ai_cloud_services["llm_models"][0]["name"])  # i-gen
```

---

**Disclaimer:** All data provided AS IS. Verify with official sources before use. See [DISCLAIMER.md](../DISCLAIMER.md).

**Note:** Italy is a founding EU member with unique labor law (NO statutory minimum wage in EU - CCNL sets ~€1,200-1,500). Bancomat (Italian debit) is 95% penetration (mandatory for shops >€60). Satispay (10M+ users) is the Italian fintech success story. SPID (38M users) is mandatory digital ID for public services. Milan is the financial/tech hub (3.1M metro). Strong SME sector (4.4M companies, 99.9% of enterprises). Italy excels in fashion/luxury (Gucci, Prada, 80+ brands using AI).
