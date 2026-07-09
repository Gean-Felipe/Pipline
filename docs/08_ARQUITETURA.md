# Arquitetura do Sistema

> Framework para Descoberta, Normalização e Relacionamento de Categorias para o Edocman

---

# 1. Introdução

Este documento descreve a arquitetura do **Migration Framework**, apresentando sua organização em módulos, responsabilidades, fluxo de execução e interação entre os componentes.

A arquitetura foi projetada seguindo os princípios de modularidade, reutilização e baixo acoplamento, permitindo que novas migrações sejam configuradas sem alterações significativas no núcleo da aplicação.

---

# 2. Visão Geral

O framework atua como uma camada intermediária entre o banco de dados de origem e o banco de dados do Edocman.

Seu objetivo é extrair os documentos da origem, identificar suas categorias, aplicar regras de normalização, localizar a categoria correspondente no banco de destino e criar o relacionamento entre documentos e categorias.

```text
              Banco de Origem
                     │
                     ▼
          ┌──────────────────────┐
          │  Migration Framework │
          └──────────────────────┘
                     │
                     ▼
             Banco do Edocman
```

---

# 3. Arquitetura em Camadas

O framework será dividido em camadas, cada uma responsável por uma parte específica do processo.

```text
┌──────────────────────────────┐
│        Configuração          │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│      Acesso ao Banco         │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│      Extração dos Dados      │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ Discovery das Categorias     │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ Normalização                 │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ Busca da Categoria           │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ Relacionamento               │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│ Validação e Relatórios       │
└──────────────────────────────┘
```

---

# 4. Componentes da Arquitetura

## Config

Responsável por carregar todas as configurações do projeto.

Exemplos:

- conexão com banco;
- cliente;
- SQL utilizada;
- parâmetros da migração;
- regras de normalização.

---

## Database

Gerencia as conexões com os bancos de dados.

Responsabilidades:

- abrir conexão;
- fechar conexão;
- executar comandos SQL;
- controlar transações.

---

## SQL Loader

Responsável por localizar e carregar consultas SQL armazenadas em arquivos externos.

Exemplo:

```text
sql/

extract_documents.sql
lookup_category.sql
insert_relationship.sql
```

---

## Extraction

Executa a consulta SQL no banco de origem.

Resultado:

```text
Banco

↓

DataFrame
```

Todo o processamento posterior será realizado sobre DataFrames.

---

## Discovery

Responsável por descobrir onde está localizada a categoria.

Dependendo do cliente, ela poderá estar:

- coluna específica;
- título;
- storage_path;
- descrição;
- regra personalizada.

---

## Normalizer

Aplica regras para padronizar as categorias.

Exemplos:

Antes

```text
Ata Registro Preço 2025
```

Depois

```text
Ata de Registro de Preço 2025
```

As regras poderão incluir:

- remoção de espaços;
- remoção de acentos;
- substituição de palavras;
- padronização de caixa;
- expressões regulares.

---

## Category Lookup

Pesquisa a categoria normalizada no banco do Edocman.

Entrada:

```text
Ata de Registro de Preço 2025
```

Saída:

```text
category_id = 18
```

---

## Relationship Loader

Cria o relacionamento na tabela:

```text
GWS_edocman_document_category
```

Campos inseridos:

- document_id;
- category_id;
- is_main_category.

---

## Validation

Executa verificações após a migração.

Exemplos:

- categoria inexistente;
- documento sem categoria;
- relacionamento duplicado;
- erro de inserção.

---

## Logger

Registra todas as operações executadas.

Exemplo:

```text
08:30

Categoria localizada

Ata de Registro de Preço 2025

category_id = 18
```

---

## Reports

Gera o relatório final da migração.

Informações:

- documentos processados;
- categorias encontradas;
- categorias não encontradas;
- relacionamentos criados;
- erros;
- tempo de execução.

---

# 5. Fluxo de Execução

```text
Início

↓

Carregar Configuração

↓

Abrir Banco

↓

Executar SQL

↓

Criar DataFrame

↓

Discovery

↓

Normalização

↓

Buscar Categoria

↓

Obter category_id

↓

Inserir Relacionamento

↓

Validar

↓

Gerar Relatórios

↓

Fim
```

---

# 6. Estrutura de Diretórios

```text
migration-framework/

│
├── config/
│   ├── database.yaml
│   ├── client.yaml
│   └── normalize.yaml
│
├── database/
│   ├── connection.py
│   └── executor.py
│
├── sql/
│   ├── extract_documents.sql
│   ├── lookup_category.sql
│   └── insert_relationship.sql
│
├── extraction/
│   └── extractor.py
│
├── discovery/
│   └── discover.py
│
├── normalizer/
│   └── normalize.py
│
├── lookup/
│   └── category_lookup.py
│
├── relationship/
│   └── relationship_loader.py
│
├── validation/
│   └── validator.py
│
├── reports/
│   └── report.py
│
├── logs/
│
├── main.py
│
└── README.md
```

---

# 7. Comunicação entre os Componentes

```text
Config
   │
   ▼
Database
   │
   ▼
Extraction
   │
   ▼
Discovery
   │
   ▼
Normalizer
   │
   ▼
Category Lookup
   │
   ▼
Relationship Loader
   │
   ▼
Validation
   │
   ▼
Reports
```

Cada módulo recebe apenas os dados necessários da etapa anterior, reduzindo o acoplamento e facilitando testes e manutenção.

---

# 8. Princípios Arquiteturais

A arquitetura do framework segue os seguintes princípios:

- Modularidade;
- Baixo acoplamento;
- Alta coesão;
- Reutilização;
- Configuração acima de código;
- Separação de responsabilidades;
- Código reutilizável;
- Escalabilidade;
- Facilidade de manutenção.

---

# 9. Resultado Esperado

A arquitetura proposta permitirá que novas migrações sejam realizadas apenas alterando arquivos de configuração, consultas SQL e regras de normalização, mantendo o núcleo do framework inalterado.

Com isso, o framework torna-se reutilizável, extensível e preparado para suportar diferentes estruturas de bancos de dados de origem.
