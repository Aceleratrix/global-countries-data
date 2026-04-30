# 🌍 Global Countries Data

> **The world's most comprehensive country data repository for AI agents** — structured YAML datasets covering legal, fiscal, telecom, business, and tech infrastructure for every country. Plug into Paperclip, OpenClaw, Hermes, and any multi-agent system for truly localized AI operations.

[![GitHub stars](https://img.shields.io/github/stars/Aceleratrix/global-countries-data?style=social)](https://github.com/Aceleratrix/global-countries-data)
[![GitHub forks](https://img.shields.io/github/forks/Aceleratrix/global-countries-data?style=social)](https://github.com/Aceleratrix/global-countries-data)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Aceleratrix/global-countries-data/blob/main/LICENSE)
[![Status: 3 Countries 100% Complete](https://img.shields.io/badge/Status-3 Countries 100% Complete-green)](https://github.com/Aceleratrix/global-countries-data)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Powered by YAML](https://img.shields.io/badge/Powered_by-YAML-blue)](https://yaml.org/)

---

## 🚀 What Is This?

A structured, machine-readable database of country-specific data designed for **AI agents and multi-agent systems**. Each country folder contains 13-17 YAML files covering everything an AI system needs to operate in that jurisdiction:

- **🏛️ Legal & Regulatory** — Privacy laws (GDPR, LGPD, APPI), AI regulations, employment law
- **💰 Fiscal & Financial** — Tax codes, VAT/sales tax, banking systems, payment methods (PIX, SEPA, Konbini)
- **📱 Telecom & Demographics** — Phone formats, postal codes, population data, internet infrastructure
- **🏢 Business & Company** — Company types, sizes, software APIs, real estate, import/export
- **🤖 Tech & AI Services** — Cloud regions (AWS/GCP/Azure), LLM APIs, GPU providers, tech hubs
- **📢 Marketing** — Digital platforms, ad networks, social media penetration

### Why It Matters

| Feature | Benefit for AI Agents |
|---------|----------------------|
| **Structured YAML** | Direct `cat country/file.yaml` — no parsing needed |
| **Schema-Validated** | JSON Schema enforcement via CI/CD |
| **AI-First Design** | Every field chosen for agent decision-making |
| **Multi-Agent Ready** | Drop into Paperclip, OpenClaw, Hermes, LangChain, AutoGPT |
| **Regionalized** | Agents respect local laws, payments, and culture |

---

## 📊 Coverage Progress (3 / 195 = 1.5%)

| Country | Files | Status | Key Highlights | Primary Language |
|---------|-------|--------|-----------------|-----------------|
| 🇧🇷 **Brazil** | 17/17 | ✅ **100% COMPLETE** | PIX (76% adoption), LGPD, 4 cloud regions | Portuguese (pt-BR) + English |
| 🇺🇸 **USA** | 13/13 | ✅ **100% COMPLETE** | Silicon Valley, Section 230, 20+ cloud regions | English (en-US) |
| 🇯🇵 **Japan** | 14/14 | ✅ **100% COMPLETE** | Konbini (25% e-commerce!), LINE (95%), Society 5.0 | English (en-US) |
| 🇩🇪 **Germany** | 8/13 | 🚧 **IN PROGRESS** | GDPR (gold standard), EU AI Act, SEPA, Industry 4.0 | English (en-US) |

**Total: 44 structured YAML files covering 3 countries!**

---

## 🤖 Quick Start for AI Agents

### Paperclip Integration
```bash
# Import country data into your Paperclip agent company
npx paperclip company import --from ./global-countries-data/brazil
```

### Direct YAML Access (Hermes / OpenClaw)
```yaml
# Example: Check phone formats in USA
cat usa/telecom/phone-formats.yaml

# Example: Check privacy laws in Japan  
cat japan/legal/internet-law.yaml

# Example: Get payment methods in Brazil
cat brazil/financial/payment-apis.yaml
```

### Python / LangChain / AutoGPT
```python
import yaml
import os

def load_country_data(country_code):
    """Load all YAML data for a country."""
    country_path = f"global-countries-data/{country_code}/"
    data = {}
    for root, dirs, files in os.walk(country_path):
        for file in files:
            if file.endswith('.yaml'):
                with open(os.path.join(root, file)) as f:
                    key = file.replace('.yaml', '')
                    data[key] = yaml.safe_load(f)
    return data

# Load Brazil data
brazil = load_country_data('brazil')
print(brazil['tax-codes']['vat']['standard_rate_percent'])  # 17.5
```

---

## 📁 Repository Structure

```
global-countries-data/
├── brazil/          # 🇧🇷 100% COMPLETE (17 files)
│   ├── COUNTRY.md
│   ├── README.md    # Full documentation
│   ├── fiscal/
│   ├── financial/
│   ├── telecom/
│   ├── demographics/
│   ├── business/
│   ├── legal/
│   ├── tech/
│   └── marketing/
│
├── usa/             # 🇺🇸 100% COMPLETE (13 files)
│   └── ... (same structure as brazil)
│
├── japan/           # 🇯🇵 100% COMPLETE (14 files)
│   └── ... (same structure as brazil)
│
├── germany/         # 🇩🇪 IN PROGRESS (8 files)
│   └── ... (same structure as brazil)
│
├── schemas/         # JSON Schema validation
├── scripts/         # Python validation scripts
├── templates/       # Country template (copy to start new country)
├── assets/          # Images, prompts, diagrams
└── CONTRIBUTING.md  # Contributor guidelines
```

---

## 🎯 AI-First Highlights

### 🇧🇷 Brazil
- **PIX Mandatory** — 76% adoption, instant 24/7, FREE for merchants
- **LGPD Complete** — Max 2% revenue fines, DPO mandatory
- **4 Cloud Regions** — AWS (2011), GCP (2017), Azure (2014), Oracle (2021)
- **13,000 Startups** — 17 unicorns, 5th largest in Latin America

### 🇺🇸 USA (Silicon Valley Focus)
- **Section 230** — Platform immunity (unique in world!)
- **20+ Cloud Regions** — AWS, GCP, Azure, Oracle (unmatched!)
- **At-Will Employment** — Fire anytime, no reason needed
- **$89B VC Deployed** (2025) — World's largest ecosystem

### 🇯🇵 Japan (Tokyo Tech Hub)
- **Konbini Payments** — 25% e-commerce at 56,000 stores! UNIQUE!
- **LINE** — 95% penetration (Japanese WhatsApp with payments!)
- **Society 5.0** — $2B government AI investment
- **Non-Competes NOT Enforceable** — Can join competitors!
- **No Daylight Saving Time** — UTC+9 always!

### 🇩🇪 Germany (In Progress)
- **GDPR (Gold Standard)** — Max €20M or 4% revenue (inspired LGPD, APPI!)
- **EU AI Act (2024)** — **WORLD'S FIRST comprehensive AI law!**
- **SEPA Direct Debit** — 40% e-commerce (Eurozone standard!)
- **Co-determination** — 50% worker board seats! UNIQUE TO GERMANY!
- **Industry 4.0** — Smart factories with AI/IoT (global leader!)

---

## 🌍 Roadmap (Next Countries)

| Country | Priority | Reason |
|---------|----------|--------|
| 🇬🇧 UK | High | Financial hub, Brexit, Open Banking |
| 🇮🇳 India | High | 1.4B people, UPI payments, tech hub |
| 🇨🇳 China | Medium | Largest population, Alipay/WeChat, Great Firewall |
| 🇫🇷 France | Medium | GDPR origin, 2nd largest EU economy |
| 🇦🇺 Australia | Medium | APAC hub, proximity to Japan |
| 🇸🇬 Singapore | Low | Asian financial hub, very small |
| 🇰🇷 South Korea | Low | K-pop, advanced tech, 5G leader |

**Goal: 10 countries by end of 2026!**

---

## 🤝 How to Contribute

We welcome contributions from the global community! This repository is designed to be **collaborative and scalable**.

### Quick Contribution Guide

1. **Fork the repository**
2. **Create a branch** (`git checkout -b feature/new-country`)
3. **Follow the structure** based on Brazil/USA/Japan templates
4. **All files in English** (primary language requirement)
5. **Open a Pull Request** with detailed description

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions.

### Adding a New Country (Copy Template)
```bash
cp -r templates/new-country germany
cd germany
# Edit all YAML files following Brazil/USA/Japan examples
git add germany/
git commit -m "Germany IN PROGRESS (8 files created)"
git push origin feature/germany
```

---

## 🔗 Integration Examples

### For Paperclip AI Companies
```bash
# Add country data to your agent company
npx companies.sh add Aceleratrix/global-countries-data --country brazil
```

### For Hermes Agent
```yaml
# In your Hermes skill or agent config:
context_sources:
  - path: "global-countries-data/brazil/fiscal/tax-codes.yaml"
    description: "Brazil tax codes for invoice generation"
  - path: "global-countries-data/brazil/financial/payment-apis.yaml"
    description: "PIX and Brazilian payment methods"
```

### For OpenClaw Agents
```python
# OpenClaw skill loading country data
from openclaw import Skill

class BrazilTaxSkill(Skill):
    def load_data(self):
        import yaml
        with open('global-countries-data/brazil/fiscal/tax-codes.yaml') as f:
            return yaml.safe_load(f)
```

---

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 🔗 Useful Links

- **Repository**: https://github.com/Aceleratrix/global-countries-data
- **Issues**: https://github.com/Aceleratrix/global-countries-data/issues
- **Discussions**: https://github.com/Aceleratrix/global-countries-data/discussions
- **Inspiration**: https://github.com/paperclipai/companies

---

## 🎯 Vision

> *"To be the world's most complete and reliable data repository, enabling any AI system to operate in any country with full understanding of regional nuances."*

---

**Created by**: [@mtorresbr](https://github.com/mtorresbr)  
**Organization**: [Aceleratrix](https://github.com/Aceleratrix)  
**Last Updated**: 2026-04-30  
**Status**: 🚧 Constantly expanding (3 countries 100% complete, many more coming!)

---

### 🖼️ Visual Assets

Check `assets/prompts/README-images.md` for professional image generation prompts (hero banner, architecture diagrams, coverage maps, integration visualizations).

**Pro tip**: Use these prompts with Midjourney, DALL-E 3, or Stable Diffusion to create stunning visuals for your agent company's documentation!
