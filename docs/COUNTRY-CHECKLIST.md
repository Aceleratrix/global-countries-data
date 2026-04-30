# 🌍 Country Readiness Checklist

## Definition of "Country Complete" (Ready for AI Agents)

A country is considered **100% COMPLETE** when it has **ALL** the following files with **full data**:

### Mandatory Files (13-17 files per country)

#### 1. **Metadata & Documentation** (2 files)
- [ ] `COUNTRY.md` — Country metadata (YAML frontmatter) + overview
- [ ] `README.md` — Full documentation (100% complete badge, highlights, comparisons)

#### 2. **Legal & Regulatory** (2-3 files)
- [ ] `legal/internet-law.yaml` — Privacy law (GDPR/LGPD/APPI), AI law, platform liability
- [ ] `legal/labor-law.yaml` — Employment types, salaries, unions, benefits
- [ ] `legal/ecommerce-law.yaml` *(if applicable)* — E-commerce regulations

#### 3. **Fiscal & Financial** (2 files)
- [ ] `fiscal/tax-codes.yaml` — VAT/sales tax, corporate tax, R&D credits
- [ ] `financial/banks.yaml` — Banks, payment methods, fintech, cryptocurrencies

#### 4. **Telecom & Demographics** (2 files)
- [ ] `telecom/phone-formats.yaml` — Phone formats, postal codes, ISPs, time zones
- [ ] `demographics/population.yaml` — Population, age, languages, education, internet stats

#### 5. **Business & Company** (3-4 files)
- [ ] `business/company-sizes.yaml` — Company types, sizes, sectors, startup ecosystem
- [ ] `business/software-apis.yaml` — Accounting software, ERP, SaaS, APIs
- [ ] `business/real-estate.yaml` — Office spaces, coworking, tech hubs
- [ ] `business/import-export.yaml` — Trade regulations, customs, authorities

#### 6. **Tech & AI Services** (1 file)
- [ ] `tech/ai-cloud-services.yaml` — Cloud regions, LLM APIs, GPU providers, tech hubs, talent pool

#### 7. **Marketing** (1 file)
- [ ] `marketing/digital-marketing.yaml` — Ad platforms, social media, e-commerce stats

---

## ✅ Completion Criteria

A country is **READY** when:
1. **ALL files above exist** (13-17 YAML files + 2 MD files)
2. **ALL YAML files have** `disclaimer` field (legal protection)
3. **ALL YAML files have** `last_updated` field (freshness tracking)
4. **Data is comprehensive** (covers all fields in templates)
5. **Country README.md** shows ✅ **100% COMPLETE** badge
6. **Comparisons included** (vs Brazil/USA/Japan/Germany)
7. **Integration examples** (Paperclip, OpenClaw, Hermes)
8. **Unique features highlighted** (what makes this country special for AI agents)

---

## 📊 Completion Progress Template

```
| Country | Files | Status | Key Highlights | Primary Language |
|---------|-------|--------|-----------------|-----------------|
| 🇽🇽 Country | X/Y | ✅ **100% COMPLETE** | Unique feature 1, 2, 3 | en-XX |
```

---

## 🎯 Quality Standards

### Data Must Be:
- ✅ **Accurate** — Cross-checked with official sources (links provided)
- ✅ **Current** — `last_updated` within 6 months
- ✅ **Structured** — Follows YAML schema validation
- ✅ **AI-Readable** — No ambiguous fields, clear naming
- ✅ **Legally Protected** — Has `disclaimer` field

### Files Must Have:
```yaml
version: 1.0.0
country: example
last_updated: 2026-04-30
disclaimer: "Data provided AS IS. Verify with official sources before use. See DISCLAIMER.md for full terms."
description: "Brief description of this file's purpose"
```

---

## 🚀 Progress Tracking

### Completed (100%):
- 🇧🇷 Brazil (17/17 files) ✅
- 🇺🇸 USA (13/13 files) ✅
- 🇯🇵 Japan (14/14 files) ✅

### In Progress:
- 🇩🇪 Germany (8/13 files) 🚧

### Pending (by economy size):
See `COUNTRIES-LIST.md` for full prioritized list.

---

**Last Updated**: 2026-04-30  
**Maintainer**: [@mtorresbr](https://github.com/mtorresbr)  
**Organization**: [Aceleratrix](https://github.com/Aceleratrix)
