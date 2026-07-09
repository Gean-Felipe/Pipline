# Requisitos Funcionais

> Framework para Descoberta, Normalização e Migração de Categorias para o Edocman

---

# 1. Introdução

Os requisitos funcionais descrevem todas as funcionalidades que deverão ser implementadas pelo **Migration Framework**.

Cada requisito representa uma responsabilidade do sistema e define o comportamento esperado durante o processo de migração.

Todos os módulos do framework deverão atender aos requisitos descritos neste documento.

---

# 2. Visão Geral

O framework deverá ser capaz de executar o seguinte fluxo operacional:

```text
Conectar ao Banco
        │
        ▼
Executar SQL
        │
        ▼
Extrair Dados
        │
        ▼
Descobrir Categorias
        │
        ▼
Normalizar
        │
        ▼
Localizar Categoria
        │
        ▼
Criar Relacionamento
        │
        ▼
Validar
        │
        ▼
Gerar Relatórios
```

---

# 3. Lista de Requisitos

| Código | Funcionalidade | Módulo |
|---------|----------------|---------|
| RF001 | Conexão com Banco | Database |
| RF002 | Execução de SQL | SQL Loader |
| RF003 | Extração dos Dados | Extraction |
| RF004 | Discovery das Categorias | Discovery |
| RF005 | Normalização | Normalizer |
| RF006 | Busca da Categoria | Category Lookup |
| RF007 | Relacionamento | Relationship Loader |
| RF008 | Validação | Validation |
| RF009 | Logs | Logger |
| RF010 | Relatórios | Reports |

---

# RF001 — Conexão com Banco de Dados

## Objetivo

Permitir que o framework estabeleça conexão com os bancos de dados de origem e destino.

## Entradas

- Host
- Porta
- Banco
- Usuário
- Senha

## Processamento

O sistema deverá abrir uma conexão utilizando os parâmetros definidos no arquivo de configuração.

## Saída

Conexão ativa com o banco.

---

# RF002 — Execução de SQL

## Objetivo

Executar consultas SQL externas.

## Entradas

Arquivo `.sql`

## Processamento

O framework deverá carregar o arquivo SQL e executá-lo no banco de origem.

## Saída

Resultado da consulta.

---

# RF003 — Extração dos Dados

## Objetivo

Carregar os dados da consulta em memória.

## Entradas

Resultado da consulta SQL.

## Processamento

Os dados deverão ser convertidos para um DataFrame do Pandas.

## Saída

DataFrame contendo os documentos.

---

# RF004 — Discovery das Categorias

## Objetivo

Identificar automaticamente a categoria correspondente a cada documento.

## Entradas

DataFrame de documentos.

## Processamento

O framework deverá localizar a categoria utilizando regras configuráveis.

A categoria poderá estar em:

- coluna específica;
- título;
- storage_path;
- descrição;
- regra personalizada.

## Saída

Categoria encontrada.

---

# RF005 — Normalização

## Objetivo

Padronizar os nomes das categorias.

## Entradas

Categoria identificada.

## Processamento

Aplicar regras de normalização.

Exemplos:

```text
Ata Registro Preço 2025

↓

Ata de Registro de Preço 2025
```

Outras transformações:

- remover espaços extras;
- remover caracteres especiais;
- remover acentos;
- padronizar abreviações;
- padronizar caixa de texto.

## Saída

Categoria normalizada.

---

# RF006 — Busca da Categoria

## Objetivo

Localizar automaticamente a categoria correspondente no Edocman.

## Entradas

Categoria normalizada.

## Processamento

Pesquisar na tabela de categorias do Edocman.

## Saída

```text
category_id
```

Caso não seja localizada, registrar inconsistência.

---

# RF007 — Criação do Relacionamento

## Objetivo

Criar o relacionamento entre documento e categoria.

## Entradas

- document_id
- category_id

## Processamento

Inserir automaticamente um registro na tabela

```text
GWS_edocman_document_category
```

preenchendo:

- document_id
- category_id
- is_main_category

## Saída

Relacionamento criado.

---

# RF008 — Validação

## Objetivo

Validar a consistência da migração.

## Processamento

Verificar:

- documentos sem categoria;
- categorias inexistentes;
- categorias duplicadas;
- falhas de inserção;
- registros inconsistentes.

## Saída

Lista de inconsistências.

---

# RF009 — Registro de Logs

## Objetivo

Registrar todas as operações executadas pelo framework.

## Informações registradas

- início da execução;
- consultas SQL;
- categorias encontradas;
- categorias não encontradas;
- erros;
- avisos;
- tempo de execução.

## Saída

Arquivo de log.

---

# RF010 — Relatórios

## Objetivo

Gerar um relatório completo da execução.

O relatório deverá conter:

- documentos processados;
- categorias identificadas;
- categorias relacionadas;
- categorias não encontradas;
- erros;
- avisos;
- tempo de execução.

## Saída

Relatório da migração.

---

# 4. Dependência entre os Requisitos

Os requisitos funcionam de forma sequencial.

```text
RF001
Conexão
      │
      ▼
RF002
SQL
      │
      ▼
RF003
Extração
      │
      ▼
RF004
Discovery
      │
      ▼
RF005
Normalização
      │
      ▼
RF006
Busca
      │
      ▼
RF007
Relacionamento
      │
      ▼
RF008
Validação
      │
      ▼
RF009
Logs
      │
      ▼
RF010
Relatórios
```

---

# 5. Critérios de Aceitação

Cada requisito será considerado concluído quando:

| Requisito | Critério |
|------------|-----------|
| RF001 | Conectar aos bancos de origem e destino. |
| RF002 | Executar consultas SQL externas. |
| RF003 | Carregar os dados em DataFrames. |
| RF004 | Identificar corretamente as categorias. |
| RF005 | Aplicar todas as regras de normalização. |
| RF006 | Localizar corretamente o `category_id`. |
| RF007 | Inserir registros na `GWS_edocman_document_category`. |
| RF008 | Detectar inconsistências automaticamente. |
| RF009 | Registrar todas as operações em log. |
| RF010 | Gerar relatório completo da migração. |

---

# Resumo

Os requisitos funcionais definem todas as capacidades do **Migration Framework**, desde a conexão com os bancos de dados até a geração do relatório final. Cada requisito está diretamente associado a um módulo da arquitetura, garantindo rastreabilidade entre a documentação e a implementação do sistema.