# Contributing to Global Countries Data

Obrigado por contribuir! Este repositório visa ser a base de dados mais completa do mundo para sistemas de IA operarem em diferentes países.

## Como Adicionar um Novo País

1. **Crie um diretório** com o código ISO lowercase (ex: `germany/`, `japan/`)
2. **Copie os templates** de `templates/COUNTRY.md.template`
3. **Preencha os dados** seguindo os schemas em `schemas/`
4. **Valide** com `python scripts/validate-country.py --country seu-pais`
5. **Abra um Pull Request** com:
   - Descrição clara das fontes dos dados
   - Screenshots ou links para documentação oficial
   - Status de completude

## Estrutura de um País

```
seu-pais/
├── COUNTRY.md               # Metadados principais (YAML frontmatter)
├── README.md                # Documentação human-readable
├── fiscal/                  # Dados fiscais
│   ├── tax-codes.yaml
│   ├── invoice-requirements.yaml
│   └── fiscal-obligations.yaml
├── telecom/                 # Telecomunicações
│   ├── phone-formats.yaml
│   ├── postal-codes.yaml
│   └── address-standards.yaml
├── legal/                   # Requisitos legais
│   ├── company-types.yaml
│   ├── business-registration.yaml
│   └── compliance-rules.yaml
├── financial/               # Financeiro
│   ├── currency.yaml
│   ├── banks.yaml
│   └── payment-methods.yaml
├── demographics/            # Dados demográficos
│   ├── population.yaml
│   └── languages.yaml
└── business/                # Dados empresariais
    ├── company-sizes.yaml
    └── industry-sectors.yaml
```

## Padrões de Dados

- **Formatos:** Use YAML para dados estruturados (leitura humana + machine-readable)
- **Codificação:** UTF-8
- **Schemas:** Todos os YAML devem ser validados contra o JSON Schema correspondente
- **Fontes:** Sempre cite fontes oficiais (bancos centrais, governos, ISO)

## Completude Mínima para Aceitação

Um país é considerado "aceito" se tiver pelo menos:
- [ ] Dados básicos (ISO, moeda, idioma, população)
- [ ] Formatos de telefone e CEP
- [ ] Lista dos 5+ principais bancos
- [ ] Métodos de pagamento locais
- [ ] Definição de portes de empresa
- [ ] Requisitos legais básicos

## Schemas Disponíveis

- `schemas/country-metadata.json` - Metadados do COUNTRY.md
- `schemas/fiscal.json` - Dados fiscais
- `schemas/telecom.json` - Telecomunicações
- `schemas/legal.json` - Requisitos legais
- `schemas/financial.json` - Bancos e pagamentos
- `schemas/demographics.json` - População e idiomas

## Revisão de PR

- Dados serão verificados contra fontes oficiais
- Schemas devem passar na validação automática (CI/CD)
- Contribuidores são creditados no COUNTRY.md

## Licença

Ao contribuir, você concorda que seus dados estarão sob licença MIT.

## Dicas para Contribuidores

1. **Comece pequeno:** Adicione um país por vez
2. **Documente fontes:** Links para sites oficiais ajudam na revisão
3. **Teste validação:** Rode os scripts antes de abrir o PR
4. **Seja preciso:** Dados incorretos podem causar problemas legais para quem usa
5. **Atualize README:** Adicione o país na tabela principal
