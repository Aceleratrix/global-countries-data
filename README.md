# 🌍 Global Countries Data

> **A base de dados mais completa do planeta para sistemas de IA multi-agente operarem em qualquer país.**

[![GitHub stars](https://img.shields.io/github/stars/mtorresbr/global-countries-data?style=social)](https://github.com/mtorresbr/global-countries-data)
[![GitHub forks](https://img.shields.io/github/forks/mtorresbr/global-countries-data?style=social)](https://github.com/mtorresbr/global-countries-data)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/mtorresbr/global-countries-data/blob/main/LICENSE)
[![Status: 3 Countries 100% Complete](https://img.shields.io/badge/Status-3 Countries 100% Complete-green)](https://github.com/mtorresbr/global-countries-data)

---

## 🎯 Objetivo

Criar **o maior repositório do planeta** com dados estruturados de todos os países, permitindo que modelos de IA e sistemas multi-agente:

- ✅ Operem de forma **regionalizada** respeitando leis locais (LGPD, GDPR, APPI, etc.)
- ✅ Integrem sistemas de pagamento locais (PIX, Konbini, ACH, SEPA, etc.)
- ✅ Compreendam infraestrutura tecnológica (AWS/GCP/Azure regions, fibra óptica, 5G)
- ✅ Naveguem por requisitos legais (trabalhista, fiscal, importação/exportação)
- ✅ Personalizem experiências baseadas em demografia e cultura local

---

## 📊 Progresso Global

### 🌎 Países 100% Completos (3/195 = 1.5%)

| País | Arquivos | Status | Destaque | Idioma Primário |
|-------|----------|--------|----------|-----------------|
| 🇧🇷 **Brazil** | 17/17 | ✅ **100% COMPLETO** | PIX (76% adoção), LGPD, 5º maior da América Latina | Português (pt-BR) + Inglês |
| 🇺🇸 **USA** | 13/13 | ✅ **100% COMPLETO** | Silicon Valley, Section 230, 20+ cloud regions | Inglês (en-US) |
| 🇯🇵 **Japan** | 14/14 | ✅ **100% COMPLETO** | Konbini (25% e-commerce!), LINE (95%), Society 5.0 | Inglês (en-US) |

**Total: 44 arquivos YAML estruturados!**

---

## 🚀 Quick Start (Para Agentes de IA)

```yaml
# Exemplo: Verificar formato de telefone nos EUA
cat usa/telecom/phone-formats.yaml

# Exemplo: Verificar leis de privacidade no Japão
cat japan/legal/internet-law.yaml

# Exemplo: Ver métodos de pagamento no Brasil
cat brazil/financial/payment-apis.yaml
```

---

## 📁 Estrutura do Repositório

```
global-countries-data/
├── brazil/          # 🇧🇷 100% COMPLETO (17 arquivos)
│   ├── COUNTRY.md
│   ├── README.md    # Documentação 100% completa
│   ├── fiscal/
│   ├── financial/
│   ├── telecom/
│   ├── demographics/
│   ├── business/
│   ├── legal/
│   ├── tech/
│   └── marketing/
│
├── usa/             # 🇺🇸 100% COMPLETO (13 arquivos)
│   ├── COUNTRY.md
│   ├── README.md    # Documentação 100% completa
│   └── ... (mesma estrutura do Brazil)
│
├── japan/           # 🇯🇵 100% COMPLETO (14 arquivos)
│   ├── COUNTRY.md
│   ├── README.md    # Documentação 100% completa
│   └── ... (mesma estrutura do Brazil)
│
└── (próximos países em breve...)
```

---

## 🎉 Destaques Exclusivos (AI First)

### 🇧🇷 Brazil
- **PIX Obrigatório** - 76% adoção, 24/7, gratuito para lojistas
- **LGPD Completa** - Multas até R$ 50M, DPO obrigatório
- **4 Cloud Regions** - AWS (2011), GCP (2017), Azure (2014), Oracle (2021)
- **13.000 Startups** - 17 unicórnios, 5º maior da América Latina

### 🇺🇸 USA (Silicon Valley Focus)
- **Section 230** - Imunidade para plataformas de internet
- **20+ Cloud Regions** - AWS, GCP, Azure, Oracle
- **At-Will Employment** - Pode demitir a qualquer momento
- **Maior ecossistema de VC** - $89B (2025)

### 🇯🇵 Japan (Tokyo Tech Hub)
- **Konbini Payments** - 25% e-commerce em 56.000 lojas! ÚNICO NO MUNDO!
- **LINE** - 95% penetração (WhatsApp japonês com pagamentos!)
- **Society 5.0** - $2B investimento governamental em IA
- **Non-competes NÃO executáveis** - Pode ir para concorrentes!
- **Sem Horário de Verão** - UTC+9 sempre!

---

## 🤖 Para Agentes de IA e Sistemas Multi-Agente

Este repositório foi desenhado para ser consumido por:

- **LLMs** (GPT-4, Claude, Gemini) - Leitura direta de YAML
- **Agentes Autônomos** - Navegação estruturada por país
- **Multi-Agent Systems** - Dados padronizados para coordenação global
- **RAG Systems** - Base de conhecimento para Q&A regionalizado

### Exemplo de Query para Agentes:
```
"Como configurar pagamentos para uma empresa AI First no Japão?"
→ Ler japan/financial/banks.yaml + japan/marketing/digital-marketing.yaml
→ Resposta: Konbini (25%), LINE Pay (60M usuários), Suica/Pasmo
```

---

## 🌍 Próximos Países (Roadmap)

| País | Prioridade | Motivo |
|------|------------|--------|
| 🇩🇪 Germany | Alta | Maior economia da Europa, GDPR, SEPA |
| 🇬🇧 UK | Alta | Hub financeiro, Brexit, Open Banking |
| 🇮🇳 India | Alta | 1.4B pessoas, UPI, tech hub |
| 🇨🇳 China | Média | Maior população, Alipay/WeChat, Great Firewall |
| 🇫🇷 France | Média | GDPR origin, segunda maior economia UE |
| 🇦🇺 Australia | Média | APAC hub, proximity to Japan |
| 🇸🇬 Singapore | Baixa | Hub financeiro asiático, muito pequeno |
| 🇰🇷 South Korea | Baixa | K-pop, tech avançada, 5G líder |

**Meta: 10 países até fim de 2026!**

---

## 🛠️ Como Contribuir

1. **Fork o repositório**
2. **Crie um branch** (`git checkout -b feature/novo-pais`)
3. **Siga a estrutura** baseada no Brazil/USA/Japan
4. **Todos os arquivos em Inglês** (idioma primário)
5. **Abra um Pull Request** com descrição detalhada

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para instruções detalhadas (em breve).

---

## 📜 Licença

Este projeto está licenciado sob a **MIT License** - veja [LICENSE](LICENSE) para detalhes.

---

## 🔗 Links Úteis

- **Repositório**: https://github.com/mtorresbr/global-countries-data
- **Issues**: https://github.com/mtorresbr/global-countries-data/issues
- **Discussions**: https://github.com/mtorresbr/global-countries-data/discussions
- **Inspiration**: https://github.com/paperclipai/companies

---

## 🎯 Visão

> "Ser a base de dados mais completa e confiável do planeta, permitindo que qualquer sistema de IA opere em qualquer país com total compreensão das nuances regionais."

---

**Criado por**: [@mtorresbr](https://github.com/mtorresbr)  
**Última Atualização**: 2026-04-30  
**Status**: 🚧 Em constante expansão (3 países 100% completos, muitos outros por vir!)