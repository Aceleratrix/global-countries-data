# India 🇮🇳

**Status:** ✅ 100% COMPLETE  
**Last Updated:** 2026-04-30  
**Files:** 13/13 (All required files complete)

---

## Country Overview

India is the world's 5th largest economy by GDP ($3.94 trillion) and the most populous country (1.43 billion, surpassing China in 2023). Known for its digital revolution (UPI processing 12B+ transactions/month), massive IT services sector, and youthful demographic (median age 28.2).

- **Capital:** New Delhi
- **Population:** 1,428,600,000 (world's largest)
- **Currency:** INR (Indian Rupee) - ₹
- **Official Languages:** Hindi, English (+ 21 scheduled languages)
- **BRICS Member:** Yes (since 2024 with new members)
- **RCEP Member:** No (opted out in 2019)

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

### 🚨 Critical Digital & Business Considerations
- **Digital Payment Revolution:** UPI processes 12B+ transactions/month (world's largest real-time payment system!)
- **Data Localization:** DPDPA 2023 requires sensitive personal data stored in India
- **WhatsApp Dominance:** 530M users - CRITICAL for customer engagement
- **Jio Effect:** Reliance Jio's cheap data (₹10/GB) transformed internet access (748M users)
- **Language Diversity:** 22 official languages, Hindi/English primary for business
- **Digital India:** Government initiative (2015-2030) - Aadhaar (1.3B), UPI, DigiLocker

### Cloud & AI Infrastructure
- **Top Cloud Providers:** AWS (32%), Microsoft Azure (24%), Google Cloud (15%)
- **AI Models:** BharatGPT (IIT Bombay - 22 languages), Krutim (Ola), Hanooman (IIT)
- **GPU Access:** A100/V100 via AWS/Azure/GCP (Mumbai, Hyderabad, Delhi regions)
- **AI Policy:** Light-touch, ethics-based (draft guidelines 2023, expected 2026)

### Banking & Finance
- **UPI (Unified Payments Interface):** 12B+ txns/month, 75% adoption
- **Top Banks:** SBI (23%), HDFC (15%), ICICI (12%), Kotak (6%)
- **Digital Wallets:** PhonePe (45% UPI share), Google Pay (35%), Paytm (15%)
- **RuPay:** 800M domestic cards (60% market share, beats Visa/MC)

### Legal & Compliance
- **Data Protection:** DPDPA 2023 (effective 2024, India's GDPR)
- **Cybersecurity:** IT Act 2000 (amended 2008)
- **GST:** 5 slabs (0%, 5%, 12%, 18%, 28%) - unified indirect tax
- **Corporate Tax:** 25% (domestic), 40% (foreign companies)

---

## Important Government Agencies

| Agency | Role |
|--------|------|
| **MCA** (Ministry of Corporate Affairs) | Company registration, LLP formation |
| **RBI** (Reserve Bank of India) | Central bank, payment systems (UPI), fintech |
| **MEITY** (Ministry of Electronics & IT) | Digital India, IT Act, AI policy |
| **DPIIT** (Dept of Promotion of Industry) | Startup India, FDI norms |
| **CBDT** (Central Board of Direct Taxes) | Income tax, corporate tax |
| **DGFT** (Directorate General of Foreign Trade) | IEC issuance, export schemes |
| **GSTN** (GST Network) | GST collection, compliance |

---

## Sources
- Ministry of Corporate Affairs: https://www.mca.gov.in
- Reserve Bank of India: https://www.rbi.org.in
- Ministry of Electronics & IT: https://www.meity.gov.in
- Digital India: https://www.digitalindia.gov.in
- GST Portal: https://www.gst.gov.in

---

## Integration Examples

### Paperclip
```yaml
- name: "Check Indian GST rate"
  action: "get_tax_rate"
  country: "in"
  tax_type: "gst_standard"
# Returns: 18
```

### OpenClaw
```json
{
  "country": "india",
  "data_needed": ["upi_payments", "digital_wallets", "ai_models"],
  "language": "hi-IN"
}
```

### Hermes
```python
from countries import India
in = India()
print(in.financial.banks["payment_systems"]["upi_unified_payments_interface"]["volume_monthly"])  # 12B+
print(in.tech.ai_cloud_services["cloud_providers"][0]["name"])  # AWS
```

---

**Disclaimer:** All data provided AS IS. Verify with official sources before use. See [DISCLAIMER.md](../DISCLAIMER.md).

**Note:** India is the world's fastest-growing major economy with a massive digital ecosystem. UPI (12B+ monthly transactions) is the world's largest real-time payment system. WhatsApp (530M users) is CRITICAL for customer engagement. AI agents must integrate UPI for digital products and support Hindi/English + 22 regional languages.
