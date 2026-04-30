# 🌍 Global Countries Data

> **A base de dados mais completa do planeta para sistemas de IA multi-agente operarem em qualquer país.**

[![GitHub stars](https://img.shields.io/github/stars/mtorresbr/global-countries-data?style=social)](https://github.com/mtorresbr/global-countries-data)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Countries](https://img.shields.io/badge/Countries-3+-blue)](https://github.com/mtorresbr/global-countries-data)
[![Completeness](https://img.shields.io/badge/Data_Completeness-In%20Progress-yellow)](https://github.com/mtorresbr/global-countries-data)

## 🚀 O Que É Isto?

Um repositório open-source estruturado de dados regionais para que **sistemas de IA possam criar empresas "AI First" que entendam nuances locais**.

Cada país possui dados detalhados sobre:
- **Fiscal:** Impostos, códigos fiscais, notas fiscais eletrônicas
- **Telecom:** Formatos de telefone, CEP, padrões de endereço
- **Legal:** Tipos de empresa, requisitos de registro, compliance
- **Financeiro:** Moeda, bancos, métodos de pagamento (PIX, SEPA, etc.)
- **Demográfico:** População, idiomas, fusos horários
- **Empresarial:** Portes, setores, horários comerciais

## 📊 Países Disponíveis

| País | ISO | Moeda | Idioma | Completude | Dados |
|------|-----|-------|--------|-----------|-------|
| [Brasil](#brazil) | BR | BRL | pt-BR | Em progresso | [Ver](brazil/) |
| [EUA](#usa) | US | USD | en-US | Em breve | [Ver](usa/) |
| [Japão](#japan) | JP | JPY | ja-JP | Em breve | [Ver](japan/) |

## 🤖 Como Usar (Para Sistemas de IA)

### Python
```python
import yaml
import json

# Carregar dados do Brasil
with open('brazil/fiscal/tax-codes.yaml') as f:
    tax_data = yaml.safe_load(f)

# Usar em seu sistema multi-agente
print(tax_data['taxes'][0]['name'])  # "ICMS"
```

### Consumo via API (Futuro)
```bash
curl https://api.global-countries.dev/v1/brazil/fiscal
```

## 📈 Impacto

Este repositório permite que:
- Sistemas de IA criem empresas que **respeitem leis locais**
- Agentes multi-agent entendam **formatos regionais** (telefone, CEP)
- Empresas "AI First" operem com **pagamentos locais** (PIX, SEPA, etc.)
- Reduza erros de compliance em **sistemas automatizados**

## 🏗️ Estrutura do Repositório

```
global-countries-data/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── schemas/              # JSON Schemas para validação
├── templates/            # Templates para novos países
├── scripts/              # Scripts de validação
├── brazil/               # Dados do Brasil
├── usa/                  # Dados dos EUA
└── japan/                # Dados do Japão
```

## 🤝 Contribua

Todo mundo é bem-vindo! Adicione seu país, melhore dados existentes, ou crie schemas novos.
Leia o [CONTRIBUTING.md](CONTRIBUTING.md) para começar.

## 📜 Licença

MIT - Use livremente em seus projetos comerciais ou open-source.

**Construído com ❤️ pela comunidade open-source para o futuro da IA regionalizada.**
