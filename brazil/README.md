# Brazil (Brasil) - Dados do País

Este diretório contém todos os dados estruturados para operar sistemas de IA e empresas "AI First" no Brasil.

## 📊 Resumo Rápido

| Atributo | Valor |
|----------|-------|
| **ISO Code** | BR (BRA) |
| **Moeda** | Real (BRL / R$) |
| **Idioma** | Português (pt-BR) |
| **População** | 215 milhões |
| **PIB** | USD 1.9 trilhões |
| **Prefixo Telefônico** | +55 |
| **Formato CEP** | XXXXX-XXX |

## 📁 Estrutura de Dados

### [COUNTRY.md](COUNTRY.md)
Metadados principais com YAML frontmatter - schema, versão, autores, completude.

### [Fiscal/](fiscal/)
Dados fiscais tributários:
- [tax-codes.yaml](fiscal/tax-codes.yaml) - Impostos (ICMS, IPI, PIS/COFINS), regimes (Simples Nacional, Lucro Real)
- Regimes de tributação e alíquotas
- NF-e (Nota Fiscal Eletrônica) e obrigações acessórias

### [Financial/](financial/)
Bancos e métodos de pagamento:
- [banks.yaml](financial/banks.yaml) - Top 10 bancos (Itaú, BB, Bradesco, Caixa, Santander)
- PIX (pagamento instantâneo obrigatório)
- Boleto bancário, cartões de crédito
- Gateways: PagSeguro, Mercado Pago, Stone, Cielo

### [Telecom/](telecom/)
Formatos de comunicação:
- [phone-formats.yaml](telecom/phone-formats.yaml) - Formatos de telefone (celular +55 11 9XXXX-XXXX)
- CEP (Código de Endereçamento Postal)
- DDDs por estado
- Padrão de endereço brasileiro

### [Demographics/](demographics/)
Dados populacionais:
- [population.yaml](demographics/population.yaml) - População por região, faixa etária, gênero
- Fusos horários (UTC-2 a UTC-5)
- Idiomas e cultura
- Indicadores sociais (IDH, Gini)

### [Business/](business/)
Dados empresariais:
- [company-sizes.yaml](business/company-sizes.yaml) - Portes (Micro, Pequena, Média, Grande, MEI)
- Setores CNAE
- Horários comerciais
- Feriados nacionais 2026
- Ecossistema de startups (13k startups, 17 unicórnios)

### [Legal/](legal/) (Em breve)
- Tipos de empresa (LTDA, SA, EIRELI)
- Requisitos de registro (CNPJ, Junta Comercial)
- LGPD (Lei Geral de Proteção de Dados)
- Compliance e regulamentação

## 🤖 Como Usar (Para IAs)

### Python
```python
import yaml

# Carregar dados fiscais
with open('fiscal/tax-codes.yaml') as f:
    tax = yaml.safe_load(f)
    print(f"Regimes: {[r['code'] for r in tax['tax_regimes']]}")

# Validar telefone brasileiro
import re
with open('telecom/phone-formats.yaml') as f:
    phone = yaml.safe_load(f)
    pattern = phone['phone']['formats']['mobile']['pattern']
    test = "+5511999999999"
    print(f"Válido: {bool(re.match(pattern, test))}")

# Verificar bancos com PIX
with open('financial/banks.yaml') as f:
    banks = yaml.safe_load(f)
    pix_banks = [b['name'] for b in banks['banks'] if b.get('pix_enabled')]
    print(f"Bancos com PIX: {pix_banks}")
```

### JSON Schema Validation
```bash
python ../scripts/validate-country.py --country brazil
```

## 🏆 Destaques para Sistemas Multi-Agent

1. **PIX Obrigatório**: Sistema de pagamento instantâneo brasileiro (24/7)
2. **NF-e**: Nota Fiscal Eletrônica obrigatória (modelo 55)
3. **Simples Nacional**: Regime simplificado até R$ 3.6M/ano
4. **LGPD**: Lei de proteção de dados (equivalente ao GDPR)
5. **CNPJ**: 14 dígitos, obrigatório para empresas
6. **4 Fusos Horários**: Do UTC-2 (Fernando de Noronha) ao UTC-5 (Acre)
7. **13.000 Startups**: 5º maior ecossistema da América Latina

## 📈 Status de Completude

| Categoria | Progresso |
|-----------|-----------|
| Fiscal | ████████░░ 80% |
| Telecom | █████████░ 90% |
| Legal | ██████░░░░ 70% |
| Financial | ██████████ 95% |
| Demographics | ██████████ 100% |
| Business | █████████░ 85% |

## 🤝 Contribua

Encontrou dados desatualizados ou quer adicionar mais informações?
1. Edite os arquivos YAML
2. Rode `python ../scripts/validate-country.py --country brazil`
3. Abra um Pull Request

## 📚 Fontes Oficiais

- **Receita Federal**: https://www.receita.fazenda.gov.br
- **Banco Central**: https://www.bcb.gov.br
- **IBGE**: https://www.ibge.gov.br
- **Sebrae**: https://www.sebrae.com.br
- **Correios**: https://www.correios.com.br

---

**Mantido por:** [Marcos Torres](https://github.com/mtorresbr)  
**Atualizado em:** 30 de abril de 2026  
**Schema:** countries-data/v1  
**Licença:** MIT
