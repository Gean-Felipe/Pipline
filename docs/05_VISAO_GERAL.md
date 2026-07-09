# Visão Geral

> Framework para Descoberta, Normalização e Migração de Categorias para o Edocman

---

# 1. Introdução

O **Migration Framework** é uma solução desenvolvida para automatizar o processo de descoberta, normalização e relacionamento de categorias entre diferentes sistemas de gerenciamento de documentos e o componente **Edocman**.

O framework foi projetado para atuar como uma camada intermediária entre o banco de dados de origem e o banco de dados de destino, abstraindo as diferenças estruturais existentes entre os sistemas e fornecendo um fluxo único de processamento.

Dessa forma, cada novo projeto de migração necessita apenas da configuração das consultas SQL e das regras específicas do cliente, reutilizando toda a infraestrutura já desenvolvida.

---

# 2. Visão Geral da Arquitetura

O framework é composto por módulos independentes, cada um responsável por uma etapa específica do processo de migração.

```text
                Migration Framework

        ┌────────────────────────────┐
        │      Banco de Origem       │
        └─────────────┬──────────────┘
                      │
                      ▼
              Extração dos Dados
                      │
                      ▼
             Discovery das Categorias
                      │
                      ▼
              Normalização dos Dados
                      │
                      ▼
       Construção da Categoria Final
                      │
                      ▼
        Busca da Categoria no Destino
                      │
                      ▼
             Obtenção do category_id
                      │
                      ▼
      Criação do Relacionamento
                      │
                      ▼
            Validação dos Dados
                      │
                      ▼
             Logs e Relatórios
```

Cada módulo possui apenas uma responsabilidade, permitindo manutenção, reutilização e evolução independentes.

---

# 3. Fluxo Geral do Processo

O processamento ocorre em uma sequência lógica de etapas.

## Etapa 1 — Extração

O framework conecta-se ao banco de dados de origem e executa uma consulta SQL previamente configurada.

O resultado é carregado em um DataFrame do Pandas.

---

## Etapa 2 — Discovery

Nesta etapa o framework identifica automaticamente a categoria de cada documento.

Dependendo da estrutura do banco de origem, a categoria poderá estar localizada em diferentes campos.

Exemplos:

- tabela de documentos;
- coluna específica;
- título do documento;
- caminho do arquivo (`storage_path`);
- regra personalizada.

---

## Etapa 3 — Normalização

Após identificar a categoria, são aplicadas regras de padronização para reduzir diferenças de escrita.

Entre as transformações realizadas estão:

- remoção de espaços duplicados;
- remoção de caracteres especiais;
- remoção de acentos;
- padronização de caixa (maiúsculas/minúsculas);
- substituição de abreviações.

O objetivo é garantir que categorias equivalentes sejam tratadas como iguais.

---

## Etapa 4 — Construção da Categoria Final

Após a normalização, o framework gera a categoria que será utilizada para localizar o registro correspondente no banco de destino.

Exemplo:

```text
Origem

Ata Registro de Preços 2025

↓

Normalização

Ata de Registro de Preço 2025
```

Essa categoria passa a representar o padrão utilizado durante toda a migração.

---

## Etapa 5 — Busca da Categoria

Com a categoria final definida, o framework consulta o banco do Edocman para localizar a categoria correspondente.

O resultado dessa consulta é a obtenção do identificador único da categoria (`category_id`).

Caso nenhuma categoria seja encontrada, o framework registra a inconsistência para análise posterior.

---

## Etapa 6 — Relacionamento

Após localizar a categoria, o framework cria automaticamente o relacionamento entre documento e categoria.

O relacionamento é inserido na tabela:

```text
GWS_edocman_document_category
```

Cada registro contém:

- document_id;
- category_id;
- is_main_category.

---

## Etapa 7 — Validação

Antes da finalização da migração, o framework realiza diversas validações para garantir a integridade dos dados.

São verificadas situações como:

- categorias inexistentes;
- documentos sem categoria;
- relacionamentos duplicados;
- falhas de inserção.

---

## Etapa 8 — Relatórios

Ao final do processamento são gerados relatórios contendo informações sobre toda a execução.

Entre elas:

- quantidade de documentos processados;
- categorias encontradas;
- categorias relacionadas;
- erros;
- avisos;
- tempo de execução.

---

# 4. Fluxo Completo

```text
Banco de Origem
        │
        ▼
Conexão
        │
        ▼
Consulta SQL
        │
        ▼
DataFrame
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
Validação
        │
        ▼
Relatórios
```

---

# 5. Componentes do Framework

O framework será organizado em módulos independentes.

| Módulo              | Responsabilidade                                     |
| ------------------- | ---------------------------------------------------- |
| Config              | Carregar parâmetros de configuração.                 |
| Database            | Gerenciar conexões com os bancos de dados.           |
| SQL Loader          | Carregar consultas SQL externas.                     |
| Extraction          | Executar consultas e carregar os dados.              |
| Discovery           | Identificar categorias na origem.                    |
| Normalization       | Padronizar os nomes das categorias.                  |
| Category Builder    | Construir a categoria final.                         |
| Category Lookup     | Localizar a categoria no Edocman.                    |
| Relationship Loader | Criar relacionamentos entre documentos e categorias. |
| Validation          | Validar a integridade da migração.                   |
| Reports             | Gerar relatórios de execução.                        |
| Logs                | Registrar todas as operações realizadas.             |

---

# 6. Benefícios da Arquitetura

A arquitetura proposta oferece diversas vantagens.

## Modularidade

Cada componente possui uma única responsabilidade, facilitando manutenção e evolução.

---

## Reutilização

O núcleo do framework permanece o mesmo para diferentes clientes, alterando apenas as consultas SQL e configurações.

---

## Flexibilidade

O framework adapta-se a diferentes estruturas de banco de dados sem necessidade de alterações significativas no código.

---

## Escalabilidade

Novos módulos e novas regras podem ser adicionados sem impactar o restante da aplicação.

---

## Manutenibilidade

A separação entre configuração, regras de negócio e acesso ao banco reduz o acoplamento e facilita futuras modificações.

---

# 7. Resultado Esperado

Ao término do processamento, o framework deverá entregar:

- documentos processados;
- categorias identificadas;
- categorias normalizadas;
- `category_id` localizado;
- relacionamentos inseridos na tabela `GWS_edocman_document_category`;
- inconsistências registradas;
- logs detalhados;
- relatório final da execução.

---

# Resumo

O **Migration Framework** atua como uma camada de transformação entre diferentes sistemas de origem e o Edocman. Seu objetivo é abstrair as diferenças entre as bases de dados, automatizar a identificação e padronização das categorias e criar os relacionamentos necessários para que os documentos sejam corretamente classificados no sistema de destino.

A arquitetura modular permite que o framework seja reutilizado em diferentes projetos de migração, exigindo apenas adaptações nas consultas SQL e nas configurações específicas de cada cliente.
