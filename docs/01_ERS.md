# Especificação de Requisitos do Sistema (ERS)

> Framework para Descoberta, Normalização e Migração de Categorias para o Edocman

---

| Informação | Valor                                  |
| ---------- | -------------------------------------- |
| Projeto    | Migration Framework                    |
| Documento  | Especificação de Requisitos do Sistema |
| Versão     | 1.0                                    |
| Autor      | Gean                                   |
| Data       | Julho/2026                             |
| Status     | Em Desenvolvimento                     |

---

# Sumário

1. Introdução
2. Objetivo
3. Escopo
4. Definições
5. Visão Geral
6. Stakeholders
7. Requisitos Funcionais
8. Requisitos Não Funcionais
9. Restrições Técnicas
10. Premissas
11. Riscos
12. Critérios de Aceitação
13. Fora do Escopo

---

# 1. Introdução

## 1.1 Finalidade

Este documento especifica os requisitos funcionais e não funcionais do **Migration Framework**, estabelecendo as regras que deverão ser atendidas durante o desenvolvimento.

A ERS servirá como referência para implementação, testes, manutenção e evolução do framework.

---

## 1.2 Objetivo do Sistema

O framework tem como objetivo automatizar a descoberta, normalização e classificação de categorias provenientes de diferentes bancos de dados, criando automaticamente os relacionamentos necessários entre documentos e categorias no Edocman.

O sistema foi concebido para reduzir atividades manuais, aumentar a confiabilidade das migrações e permitir a reutilização do processo para diferentes clientes.

---

# 2. Escopo

O framework deverá ser capaz de:

- conectar-se ao banco de origem;
- executar consultas SQL;
- extrair documentos;
- identificar categorias automaticamente;
- normalizar categorias;
- localizar categorias no banco de destino;
- obter o `category_id`;
- criar relacionamentos na tabela `GWS_edocman_document_category`;
- validar os resultados;
- gerar logs e relatórios.

O framework não será responsável pela criação do banco de dados de destino nem pela criação de categorias inexistentes.

---

# 3. Definições

| Termo           | Definição                                                  |
| --------------- | ---------------------------------------------------------- |
| Origem          | Banco de dados do cliente.                                 |
| Destino         | Banco de dados do Edocman.                                 |
| Discovery       | Processo de identificação automática da categoria.         |
| Normalização    | Padronização dos textos para comparação.                   |
| Categoria Pai   | Categoria principal, sem o ano.                            |
| Categoria Final | Categoria utilizada para localizar o `category_id`.        |
| Relacionamento  | Registro criado na tabela `GWS_edocman_document_category`. |

---

# 4. Visão Geral

O framework será dividido em módulos independentes.

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
Normalização
        │
        ▼
Construção da Categoria Final
        │
        ▼
Busca da Categoria
        │
        ▼
Relacionamento
        │
        ▼
Validação
        │
        ▼
Relatórios
```

Cada módulo possuirá responsabilidade única, reduzindo o acoplamento entre as camadas.

---

# 5. Stakeholders

Os principais interessados no framework são:

- Desenvolvedor responsável pelas migrações;
- Equipe de desenvolvimento;
- Equipe de suporte;
- Administrador de Banco de Dados (DBA);
- Gestores responsáveis pelos projetos de migração.

---

# 6. Requisitos Funcionais

## RF001 — Conexão

O sistema deverá conectar-se ao banco de dados de origem utilizando parâmetros configuráveis.

---

## RF002 — Execução de SQL

O sistema deverá executar consultas SQL externas armazenadas em arquivos `.sql`.

---

## RF003 — Extração

Os documentos deverão ser carregados em DataFrames do Pandas.

---

## RF004 — Discovery

O sistema deverá identificar automaticamente a categoria de cada documento.

A categoria poderá ser obtida por:

- campo específico;
- título;
- caminho do arquivo (`storage_path`);
- expressão regular;
- regra personalizada.

---

## RF005 — Normalização

O sistema deverá padronizar os textos antes da comparação.

As transformações deverão incluir:

- remoção de acentos;
- remoção de espaços duplicados;
- padronização de maiúsculas/minúsculas;
- remoção de caracteres especiais;
- normalização de abreviações.

---

## RF006 — Construção da Categoria

O sistema deverá gerar automaticamente a categoria final a partir da categoria identificada.

---

## RF007 — Busca da Categoria

O sistema deverá localizar automaticamente a categoria correspondente no banco de destino.

O resultado esperado é a obtenção do `category_id`.

---

## RF008 — Relacionamento

O sistema deverá inserir registros automaticamente na tabela:

```text
GWS_edocman_document_category
```

utilizando:

- document_id;
- category_id;
- is_main_category.

---

## RF009 — Validação

O sistema deverá validar:

- categorias inexistentes;
- categorias duplicadas;
- documentos sem categoria;
- falhas de relacionamento;
- inconsistências nos dados.

---

## RF010 — Relatórios

Ao final da execução deverão ser gerados:

- quantidade de documentos processados;
- quantidade de relacionamentos criados;
- categorias não encontradas;
- erros;
- avisos;
- tempo de execução.

---

# 7. Requisitos Não Funcionais

## RNF001 — Reutilização

O framework deverá permitir sua utilização em diferentes clientes sem alterações no núcleo do sistema.

---

## RNF002 — Configuração

Toda configuração deverá ser realizada por arquivos externos.

---

## RNF003 — Modularidade

Cada módulo deverá possuir apenas uma responsabilidade.

---

## RNF004 — Manutenibilidade

O código deverá seguir padrões que facilitem manutenção e evolução.

---

## RNF005 — Reexecução

O processo deverá ser reexecutável sem necessidade de recriação da estrutura do banco.

---

## RNF006 — Registro de Logs

Todas as etapas deverão registrar informações detalhadas para auditoria e diagnóstico.

---

# 8. Restrições Técnicas

O desenvolvimento deverá utilizar:

- Python 3;
- Pandas;
- SQLAlchemy;
- PyMySQL;
- MySQL/MariaDB.

As consultas SQL deverão permanecer desacopladas do código Python.

---

# 9. Premissas

Para execução do framework considera-se que:

- existe acesso ao banco de origem;
- existe acesso ao banco de destino;
- os documentos já foram migrados;
- as categorias já existem no Edocman;
- o objetivo é apenas localizar a categoria correta e criar o relacionamento.

---

# 10. Riscos

Os principais riscos identificados são:

- categorias inexistentes no destino;
- nomenclaturas inconsistentes;
- documentos sem categoria;
- alterações na estrutura dos bancos de origem;
- regras específicas de determinados clientes.

---

# 11. Critérios de Aceitação

O framework será considerado concluído quando for capaz de:

- conectar aos bancos de dados;
- identificar categorias automaticamente;
- normalizar os dados;
- localizar o `category_id`;
- inserir registros na tabela de relacionamento;
- validar inconsistências;
- gerar logs e relatórios.

---

# 12. Fora do Escopo

Não fazem parte desta versão:

- criação automática de categorias;
- alteração da estrutura dos bancos;
- interface gráfica;
- API REST;
- dashboard de monitoramento;
- migração de arquivos físicos.

---

# Histórico de Versões

| Versão | Data       | Autor | Descrição                                      |
| ------ | ---------- | ----- | ---------------------------------------------- |
| 1.0    | Julho/2026 | Gean  | Criação inicial da ERS do Migration Framework. |
