# China 🇨🇳

**Status:** ✅ 100% COMPLETE  
**Last Updated:** 2026-04-30  
**Files:** 13/13 (All required files complete)

---

## Country Overview

China is the world's 2nd largest economy by GDP ($18.53 trillion) and the most populous country (1.41 billion). Known for its rapid digital transformation, massive e-commerce ecosystem, and strict internet governance.

- **Capital:** Beijing (北京)
- **Population:** 1,412,600,000
- **Currency:** CNY (Chinese Yuan Renminbi) - ¥
- **Official Language:** Mandarin Chinese (Simplified Chinese)
- **WTO Member:** Yes (since 2001)
- **RCEP Member:** Yes (since 2022)

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

### 🚨 Critical Internet & Regulatory Considerations
- **Internet Censorship (Great Firewall):** Google, Facebook, Twitter, WhatsApp, YouTube are ALL BLOCKED
- **Data Localization:** PIPL requires Chinese user data stored in China
- **AI Regulation:** Generative AI must be labeled, filed with CAC, follow "socialist core values"
- **Search Engine:** Baidu (65%), Bing China (18%) - Google blocked
- **Social Media:** WeChat (1.3B MAU), Douyin/TikTok (750M), Weibo (580M)

### Digital Payment Ecosystem (90% adoption!)
- **WeChat Pay:** 1.3B users (40% market share)
- **Alipay:** 1.2B users (38% market share)
- **UnionPay:** 1B users (20% - card network)
- **Digital Yuan (e-CNY):** CBDC pilot in 23 cities (300M users)

### Business Environment
- **Company Registration:** SAMR (State Administration for Market Regulation)
- **Business Culture:** Guanxi (relationships) critical, face-saving (面子) important
- **Working Culture:** Often "9-9-6" (9am-9pm, 6 days/week in tech)
- **Entity Types:** WFOE (外商独资), JV, Representative Office

### Cloud & AI Infrastructure
- **Top Cloud Providers:** Alibaba Cloud (37%), Tencent Cloud (16%), Huawei Cloud (11%)
- **LLMs:** Qwen (Alibaba), Hunyuan (Tencent), Ernie (Baidu), ChatGLM (Zhipu)
- **GPUs:** Huawei Ascend 910B (main A100 alternative), Nvidia restricted
- **AI Compute:** World's largest AI clusters (multiple 50K+ GPU facilities)

### Legal & Compliance
- **Data Protection:** PIPL (effective 2021), CSL (2017), DSL (2021)
- **AI Content:** Must be labeled as AI-generated, no "socialist values" violations
- **Fapiao:** Official tax invoice MANDATORY for all business transactions
- **Company Chops:** Legally binding (more than signatures)

---

## Important Government Agencies

| Agency | Role |
|--------|------|
| **SAMR** (市场监管总局) | Business registration, antitrust |
| **CAC** (网信办) | Internet regulation, AI governance |
| **MIIT** (工信部) | Telecom, cloud licensing |
| **PBOC** (央行) | Central bank, fintech, Digital Yuan |
| **GACC** (海关总署) | Customs, import/export |
| **STA** (税务总局) | Tax collection (VAT 13%, CIT 25%) |
| **MOHRSS** (人社部) | Labor law, social insurance |

---

## Sources
- National Bureau of Statistics: https://www.stats.gov.cn
- State Taxation Administration: https://www.chinatax.gov.cn
- Cyberspace Administration (CAC): https://www.cac.gov.cn
- Ministry of Commerce: https://www.mofcom.gov.cn
- General Administration of Customs: https://www.customs.gov.cn

---

## Integration Examples

### Paperclip
```yaml
- name: "Check Chinese VAT rate"
  action: "get_tax_rate"
  country: "cn"
  tax_type: "vat_standard"
# Returns: 13
```

### OpenClaw
```json
{
  "country": "china",
  "data_needed": ["payment_methods", "social_media", "ai_models"],
  "language": "zh-CN"
}
```

### Hermes
```python
from countries import China
cn = China()
print(cn.financial.banks["digital_payments"]["adoption_rate"])  # 90%
print(cn.tech.ai_cloud_services["cloud_providers"][0]["name"])  # Alibaba Cloud
```

---

**Disclaimer:** All data provided AS IS. Verify with official sources before use. See [DISCLAIMER.md](../DISCLAIMER.md).

**Note:** This is the most complex country profile due to China's unique internet governance, massive digital ecosystem, and strict data localization requirements. AI agents operating in China MUST use domestic alternatives (Baidu, WeChat, Alipay, Alibaba Cloud) and comply with PIPL, CSL, and AI regulations.
