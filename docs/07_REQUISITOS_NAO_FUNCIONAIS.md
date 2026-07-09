# Requisitos Não Funcionais

> Framework para Descoberta, Normalização e Migração de Categorias para o Edocman

---

# 1. Introdução

Os requisitos não funcionais estabelecem os padrões de qualidade que deverão ser atendidos pelo **Migration Framework**.

Esses requisitos não descrevem funcionalidades específicas, mas definem características relacionadas ao desempenho, arquitetura, segurança, manutenção e reutilização do sistema.

O atendimento a esses requisitos garante que o framework possa evoluir de forma organizada e ser utilizado em diferentes projetos de migração.

---

# 2. Objetivos

O framework deverá ser desenvolvido de forma que seja:

- reutilizável;
- modular;
- escalável;
- configurável;
- fácil de manter;
- independente do banco de origem;
- confiável;
- extensível.

---

# 3. Requisitos Não Funcionais

## RNF001 — Reutilização

O framework deverá permitir sua utilização em diferentes projetos de migração sem necessidade de alterar o núcleo da aplicação.

As particularidades de cada cliente deverão ser tratadas por meio de arquivos de configuração, consultas SQL e regras de normalização.

---

## RNF002 — Modularidade

O sistema deverá ser dividido em módulos independentes.

Cada módulo deverá possuir apenas uma responsabilidade.

Exemplo:

```text
Database
Extraction
Discovery
Normalizer
Lookup
Relationship
Validation
Reports
```

A alteração em um módulo não deverá impactar os demais.

---

## RNF003 — Configuração Externa

Nenhuma informação específica de um cliente deverá permanecer fixa no código.

Todas as configurações deverão ser armazenadas em arquivos externos.

Exemplos:

- conexão com banco;
- consultas SQL;
- regras de normalização;
- parâmetros da migração.

---

## RNF004 — Baixo Acoplamento

Os módulos deverão possuir o menor número possível de dependências entre si.

A comunicação deverá ocorrer através de interfaces e objetos bem definidos.

---

## RNF005 — Alta Coesão

Cada módulo deverá executar apenas tarefas relacionadas ao seu domínio.

Exemplo:

O módulo **Normalizer** deverá apenas normalizar categorias.

Não deverá executar consultas SQL nem inserir registros no banco.

---

## RNF006 — Escalabilidade

A arquitetura deverá permitir a inclusão de novos módulos sem necessidade de alterações significativas na estrutura existente.

Exemplos:

- novos bancos de origem;
- novos mecanismos de discovery;
- novas regras de normalização;
- novos formatos de relatório.

---

## RNF007 — Manutenibilidade

O código deverá seguir padrões que facilitem sua manutenção.

Boas práticas:

- funções pequenas;
- nomenclatura padronizada;
- documentação;
- comentários quando necessários;
- separação entre responsabilidades.

---

## RNF008 — Portabilidade

O framework deverá executar em diferentes ambientes sem necessidade de alterações no código-fonte.

Ambientes previstos:

- Windows
- Linux

---

## RNF009 — Desempenho

O processamento deverá utilizar estruturas eficientes para reduzir o tempo de execução.

Sempre que possível deverão ser utilizadas operações vetorizadas do Pandas em vez de laços de repetição.

---

## RNF010 — Integridade dos Dados

Nenhuma alteração deverá ser realizada no banco de origem.

Toda a migração deverá ocorrer preservando os dados originais.

---

## RNF011 — Confiabilidade

O framework deverá detectar falhas durante o processamento e registrar informações suficientes para permitir sua identificação e correção.

---

## RNF012 — Registro de Logs

Todas as etapas deverão gerar logs contendo:

- data;
- hora;
- módulo responsável;
- operação executada;
- mensagem;
- nível do log.

Exemplo:

```text
2026-07-10 08:35:10

INFO

Discovery

Categoria encontrada:

Ata de Registro de Preço 2025
```

---

## RNF013 — Auditoria

Toda execução deverá gerar evidências suficientes para permitir auditoria posterior.

Entre elas:

- documentos processados;
- categorias encontradas;
- categorias não localizadas;
- relacionamentos criados;
- erros encontrados.

---

## RNF014 — Reexecução

O framework deverá permitir a reexecução da migração sempre que necessário.

A execução repetida não deverá comprometer a integridade dos dados.

---

## RNF015 — Extensibilidade

Novas funcionalidades deverão poder ser adicionadas sem necessidade de reescrever os módulos existentes.

Exemplos:

- IA para classificação;
- API REST;
- Interface gráfica;
- Dashboard.

---

## RNF016 — Documentação

Toda funcionalidade implementada deverá possuir documentação técnica correspondente.

A documentação deverá ser atualizada sempre que houver alterações na arquitetura ou nas regras de negócio.

---

# 4. Padrões de Desenvolvimento

O framework deverá seguir os seguintes princípios:

- SOLID;
- DRY (Don't Repeat Yourself);
- KISS (Keep It Simple, Stupid);
- Separation of Concerns;
- Clean Code;
- Configuração acima de código.

---

# 5. Tecnologias

O framework deverá utilizar preferencialmente tecnologias consolidadas.

| Tecnologia      | Finalidade                  |
| --------------- | --------------------------- |
| Python          | Linguagem principal         |
| Pandas          | Manipulação de dados        |
| SQLAlchemy      | Conexão com banco           |
| PyMySQL         | Driver MySQL                |
| RapidFuzz       | Similaridade de textos      |
| MySQL / MariaDB | Banco de dados              |
| VS Code         | Ambiente de desenvolvimento |

---

# 6. Critérios de Qualidade

O framework será considerado aderente aos requisitos não funcionais quando:

- permitir reutilização em diferentes clientes;
- possuir arquitetura modular;
- utilizar configuração externa;
- registrar logs completos;
- permitir manutenção simplificada;
- preservar a integridade dos dados;
- executar em diferentes ambientes;
- possibilitar expansão futura.

---

# Resumo

Os requisitos não funcionais definem os padrões de qualidade do **Migration Framework**. Eles garantem que o sistema seja reutilizável, modular, escalável e de fácil manutenção, permitindo sua evolução contínua e a adaptação a diferentes cenários de migração sem comprometer a arquitetura principal.
