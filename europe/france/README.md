# France 🇫🇷

**Status:** ✅ 100% COMPLETE  
**Last Updated:** 2026-04-30  
**Files:** 13/13 (All required files complete)

---

## Country Overview

France is the world's 7th largest economy by GDP ($3.11 trillion) and a founding EU member. Known for its strong privacy laws (GDPR gold standard), world-leading AI ecosystem (Mistral AI, HuggingFace), and sovereign cloud strategy (OVHcloud).

- **Capital:** Paris
- **Population:** 68,200,000
- **Currency:** EUR (Euro) - €
- **Official Language:** French (Français)
- **EU Member:** Yes (founding member)
- **Eurozone:** Yes
- **Primary Language for AI:** French (fr-FR), English accepted

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
- **GDPR:** Gold standard (€20M or 4% revenue fines, CNIL enforcement)
- **EU AI Act:** First global AI law (adopted March 2024, phased to 2027)
- **Mistral AI:** Leading European LLM (Paris HQ, Mixtral 8x7B)
- **HuggingFace:** Global open-source leader (Paris offices)
- **Cartes Bancaires:** 95% of card payments (MANDATORY for businesses)
- **OVHcloud:** French sovereign cloud (10% market share, 5 AZs in France)
- **Toubon Law:** French MANDATORY for consumer-facing content
- **Corporate Tax:** 25% flat rate (down from 33.3% in 2020)
- **VAT:** 20% standard, 10% reduced, 5.5% super-reduced
- **SIREN (9 digits):** Company ID, SIRET (14 digits): Establishment ID

### Cloud & AI Infrastructure
- **Top Cloud Providers:** AWS (28%), Microsoft Azure (25%), Google Cloud (12%)
- **French Cloud:** OVHcloud (10%, sovereign), Scaleway (5%, eco-friendly)
- **AI Models:** Mistral AI (7B params), HuggingFace (100K+ models)
- **AI Policy:** Pro-innovation, sovereign cloud (SecNumCloud certification)
- **GPU Access:** A100/V100 via AWS/Azure/GCP/OVH (Paris region)
- **AI Startups:** 600+ companies, €3B+ funding (2025)

### Banking & Finance
- **Cartes Bancaires:** 95% of card payments (mandatory support)
- **Top Banks:** BNP Paribas (15%), Crédit Agricole (12%), Société Générale (10%)
- **SEPA:** 4.2B txns/year, instant payments available (€100K limit)
- **Neobanks:** Qonto (4M SMEs), Shine (3M freelancers)
- **Savings:** Livret A (€22,950 limit, 3.0%, 55M users, tax-free)
- **Crypto:** Legal, 4.5M users, AMF registration required (DASP)

### Legal & Compliance
- **Data Protection:** GDPR + CNIL (€20M or 4% revenue fines)
- **AI Regulation:** EU AI Act (phased 2024-2027), GPAI models
- **Digital Services Act:** Feb 2024 (VLOPs need audits)
- **Corporate Tax:** 25% (flat rate), 15% for small SMEs (<€38,120 profit)
- **VAT Registration:** €85K (goods), €34K (services)
- **Tax Credits:** CIR (R&D, 30% up to €100M), CII (innovation, 20%)

---

## Important Government Agencies

| Agency | Role |
|--------|------|
| **INSEE** (National Statistics) | Demographics, GDP, economic data |
| **DGFIP** (Tax Authority) | VAT, corporate tax, personal tax |
| **Banque de France** | Central bank, monetary policy |
| **CNIL** (Data Protection) | GDPR enforcement, privacy complaints |
| **ACPR** (Banking Regulator) | Banking + insurance supervision |
| **ARCEP** (Telecom Regulator) | Internet, telecom, 5G spectrum |
| **INPI** (Intellectual Property) | Patents, trademarks, designs |

---

## Sources
- INSEE (National Statistics): https://www.insee.fr
- DGFIP (Tax Authority): https://www.impots.gouv.fr
- Banque de France: https://www.banque-france.fr
- CNIL (Data Protection): https://www.cnil.fr
- ACPR (Banking): https://www.acpr.banque-france.fr

---

## Integration Examples

### Paperclip
```yaml
- name: "Check French VAT rate"
  action: "get_tax_rate"
  country: "france"
  tax_type: "vat_standard"
# Returns: 20
```

### OpenClaw
```json
{
  "country": "france",
  "data_needed": ["cart_bancaires", "mistral_ai", "eu_ai_act"],
  "language": "fr-FR"
}
```

### Hermes
```python
from countries import France
fr = France()
print(fr.financial.banks["payment_systems"][0]["market_share"])  # 95 (CB)
print(fr.tech.ai_cloud_services["llm_models"][0]["name"])  # Mistral AI
```

---

**Disclaimer:** All data provided AS IS. Verify with official sources before use. See [DISCLAIMER.md](../DISCLAIMER.md).

**Note:** France is a founding EU member with the world's strongest privacy laws (GDPR gold standard) and first AI regulation (EU AI Act 2024). Mistral AI (Paris HQ) leads European LLM development. Cartes Bancaires (CB) are mandatory for French businesses (95% penetration). Sovereign cloud strategy (OVHcloud, Scaleway) ensures data residency. Toubon Law requires French language for all consumer content. Paris is Europe's 2nd tech hub after London (Station F = world's largest startup campus).
