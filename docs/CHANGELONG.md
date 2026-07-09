# Changelog

Todas as alterações relevantes deste projeto serão documentadas neste arquivo.

O formato deste documento é baseado em **Keep a Changelog** e segue o versionamento semântico (Semantic Versioning).

## Versionamento

O projeto utiliza o padrão:

MAJOR.MINOR.PATCH

- **MAJOR** → alterações incompatíveis com versões anteriores.
- **MINOR** → novas funcionalidades compatíveis.
- **PATCH** → correções de bugs e pequenos ajustes.

---

# [0.1.0] - Julho/2026

## Adicionado

### Documentação Inicial

- Criação da estrutura de documentação do projeto.
- Definição da Especificação de Requisitos do Sistema (ERS).
- Criação do README.
- Organização da estrutura de diretórios.
- Definição da arquitetura do framework.

### Engenharia de Software

- Definição dos objetivos do projeto.
- Definição do escopo.
- Levantamento do problema atual.
- Definição da visão geral da solução.
- Definição dos requisitos funcionais.
- Definição dos requisitos não funcionais.
- Definição dos princípios de desenvolvimento.
- Definição do resultado esperado.

### Arquitetura

- Estrutura modular do framework.
- Separação por responsabilidades.
- Definição dos módulos principais.
- Estrutura inicial de diretórios.

### Planejamento

- Definição do fluxo de migração.
- Definição do fluxo de descoberta de categorias.
- Definição do processo de normalização.
- Definição do relacionamento com o Edocman.

---

# [0.2.0] - (Planejado)

## Adicionado

- Estrutura inicial do projeto em Python.
- Configuração do ambiente virtual.
- Implementação do módulo Database.
- Implementação do módulo Config.

---

# [0.3.0] - (Planejado)

## Adicionado

- Implementação do módulo SQL Loader.
- Implementação do módulo Extraction.
- Primeira conexão com o banco de origem.

---

# [0.4.0] - (Planejado)

## Adicionado

- Implementação do módulo Discovery.
- Primeira descoberta automática de categorias.

---

# [0.5.0] - (Planejado)

## Adicionado

- Implementação do módulo Normalizer.
- Criação do mecanismo de regras de normalização.

---

# [0.6.0] - (Planejado)

## Adicionado

- Implementação do Category Lookup.
- Localização automática do category_id.

---

# [0.7.0] - (Planejado)

## Adicionado

- Implementação do Relationship Loader.
- Inserção automática na tabela GWS_edocman_document_category.

---

# [0.8.0] - (Planejado)

## Adicionado

- Implementação do Validation.
- Implementação do Logger.

---

# [0.9.0] - (Planejado)

## Adicionado

- Implementação dos relatórios.
- Exportação dos resultados da migração.

---

# [1.0.0] - (Planejado)

## Primeira versão estável

### Funcionalidades

- Conexão com banco de origem e destino.
- Execução de SQL externa.
- Extração de documentos.
- Discovery das categorias.
- Normalização.
- Busca automática da categoria.
- Criação dos relacionamentos.
- Validação.
- Logs.
- Relatórios.

### Objetivo alcançado

Primeira versão funcional do **Migration Framework**, capaz de executar o processo completo de descoberta, normalização e relacionamento de categorias para o Edocman.
