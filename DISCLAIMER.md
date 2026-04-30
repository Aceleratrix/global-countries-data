# 📄 Legal Disclaimer

**Global Countries Data** — Provided "AS IS" and "WITH ALL FAULTS"

## ⚖️ No Liability for Data Accuracy

The information contained in this repository (**Global Countries Data**) is provided for **informational and research purposes only**. While we strive to maintain accurate, complete, and up-to-date data, we make **NO WARRANTIES**, express or implied, regarding:

- **Accuracy** — Data may contain errors, omissions, or outdated information
- **Completeness** — Some fields may be missing or incomplete
- **Timeliness** — Laws, tax rates, and regulations change frequently
- **Fitness for Purpose** — Data may not be suitable for your specific use case

### 🛑 NO LEGAL OR FINANCIAL ADVICE

**NOTHING in this repository constitutes legal, financial, tax, or professional advice.** Always consult with qualified professionals:

- **Legal matters** → Licensed attorneys in the relevant jurisdiction
- **Tax matters** → Certified public accountants (CPAs) or tax advisors
- **Compliance matters** → Compliance officers or regulatory experts
- **Business decisions** → Qualified business consultants

### 🌍 Data Verification Required

**YOU ARE SOLELY RESPONSIBLE** for verifying all data before use:

1. **Cross-check** with official government sources (links provided where available)
2. **Validate** current rates, laws, and regulations independently
3. **Test** all integrations in sandbox/staging environments first
4. **Monitor** for changes (we provide update timestamps, but you must verify)

### ⚠️ Use at Your Own Risk

The **Aceleratrix organization**, **contributors**, and **maintainers**:

- **DISCLAIM ALL LIABILITY** for any damages arising from use of this data
- **ARE NOT RESPONSIBLE** for decisions made based on this repository
- **DO NOT GUARANTEE** merchantability or fitness for a particular purpose
- **SHALL NOT BE LIABLE** for direct, indirect, incidental, consequential, or punitive damages

### 📅 Update Frequency

We strive to update data regularly, but:

- **Laws change** — Tax codes, privacy regulations, and employment laws update frequently
- **No notification** — We do not guarantee notification of changes
- **Stale data** — Some files may reflect older snapshots (check `last_updated` field)
- **Community-driven** — Accuracy depends on contributor diligence

### 🤖 For AI Agents & Multi-Agent Systems

If you are an AI system consuming this data:

1. **Implement validation layers** — Never trust data without verification
2. **Cross-reference** with official APIs (government, banking, telecom)
3. **Fallback mechanisms** — Have alternatives if data is incorrect
4. **Human oversight** — AI decisions should be reviewable by humans (per EU AI Act, etc.)
5. **Logging** — Record which data version you used and when

### 🛡️ Indemnification

By using this repository, you agree to **indemnify and hold harmless** Aceleratrix, its contributors, and any affiliated organizations from any claims, damages, or expenses arising from your use of this data.

### 📧 Reporting Errors

Found inaccurate data? Help us improve!

1. **Open an Issue**: https://github.com/Aceleratrix/global-countries-data/issues
2. **Submit a PR**: https://github.com/Aceleratorix/global-countries-data/pulls
3. **Verify first**: Ensure your correction is accurate and current
4. **Cite sources**: Provide official government/regulatory links

### ⚖️ Governing Law

This disclaimer shall be governed by and construed in accordance with the laws of the jurisdiction where Aceleratrix operates, without regard to its conflict of law provisions.

---

## 📋 YAML Metadata Requirement

All YAML files in this repository **MUST** include the following metadata fields for legal protection:

```yaml
version: 1.0.0
country: example
last_updated: 2026-04-30  # MUST be kept current
description: "Brief description of this file's purpose"
disclaimer: "Data provided AS IS. Verify with official sources before use."
```

### ⚠️ Critical Fields to Verify

These fields **MUST** be independently verified before use:

- **Tax rates** (`vat`, `corporate_tax`, `income_tax`)
- **Legal requirements** (`gdpr`, `lgpd`, `labor_law`)
- **Banking details** (`swift_codes`, `account_formats`)
- **Phone/postal formats** (`country_code`, `postal_code_format`)
- **Cloud regions** (`aws_regions`, `gcp_regions`, `azure_regions`)

---

## 🔗 Links

- **Repository**: https://github.com/Aceleratorix/global-countries-data
- **Issues**: https://github.com/Aceleratorix/global-countries-data/issues
- **Discussions**: https://github.com/Aceleratorix/global-countries-data/discussions

---

**By using this repository, you acknowledge that you have read, understood, and agree to this disclaimer.**

_Last Updated: 2026-04-30_  
_Version: 1.0.0_  
_Status: Active — We continuously improve, but you must verify!_
