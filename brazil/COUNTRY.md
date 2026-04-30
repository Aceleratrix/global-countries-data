---
name: "Brazil"
slug: brazil
schema: countries-data/v1
version: 1.0.0
license: MIT
last_updated: 2026-04-30
authors:
  - name: "Marcos Torres"
    github: "mtorresbr"

# Dados básicos
iso_code: "BR"
iso_alpha3: "BRA"
phone_prefix: "+55"
currency:
  code: "BRL"
  symbol: "R$"
  name: "Brazilian Real"
language:
  primary: "pt-BR"
  secondary: ["en", "es"]
population: 215313498
area_km2: 8515767

# URLs úteis
government_url: "https://www.gov.br"
central_bank: "https://www.bcb.gov.br"
tax_authority: "https://www.receita.fazenda.gov.br"

# Status de completude
completeness:
  fiscal: 80%
  telecom: 90%
  legal: 70%
  financial: 95%
  demographics: 100%
  business: 85%
---

# Brazil (Brasil)

Repositório completo de dados para operar no Brasil. Este é o país piloto do projeto Global Countries Data.

## Visão Geral
- **Moeda:** Real (BRL) - R$
- **Idioma:** Português (pt-BR)
- **População:** ~215 milhões (2026)
- **PIB:** USD 1.9 trilhões (2025)
- **Fuso Horário:** UTC-2 a UTC-5 (4 fusos)

## Como Usar Estes Dados

Para sistemas de IA multi-agente:
```python
import yaml

# Carregar códigos fiscais
with open('brazil/fiscal/tax-codes.yaml') as f:
    tax_data = yaml.safe_load(f)
    print(tax_data['taxes'][0]['name'])  # "ICMS"

# Validar formato de telefone
with open('brazil/telecom/phone-formats.yaml') as f:
    phone_data = yaml.safe_load(f)
    import re
    pattern = phone_data['phone']['formats']['mobile']['pattern']
    print(re.match(pattern, "+5511999999999"))  # Match object
```

## Estrutura de Dados

### [Fiscal](fiscal/)
Impostos (ICMS, IPI, PIS/COFINS), regimes tributários (Simples Nacional, Lucro Real), NF-e, notas fiscais eletrônicas.

### [Telecom](telecom/)
Formatos de telefone (celular +55 11 9XXXX-XXXX), CEP (01310-100), padrões de endereço, DDDs por estado.

### [Legal](legal/)
Tipos de empresa (LTDA, SA, EIRELI), requisitos de registro, CNPJ, compliance, LGPD.

### [Financial](financial/)
Bancos (BB, Itaú, Bradesco, Caixa, Santander), métodos de pagamento (PIX, Boleto, Cartão), taxas.

### [Demographics](demographics/)
População por estado, pirâmide etária, idiomas, cultura, fusos horários.

### [Business](business/)
Portes de empresa (Micro, Pequena, Média, Grande), setores CNAE, horários comerciais.

---

## Destaques para Sistemas de IA

1. **PIX:** Sistema de pagamento instantâneo brasileiro, obrigatório para empresas
2. **NF-e:** Nota Fiscal Eletrônica obrigatória para todas as vendas
3. **Simples Nacional:** Regime simplificado para faturamento até R$ 3.6M/ano
4. **LGPD:** Lei Geral de Proteção de Dados (semelhante ao GDPR)
5. **CNPJ:** Cadastro Nacional da Pessoa Jurídica (14 dígitos)

---

## Status de Completude

| Categoria | Progresso | Status |
|-----------|-----------|--------|
| Fiscal | 80% | 🟡 Quase completo |
| Telecom | 90% | 🟢 Quase lá |
| Legal | 70% | 🟡 Em progresso |
| Financial | 95% | 🟢 Quase completo |
| Demographics | 100% | ✅ Completo |
| Business | 85% | 🟢 Quase completo |

---

**Mantido por:** [Marcos Torres](https://github.com/mtorresbr) e [Comunidade Open Source](https://github.com/mtorresbr/global-countries-data)
**Licença:** MIT
**Schema:** countries-data/v1
**Última atualização:** 30 de abril de 2026
