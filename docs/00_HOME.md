# Home

> Framework para Descoberta, Normalização e Migração de Categorias para o Edocman

---

# Bem-vindo

Esta documentação descreve toda a arquitetura, regras de negócio, requisitos e fluxo de funcionamento do **Migration Framework**.

O framework foi desenvolvido para automatizar o processo de migração de categorias entre diferentes sistemas de gerenciamento de documentos e o componente **Edocman**, eliminando processos manuais e permitindo reutilização em diversos clientes.

A documentação está organizada de forma modular, permitindo compreender desde a visão geral do projeto até os detalhes técnicos de implementação.

---

# Objetivo da Documentação

Esta documentação possui como objetivos:

- documentar toda a arquitetura do framework;
- registrar as regras de negócio utilizadas durante as migrações;
- servir como guia para futuras implementações;
- facilitar a manutenção do projeto;
- padronizar o processo de desenvolvimento;
- reduzir a dependência de conhecimento individual;
- permitir que novos desenvolvedores compreendam rapidamente o funcionamento do sistema.

---

# Público-Alvo

Esta documentação destina-se a:

- Desenvolvedores;
- Analistas de Sistemas;
- Administradores de Banco de Dados (DBA);
- Responsáveis por Migração de Dados;
- Equipe de Manutenção.

---

# Estrutura da Documentação

A documentação está dividida em diversos documentos especializados.

| Documento                           | Descrição                              |
| ----------------------------------- | -------------------------------------- |
| **01_ERS.md**                       | Especificação de Requisitos do Sistema |
| **02_OBJETIVO.md**                  | Objetivos do projeto                   |
| **03_ESCOPO.md**                    | Escopo do framework                    |
| **04_PROBLEMA_ATUAL.md**            | Situação atual do processo de migração |
| **05_VISAO_GERAL.md**               | Visão geral da solução                 |
| **06_REQUISITOS_FUNCIONAIS.md**     | Requisitos funcionais                  |
| **07_REQUISITOS_NAO_FUNCIONAIS.md** | Requisitos não funcionais              |
| **08_ARQUITETURA.md**               | Arquitetura do framework               |
| **09_PRINCIPIOS.md**                | Princípios de desenvolvimento          |
| **10_RESULTADO_ESPERADO.md**        | Resultados esperados                   |
| **CHANGELOG.md**                    | Histórico de alterações                |

---

# Visão Geral

O framework automatiza o processo de descoberta, classificação e relacionamento de categorias provenientes de diferentes sistemas.

O foco principal não é apenas migrar documentos, mas identificar corretamente a categoria de cada documento e criar automaticamente o relacionamento correspondente no banco de dados do Edocman.

---

# Fluxo Geral

```text
Banco de Origem
        │
        ▼
Extração SQL
        │
        ▼
Discovery
        │
        ▼
Categoria Encontrada
        │
        ▼
Normalização
        │
        ▼
Categoria Final
        │
        ▼
Busca no Edocman
        │
        ▼
category_id
        │
        ▼
Relacionamento
        │
        ▼
Relatórios
```

---

# Estrutura do Projeto

```text
migration-framework/

├── docs/
├── src/
├── sql/
├── config/
├── logs/
├── tests/
└── README.md
```

---

# Tecnologias Utilizadas

O framework utiliza as seguintes tecnologias:

- Python 3
- Pandas
- SQLAlchemy
- PyMySQL
- RapidFuzz
- MySQL
- MariaDB
- Visual Studio Code
- Git

---

# Conceitos Fundamentais

Antes de prosseguir na leitura da documentação, é importante compreender alguns conceitos utilizados pelo framework.

## Discovery

Processo responsável por identificar automaticamente a categoria de um documento a partir das informações disponíveis na base de origem.

---

## Normalização

Processo responsável por padronizar os textos encontrados na origem para garantir consistência durante o mapeamento.

---

## Categoria Pai

Categoria principal utilizada para organizar os documentos.

Exemplo:

```text
Ata de Registro de Preço
```

---

## Categoria Filha

Categoria derivada da categoria principal, normalmente composta pela categoria pai acrescida do ano.

Exemplo:

```text
Ata de Registro de Preço 2025
```

---

## Relacionamento

Após localizar a categoria correspondente no banco de destino, o framework cria automaticamente o vínculo entre documento e categoria na tabela:

```text
GWS_edocman_document_category
```

---

# Navegação Recomendada

Para compreender completamente o framework, recomenda-se a seguinte ordem de leitura:

```text
README

↓

HOME

↓

ERS

↓

Objetivo

↓

Escopo

↓

Problema Atual

↓

Visão Geral

↓

Requisitos

↓

Arquitetura

↓

Princípios

↓

Resultado Esperado
```

---

# Convenções Utilizadas

Durante toda a documentação serão utilizadas as seguintes convenções:

- **Framework** → Sistema desenvolvido neste projeto.
- **Origem** → Banco de dados do cliente.
- **Destino** → Banco de dados do Edocman.
- **Discovery** → Processo de identificação da categoria.
- **Normalização** → Padronização dos dados.
- **Mapeamento** → Associação entre categorias de origem e destino.
- **Relacionamento** → Registro na tabela `GWS_edocman_document_category`.

---

# Próximos Passos

Após a leitura deste documento, recomenda-se prosseguir para:

> **01_ERS.md — Especificação de Requisitos do Sistema**

Este documento apresenta todos os requisitos funcionais e não funcionais que orientam o desenvolvimento do framework.
