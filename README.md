# 🌍 Global Countries Data

> **A base de dados mais completa do planeta para sistemas de IA multi-agente operarem em qualquer país.**

[![GitHub stars](https://img.shields.io/github/stars/mtorresbr/global-countries-data?style=social)](https://github.com/mtorresbr/global-countries-data)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Countries](https://img.shields.io/badge/Countries-3+-blue)](https://github.com/mtorresbr/global-countries-data)
[![Brazil Status](https://img.shields.io/badge/Brazil-100%25%20COMPLETE-brightgreen)](https://github.com/mtorresbr/global-countries-data/brazil/)
[![AI First](https://img.shields.io/badge/Focus-AI%20First-blueviolet)](https://github.com/mtorresbr/global-countries-data)
[![Bilingual](https://img.shields.io/badge/Languages-pt--BR%20+%20en-orange)](https://github.com/mtorresbr/global-countries-data)

## 🚀 O Que É Isto?

Um repositório open-source estruturado de dados regionais para que **sistemas de IA possam criar empresas "AI First" que entendam nuances locais**.

Cada país possui dados detalhados sobre:

### 📊 Dados Básicos
- **Fiscal:** Impostos (ICMS, IPI, PIS/COFINS), regimes tributários, NF-e/NFS-e
- **Telecom:** Formatos de telefone, CEP, padrões de endereço, DDDs
- **Legal:** Tipos de empresa, LGPD, Marco Civil, e-commerce law, compliance
- **Financeiro:** Moeda, bancos (Top 10+), métodos de pagamento (PIX, Boleto), gateways
- **Demográfico:** População, idiomas, fusos horários, pirâmide etária
- **Empresarial:** Portes (ME, EPP, Média, Grande, MEI), setores CNAE, horários

### 🤖 Específico para AI First / Negócios 100% Online
- **APIs de Pagamento:** Open Banking, PagSeguro, Mercado Pago, Stone, Cielo
- **Serviços de IA:** AWS Bedrock, Google Vertex AI, Azure AI, OpenAI, Anthropic
- **Cloud Computing:** Regiões no Brasil (AWS sa-east-1, GCP southamerica-east1, Azure Brazil South)
- **Marketing Digital:** Google Ads, Meta Ads, TikTok Ads, influenciadores, afiliados
- **Softwares de Gestão:** ContaAzul, Bling, Tiny, VTEX, Omie, ERPs (SAP, TOTVS)
- **E-commerce:** Marketplaces (Mercado Livre, Amazon, Magalu), Shopify, WooCommerce
- **Atendimento:** WhatsApp Business API, Zendesk, Intercom, RD Station, chatbots
- **KYC/Identity:** Serasa, SPC, DocuSign, Unico, verificação de documentos
- **Fiscal/Contábil:** Focus NFe, eNotas, ContaAzul API, Bling API
- **Assinatura Digital:** Clicksign, DocuSign, certificados ICP-Brasil
- **Trabalho/Legal:** CLT, PJ, trabalho remoto (Lei 14.442/2022), salários tech
- **Imóveis:** Escritórios comerciais, coworking, zoneamento, IPTU
- **Import/Export:** SISCOMEX, NCM, ANVISA, INMETRO, acordos internacionais

## 📊 Países Disponíveis

| País | ISO | Moeda | Idioma | Completude | AI/Cloud | Dados |
|------|-----|-------|--------|-----------|---------|-------|
| [Brasil 🇧🇷](#brazil) | BR | BRL | pt-BR / en | **100% ✅** | 15+ serviços | [Ver](brazil/) |
| [EUA 🇺🇸](#usa) | US | USD | en-US | Em breve | Em breve | [Ver](usa/) |
| [Japão 🇯🇵](#japan) | JP | JPY | ja-JP / en | Em breve | Em breve | [Ver](japan/) |

## 🤖 Como Usar (Para Sistemas de IA)

### Python
```python
import yaml

# Carregar códigos fiscais brasileiros
with open('brazil/fiscal/tax-codes.yaml') as f:
    tax_data = yaml.safe_load(f)
    print(tax_data['tax_regimes'][0]['code'])  # "SIMPLES NACIONAL"

# Validar formato de telefone brasileiro
import re
with open('brazil/telecom/phone-formats.yaml') as f:
    phone = yaml.safe_load(f)
    pattern = phone['phone']['formats']['mobile']['pattern']
    print(bool(re.match(pattern, "+5511999999999")))  # True

# Listar serviços de IA disponíveis no Brasil
with open('brazil/tech/ai-cloud-services.yaml') as f:
    ai = yaml.safe_load(f)
    models = [m['models_pt'] for m in ai['generative_ai_services']]

# Consultar salários de Data Scientist no Brasil
with open('brazil/legal/labor-law.yaml') as f:
    labor = yaml.safe_load(f)
    ds = [s for s in labor['tech_salaries_brl_year'] 
           if 'Data Scientist' in s['role_pt']][0]
    print(f"Data Scientist Senior: R$ {ds['range_brl'][1]:,}/ano")
```

### Consumo via API (Futuro)
```bash
curl https://api.global-countries.dev/v1/brazil/fiscal/tax-codes
curl https://api.global-countries.dev/v1/brazil/tech/ai-cloud-services
curl https://api.global-countries.dev/v1/brazil/business/import-export
```

## 📈 Impacto para Negócios AI First

Este repositório permite que:
- ✅ Sistemas de IA criem empresas que **respeitem leis locais** (LGPD, Marco Civil)
- ✅ Agentes multi-agent entendam **formatos regionais** (telefone +55, CEP)
- ✅ Empresas "AI First" operem com **pagamentos locais** (PIX obrigatório)
- ✅ Automação use **APIs locais** (Open Banking, NF-e, WhatsApp Business)
- ✅ Chatbots falem a **língua local** (pt-BR) com suporte nativo
- ✅ Integração com **ecossistema local** (marketplaces, ERPs, gateways)
- ✅ Contratação de **talentos locais** (salários, CLT, PJ, trabalho remoto)
- ✅ Importação/exportação **conforme regulamentação** (SISCOMEX, NCM)

## 🏗️ Estrutura do Repositório (Brasil como Exemplo)

```
global-countries-data/
├── README.md                          # Este arquivo
├── CONTRIBUTING.md                    # Diretrizes para contribuição
├── LICENSE                            # MIT License
├── schemas/                           # JSON Schemas para validação
│   └── country-metadata.json
├── templates/                         # Templates para novos países
│   └── COUNTRY.md.template
├── scripts/                           # Scripts de validação
│   └── validate-country.py
│
├── brazil/                            # 🇧🇷 Dados do Brasil (100% COMPLETO)
│   ├── COUNTRY.md                     # Metadados (YAML frontmatter)
│   ├── README.md                      # Documentação específica (100% COMPLETO)
│   ├── fiscal/                        # 📊 Fiscal
│   │   └── tax-codes.yaml             # Impostos, regimes, NF-e
│   ├── financial/                      # 💰 Financeiro
│   │   ├── banks.yaml                 # Bancos, PIX, pagamentos
│   │   └── payment-apis.yaml          # Open Banking, gateways
│   ├── telecom/                        # 📱 Telecom
│   │   └── phone-formats.yaml         # Telefone, CEP, endereços
│   ├── demographics/                   # 👥 Demográfico
│   │   └── population.yaml            # População, idiomas, fusos
│   ├── business/                       # 🏢 Empresarial
│   │   ├── company-sizes.yaml         # Portes, CNAE, horários
│   │   ├── software-apis.yaml        # ERPs, e-commerce, CRM
│   │   ├── real-estate.yaml          # Escritórios, coworking, zoneamento
│   │   └── import-export.yaml        # SISCOMEX, importação, exportação
│   ├── legal/                          # ⚖️ Legal
│   │   ├── ecommerce-law.yaml         # LGPD, Marco Civil, e-commerce
│   │   └── labor-law.yaml            # CLT, PJ, trabalho remoto, salários
│   ├── tech/                           # 🤖 Tech & IA
│   │   └── ai-cloud-services.yaml     # AWS, GCP, Azure, LLMs
│   └── marketing/                      # 📢 Marketing
│       └── digital-marketing.yaml     # Google Ads, Meta, influenciadores
│
├── usa/                               # 🇺🇸 EUA (em breve)
└── japan/                            # 🇯🇵 Japão (em breve)
```

## 🌟 Destaques do Brasil (País Piloto - 100% COMPLETO!)

### 🏆 Maior Ecossistema de Pagamentos Instantâneos
- **PIX:** Sistema obrigatório, 76% da população adulta, 24/7
- **Open Banking:** APIs padronizadas de todos os bancos principais
- **Gateways:** PagSeguro, Mercado Pago, Stone, Cielo

### 🤖 Cloud Regions para IA
- **AWS sa-east-1** (São Paulo) - 2011, 200+ serviços
- **Google Cloud southamerica-east1** (São Paulo) - 2017, 150+ serviços
- **Azure Brazil South** (São Paulo) - 2014, 180+ serviços
- **Oracle Cloud sa-saopaulo-1** (São Paulo) - 2021, 100+ serviços

### 📱 WhatsApp como Canal de Negócios
- 92% das empresas usam WhatsApp Business
- API disponível para chatbots com IA
- Integração nativa com pagamentos (PIX)

### ⚖️ LGPD (Equivalente ao GDPR)
- Autoridade: ANPD
- Multas até R$ 50 milhões
- Requisitos para IA: consentimento explícito, direito ao esquecimento
- DP (Data Protection Officer) obrigatório

### 🏭 13.000 Startups Ativas
- 17 unicórnios
- 5º maior ecossistema da América Latina
- Hubs: SP, RJ, BH (San Pedro Valley), Recife (Porto Digital)

### 💼 Trabalho e Remuneração
- **Lei do Trabalho Remoto (14.442/2022):** Empresa fornece equipamentos e internet
- **Salários Tech:** Junior R$ 48K-84K/ano, Senior R$ 144K-240K/ano
- **Contratação:** CLT (com direitos) ou PJ (flexível)
- **eSocial:** Folha digital obrigatória para todas as empresas

### 🏢 Imóveis e Infraestrutura
- **Escritórios AAA:** R$ 180-300/m² (Faria Lima, SP)
- **Coworking:** WeWork, Impact Hub, Cubo (R$ 250-1200/pessoa/mês)
- **Galpões Logísticos:** R$ 25-45/m² (Grande SP)

### 🚢 Importação e Exportação
- **SISCOMEX:** Sistema oficial da Receita Federal
- **Impostos:** II (0-35%), IPI (0-15%), PIS/COFINS (9,25%), ICMS (18%)
- **Acordos:** Mercosul, EFTA, UE (em ratificação)
- **Cross-Border E-commerce:** Alibaba (45%), Amazon (25%)

## 🤝 Contribua

Todo mundo é bem-vindo! 
- 🌍 Adicione seu país
- 📊 Melhore dados existentes
- 🤖 Adicione novos serviços de IA
- 📝 Crie schemas novos

**Padrão Obrigatório:** Todo conteúdo deve ser **bilíngue (pt-BR + en)** para garantir que IAs e sistemas multi-agent possam operar em ambos os idiomas.

Leia o [CONTRIBUTING.md](CONTRIBUTING.md) para começar.

## 📜 Licença

MIT - Use livremente em seus projetos comerciais ou open-source.

---

**Construído com ❤️ pela comunidade open-source para o futuro da IA regionalizada.**

**Contato:** [Marcos Torres](https://github.com/mtorresbr)  
**Status do Projeto:** ✅ Brasil 100% COMPLETO | 🚀 Expandindo para outros países  
**Última atualização:** 30 de abril de 2026  
**Total de Arquivos (Brasil):** 15 YAML + 2 READMEs = 17 arquivos  
**Idiomas:** 100% Bilíngue (pt-BR + en) como padrão
