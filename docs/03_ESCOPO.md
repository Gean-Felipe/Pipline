# Escopo

> Framework para Descoberta, Normalização e Migração de Categorias para o Edocman

---

# 1. Introdução

Este documento define o escopo do **Migration Framework**, estabelecendo os limites de atuação do sistema, suas responsabilidades e as funcionalidades que fazem parte da solução.

O framework foi desenvolvido para automatizar o processo de identificação, normalização e relacionamento de categorias provenientes de diferentes bancos de dados, permitindo sua utilização no componente **Edocman**.

---

# 2. Escopo do Projeto

O framework tem como responsabilidade principal automatizar o processo de migração de categorias entre diferentes sistemas de origem e o banco de dados do Edocman.

O processo inicia na extração dos documentos da base de origem e termina com a criação do relacionamento entre documentos e categorias na tabela `GWS_edocman_document_category`.

Todo o processamento deverá ocorrer de forma automatizada, reduzindo atividades manuais e permitindo a reutilização das regras de negócio em diferentes projetos.

---

# 3. Funcionalidades Contempladas

O framework deverá executar as seguintes etapas:

## 3.1 Conexão com Banco de Dados

- Conectar ao banco de dados de origem;
- Conectar ao banco de dados de destino;
- Utilizar parâmetros configuráveis;
- Permitir reutilização em diferentes clientes.

---

## 3.2 Extração de Dados

Executar consultas SQL para recuperar os documentos da base de origem.

Os dados deverão ser carregados em DataFrames do Pandas para processamento.

---

## 3.3 Descoberta das Categorias

Identificar automaticamente a categoria associada a cada documento.

A categoria poderá estar armazenada em diferentes estruturas, dependendo do sistema de origem.

Exemplos:

- coluna específica;
- título do documento;
- caminho do arquivo (`storage_path`);
- regras definidas para o cliente.

---

## 3.4 Normalização

Aplicar regras de padronização para garantir que categorias semanticamente iguais sejam tratadas como uma única categoria.

Entre as regras previstas estão:

- remoção de espaços extras;
- padronização de maiúsculas e minúsculas;
- remoção de caracteres especiais;
- remoção de acentos;
- padronização de abreviações;
- remoção de informações que não fazem parte da categoria.

---

## 3.5 Construção da Categoria Final

Após a normalização, o framework deverá gerar a categoria utilizada para localizar o registro correspondente no Edocman.

Exemplo:

Categoria encontrada na origem

```text
Ata de Registro de Preço 2025
```

Categoria utilizada na busca

```text
Ata de Registro de Preço 2025
```

Caso necessário, regras específicas poderão ser aplicadas para padronização.

---

## 3.6 Localização da Categoria

O framework deverá localizar automaticamente o registro correspondente no banco de dados do Edocman.

O resultado esperado será a obtenção do identificador único da categoria (`category_id`).

---

## 3.7 Criação do Relacionamento

Após localizar a categoria correta, o framework deverá inserir automaticamente o relacionamento na tabela:

```text
GWS_edocman_document_category
```

Cada relacionamento deverá conter:

- document_id;
- category_id;
- is_main_category.

---

## 3.8 Validação

Antes da conclusão da migração deverão ser executadas validações para identificar possíveis inconsistências.

Entre elas:

- categorias inexistentes;
- documentos sem categoria;
- relacionamentos duplicados;
- falhas de inserção;
- inconsistências de dados.

---

## 3.9 Relatórios

Ao término da execução deverão ser gerados relatórios contendo:

- documentos processados;
- categorias encontradas;
- categorias relacionadas;
- erros;
- avisos;
- tempo de execução.

---

# 4. Funcionalidades Fora do Escopo

A versão atual do framework não contempla:

- criação automática de categorias;
- alteração da estrutura do banco de dados;
- migração dos arquivos físicos dos documentos;
- interface gráfica;
- API REST;
- sincronização entre bancos;
- atualização de documentos existentes;
- exclusão de registros;
- gerenciamento de usuários.

Essas funcionalidades poderão ser incorporadas em versões futuras.

---

# 5. Limites do Sistema

O framework atua exclusivamente no processamento dos dados necessários para criar o relacionamento entre documentos e categorias.

A aplicação pressupõe que:

- o banco de origem esteja acessível;
- o banco de destino esteja acessível;
- os documentos já existam no sistema de destino;
- as categorias já estejam cadastradas no Edocman.

Caso essas condições não sejam atendidas, a execução poderá ser interrompida ou registrar inconsistências para análise posterior.

---

# 6. Fluxo Geral

```text
Banco de Origem
        │
        ▼
Consulta SQL
        │
        ▼
Extração dos Documentos
        │
        ▼
Descoberta da Categoria
        │
        ▼
Normalização
        │
        ▼
Categoria Final
        │
        ▼
Busca da Categoria
        │
        ▼
category_id
        │
        ▼
Inserção em
GWS_edocman_document_category
        │
        ▼
Validação
        │
        ▼
Relatórios
```

---

# 7. Resultado do Escopo

Ao final da execução, o framework deverá entregar:

- documentos processados;
- categorias identificadas;
- categorias normalizadas;
- categorias localizadas no Edocman;
- relacionamentos criados;
- inconsistências registradas;
- logs de execução;
- relatório final da migração.

---

# Resumo

O escopo do **Migration Framework** está concentrado na automação do processo de descoberta, normalização e relacionamento de categorias entre sistemas de origem e o Edocman. O framework não realiza alterações estruturais no banco de dados nem cria novas categorias, limitando-se a identificar, localizar e associar corretamente os documentos às categorias já existentes no sistema de destino.
