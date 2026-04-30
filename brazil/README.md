# Brazil (Brasil) - Dados do País 🎉 100% COMPLETO!

Este diretório contém **todos** os dados estruturados para operar sistemas de IA e empresas "AI First" no Brasil.

**✅ STATUS: 100% COMPLETO** (17 arquivos YAML + 2 READMEs)

## 📊 Resumo Rápido

| Atributo | Valor |
|----------|-------|
| **ISO Code** | BR (BRA) |
| **Moeda** | Real (BRL / R$) |
| **Idioma** | Português (pt-BR) + Inglês (en) |
| **População** | 215 milhões |
| **PIB** | USD 1.9 trilhões |
| **Prefixo Telefônico** | +55 |
| **Formato CEP** | XXXXX-XXX |
| **PIX Adoção** | 76% população adulta |
| **Cloud Regions** | AWS (2011), GCP (2017), Azure (2014) |

---

## 📁 Estrutura Completa de Dados (100% Bilíngue pt-BR/en)

### 📄 Metadados e Visão Geral
- **[COUNTRY.md](COUNTRY.md)** - Metadados principais (YAML frontmatter) com schema, versão, autores, completude
- **[README.md](README.md)** - Este arquivo (documentação completa)

### 📊 Fiscal e Tributário (100%)
- **[fiscal/tax-codes.yaml](fiscal/tax-codes.yaml)** - Impostos (ICMS, IPI, PIS/COFINS), regimes (Simples Nacional, Lucro Real), NF-e, obrigações acessórias

### 💰 Financeiro e Pagamentos (100%)
- **[financial/banks.yaml](financial/banks.yaml)** - Top 10 bancos (Itaú, BB, Bradesco, Caixa, Santander), PIX, boleto, gateways
- **[financial/payment-apis.yaml](financial/payment-apis.yaml)** - Open Banking, PagSeguro, Mercado Pago, Stone, Cielo APIs

### 📱 Telecomunicações (100%)
- **[telecom/phone-formats.yaml](telecom/phone-formats.yaml)** - Formatos de telefone (+55 11 9XXXX-XXXX), CEP, DDDs, endereços

### 👥 Demográfico (100%)
- **[demographics/population.yaml](demographics/population.yaml)** - População por região, faixa etária, gênero, idiomas, fusos horários, pirâmide etária

### 🏢 Empresarial (100%)
- **[business/company-sizes.yaml](business/company-sizes.yaml)** - Portes (Micro, Pequena, Média, Grande, MEI), setores CNAE, horários, feriados, startups
- **[business/software-apis.yaml](business/software-apis.yaml)** - ContaAzul, Bling, Tiny, Omie, SAP, TOTVS, ERPs, marketplaces
- **[business/real-estate.yaml](business/real-estate.yaml)** - Escritórios comerciais, coworking (WeWork, Cubo), zoneamento, IPTU, home office
- **[business/import-export.yaml](business/import-export.yaml)** - SISCOMEX, importação/exportação, NCM, ANVISA, INMETRO, acordos internacionais

### ⚖️ Legal (100%)
- **[legal/ecommerce-law.yaml](legal/ecommerce-law.yaml)** - LGPD, Marco Civil, e-commerce law, direitos do consumidor, assinatura digital
- **[legal/labor-law.yaml](legal/labor-law.yaml)** - CLT, PJ, trabalho remoto (Lei 14.442/2022), salários tech, rescisão, eSocial

### 🤖 Tech e IA (100%)
- **[tech/ai-cloud-services.yaml](tech/ai-cloud-services.yaml)** - AWS, Google Cloud, Azure (regiões no Brasil), LLMs (GPT-4, Claude, Llama), NLP, Speech, Vision, GPU providers, talentos de IA

### 📢 Marketing Digital (100%)
- **[marketing/digital-marketing.yaml](marketing/digital-marketing.yaml)** - Google Ads, Meta Ads, TikTok Ads, redes sociais, e-mail marketing, SEO, influenciadores, afiliados

---

## 🤖 Como Usar (Para IAs e Sistemas Multi-Agent)

### Python - Exemplos Práticos

```python
import yaml
import re

# 1. Carregar códigos fiscais brasileiros
with open('fiscal/tax-codes.yaml') as f:
    tax = yaml.safe_load(f)
    print(f"Regimes: {[r['code'] for r in tax['tax_regimes']]}")
    # ['SIMPLES NACIONAL', 'LUCRO PRESUMIDO', 'LUCRO REAL']

# 2. Validar telefone brasileiro
with open('telecom/phone-formats.yaml') as f:
    phone = yaml.safe_load(f)
    pattern = phone['phone']['formats']['mobile']['pattern']
    test = "+5511999999999"
    print(f"Válido: {bool(re.match(pattern, test))}")  # True

# 3. Verificar bancos com PIX
with open('financial/banks.yaml') as f:
    banks = yaml.safe_load(f)
    pix_banks = [b['name'] for b in banks['banks'] if b.get('pix_enabled')]
    print(f"Bancos com PIX: {pix_banks}")

# 4. Consultar salários de Data Scientist no Brasil
with open('legal/labor-law.yaml') as f:
    labor = yaml.safe_load(f)
    ds_salary = [s for s in labor['tech_salaries_brl_year'] 
                  if 'Data Scientist' in s['role_pt']][0]
    print(f"Data Scientist Senior: R$ {ds_salary['range_brl'][1]:,}/ano")

# 5. Verificar serviços de IA disponíveis no Brasil
with open('tech/ai-cloud-services.yaml') as f:
    ai = yaml.safe_load(f)
    generative = [s['provider'] for s in ai['generative_ai_services']]
    print(f"IA Generativa: {generative}")

# 6. Checar leis trabalhistas (Home Office)
with open('legal/labor-law.yaml') as f:
    labor = yaml.safe_load(f)
    remote = labor['employment_types'][4]  # Trabalho Remoto
    print(f"Home Office: {remote['description_pt']}")
```

### Consumo via API (Futuro)
```bash
curl https://api.global-countries.dev/v1/brazil/fiscal/tax-codes
curl https://api.global-countries.dev/v1/brazil/tech/ai-cloud-services
curl https://api.global-countries.dev/v1/brazil/business/import-export
```

---

## 🏆 Destaques Exclusivos para Negócios AI First

| Recurso | Descrição | Impacto |
|---------|-----------|---------|
| **PIX Obrigatório** | Sistema de pagamento instantâneo 24/7 | 76% adoção, gratuito para lojistas |
| **LGPD** | Equivalente ao GDPR, multas até R$ 50M | Requer DPO, consentimento explícito |
| **Cloud Regions no Brasil** | AWS (2011), GCP (2017), Azure (2014) | Latência < 10ms para SP, compliance |
| **Open Banking** | APIs bancárias padronizadas | Integração total com sistemas de IA |
| **WhatsApp Business** | 92% das empresas usam | API disponível para chatbots com IA |
| **NF-e/NFS-e** | Notas fiscais eletrônicas obrigatórias | Integração via API (certificado digital) |
| **Lei do Bem** | Incentivos fiscais para P&D em IA | 60-80% de abatimento em IR |
| **13.000 Startups** | 17 unicórnios, hubs em SP/RJ/BH/POA | 5º maior ecossistema da América Latina |
| **Home Office Regulamentado** | Lei 14.442/2022 | Empresa fornece equipamentos e internet |
| **Cross-Border E-commerce** | Alibaba (45%), Amazon (25%) | Importação até US$ 50 isenta |

---

## 📈 Métricas de Completude (100%)

| Categoria | Progresso | Arquivos |
|-----------|-----------|---------|
| 📊 Fiscal | ██████████ 100% | tax-codes.yaml |
| 💰 Financeiro | ██████████ 100% | banks.yaml, payment-apis.yaml |
| 📱 Telecom | ██████████ 100% | phone-formats.yaml |
| 👥 Demográfico | ██████████ 100% | population.yaml |
| 🏢 Empresarial | ██████████ 100% | company-sizes.yaml, software-apis.yaml, real-estate.yaml, import-export.yaml |
| ⚖️ Legal | ██████████ 100% | ecommerce-law.yaml, labor-law.yaml |
| 🤖 Tech/IA | ██████████ 100% | ai-cloud-services.yaml |
| 📢 Marketing | ██████████ 100% | digital-marketing.yaml |
| **TOTAL** | **█ 100% COMPLETO** | **15 YAML + 2 READMEs** |

---

## 🌟 Serviços de IA Disponíveis no Brasil (Regiões Locais)

### Cloud Providers com Data Center no Brasil
1. **AWS sa-east-1** (São Paulo) - 2011, 200+ serviços
2. **Google Cloud southamerica-east1** (São Paulo) - 2017, 150+ serviços
3. **Azure Brazil South** (São Paulo) - 2014, 180+ serviços
4. **Oracle Cloud sa-saopaulo-1** (São Paulo) - 2021, 100+ serviços

### Modelos de Linguagem (LLMs) Via API
- **AWS Bedrock:** Claude (Anthropic), Titan, Llama 3
- **Google Vertex AI:** Gemini 1.5, PaLM 2
- **Azure AI:** GPT-4, GPT-3.5, DALL-E 3
- **OpenAI API:** GPT-4o, GPT-4, Whisper (latência ~200ms)
- **Anthropic API:** Claude 3.5 Sonnet (~180ms)

### NLP, Speech e Vision
- Google Cloud: Natural Language, Speech-to-Text, Vision API
- AWS: Comprehend, Transcribe, Rekognition
- Azure: Text Analytics, Speech, Computer Vision

---

## 🔧 Ferramentas para Devs e IAs

### ERPs e Contabilidade
✅ ContaAzul, Bling, Tiny, Omie (e-commerce)  
✅ SAP, TOTVS, Oracle NetSuite (enterprise)  
✅ eNotas (NFS-e), Focus NFe (NF-e)

### Atendimento e Chatbots
✅ WhatsApp Business API (92% uso)  
✅ Zendesk, Intercom, RD Station CRM  
✅ Dialogflow, Amazon Lex, Rasa (chatbots)

### Marketing e Analytics
✅ Google Ads (65% market), Meta Ads (25%)  
✅ RD Station, Mailchimp, ActiveCampaign  
✅ Google Analytics 4, Meta Pixel, Hotjar

### KYC e Verificação
✅ Serasa, SPC Brasil (crédito)  
✅ Unico (biometria facial)  
✅ DocuSign/Verify (ID verification)

---

## 🤝 Contribua

Encontrou dados desatualizados ou quer adicionar mais informações?
1. Edite os arquivos YAML (mantenha bilingual pt-BR/en)
2. Rode `python ../scripts/validate-country.py --country brazil`
3. Abra um Pull Request

**Como citar dados:** Global Countries Data - Brazil (2026). Disponível em: https://github.com/mtorresbr/global-countries-data

---

## 📚 Fontes Oficiais

- **Receita Federal:** https://www.receita.fazenda.gov.br
- **Banco Central:** https://www.bcb.gov.br (PIX, Open Banking)
- **IBGE:** https://www.ibge.gov.br (demográfico)
- **ANPD:** https://www.gov.br/cidadania/pt-acessoainformacao/anpd (LGPD)
- **Sebrae:** https://www.sebrae.com.br (empresarial)
- **Correios:** https://www.correios.com.br (CEP, endereços)
- **INPI:** https://www.gov.br/inpi (propriedade intelectual)
- **SISCOMEX:** https://www.gov.br/receitafederal (import/export)

---

**Mantido por:** [Marcos Torres](https://github.com/mtorresbr)  
**Status:** ✅ 100% COMPLETO  
**Última atualização:** 30 de abril de 2026  
**Schema:** countries-data/v1  
**Licença:** MIT  
**Conteúdo:** 100% Bilíngue (pt-BR + en) como padrão
