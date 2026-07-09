# Princípios de Desenvolvimento

> Framework para Descoberta, Normalização e Relacionamento de Categorias para o Edocman

---

# 1. Introdução

Este documento apresenta os princípios de desenvolvimento adotados pelo **Migration Framework**.

Esses princípios estabelecem diretrizes para a arquitetura, organização do código e evolução do projeto, garantindo que o framework permaneça reutilizável, modular, escalável e de fácil manutenção.

Todos os módulos desenvolvidos deverão respeitar os princípios descritos neste documento.

---

# 2. Reutilização

O núcleo do framework deverá ser reutilizável em diferentes projetos de migração.

Nenhum módulo deverá ser desenvolvido especificamente para um único cliente.

As particularidades de cada migração deverão ser tratadas por meio de:

- arquivos SQL;
- arquivos de configuração;
- regras de normalização;
- parâmetros externos.

O objetivo é evitar duplicação de código e permitir que o mesmo framework seja utilizado em diversos cenários.

---

# 3. Configuração acima de Código

Todas as informações específicas de um cliente deverão estar armazenadas em arquivos externos.

Exemplos:

- credenciais de banco;
- consultas SQL;
- regras de normalização;
- parâmetros de execução.

O código-fonte deverá permanecer genérico e independente do cliente.

---

# 4. Modularidade

O framework deverá ser dividido em módulos independentes.

Cada módulo será responsável por apenas uma etapa do processo de migração.

Exemplo:

```text
Database

↓

Extraction

↓

Discovery

↓

Normalizer

↓

Lookup

↓

Relationship

↓

Validation

↓

Reports
```

Essa divisão facilita manutenção, testes e reutilização.

---

# 5. Responsabilidade Única (Single Responsibility Principle)

Cada módulo deverá possuir apenas uma responsabilidade.

Exemplos:

Database

Responsável apenas pela conexão com o banco.

Normalizer

Responsável apenas pela normalização das categorias.

Lookup

Responsável apenas pela busca da categoria no banco de destino.

Nenhum módulo deverá executar funções pertencentes a outro componente.

---

# 6. Baixo Acoplamento

Os módulos deverão possuir o menor número possível de dependências entre si.

Cada componente deverá conhecer apenas as informações necessárias para executar sua tarefa.

Isso permitirá modificar um módulo sem impactar os demais.

---

# 7. Alta Coesão

As funções de um módulo deverão estar relacionadas ao mesmo domínio de responsabilidade.

Exemplo:

O módulo **Normalizer** conterá apenas regras de normalização.

Não deverá conter consultas SQL, geração de relatórios ou conexão com banco.

---

# 8. Padronização

Todos os módulos deverão seguir um padrão único de desenvolvimento.

Aspectos padronizados:

- nomenclatura de arquivos;
- nomenclatura de funções;
- organização das pastas;
- estrutura dos DataFrames;
- formato dos logs;
- padrão dos relatórios.

A padronização reduz a complexidade do projeto e facilita sua manutenção.

---

# 9. Separação entre Dados e Regras de Negócio

As regras de negócio não deverão estar misturadas com o código responsável pelo processamento.

Exemplo:

As regras de normalização deverão ser definidas em arquivos de configuração ou estruturas específicas, permitindo alterações sem modificar o código-fonte.

---

# 10. Escalabilidade

A arquitetura deverá permitir a inclusão de novas funcionalidades sem necessidade de alterar os módulos existentes.

Exemplos:

- novos tipos de discovery;
- novos bancos de dados;
- novos formatos de relatório;
- novos mecanismos de validação.

---

# 11. Manutenibilidade

O código deverá ser desenvolvido de forma clara e organizada.

Boas práticas:

- funções pequenas;
- nomes descritivos;
- documentação;
- comentários apenas quando agregarem valor;
- reutilização de funções.

O objetivo é facilitar futuras correções e evoluções.

---

# 12. Transparência

Todo o processamento realizado pelo framework deverá ser rastreável.

Cada etapa deverá registrar:

- início;
- fim;
- quantidade de registros processados;
- erros;
- avisos;
- tempo de execução.

Isso permitirá auditoria e identificação de problemas.

---

# 13. Integridade dos Dados

O framework não deverá alterar os dados do banco de origem.

Todo o processamento será realizado em memória utilizando DataFrames do Pandas.

As alterações deverão ocorrer apenas no banco de destino.

---

# 14. Evolução Contínua

A arquitetura deverá permitir que novas funcionalidades sejam adicionadas de forma incremental.

Novos módulos deverão ser incorporados sem necessidade de reescrever o núcleo do framework.

---

# 15. Independência do Cliente

O framework não deverá conter código específico para clientes.

A adaptação para diferentes sistemas deverá ocorrer exclusivamente por meio de:

- consultas SQL;
- arquivos de configuração;
- regras de normalização;
- parâmetros de execução.

Dessa forma, a inclusão de um novo cliente exigirá apenas a criação de novos arquivos de configuração, mantendo o núcleo do framework inalterado.

---

# 16. Qualidade do Código

O desenvolvimento deverá seguir boas práticas de engenharia de software.

Entre elas:

- SOLID;
- DRY (Don't Repeat Yourself);
- KISS (Keep It Simple, Stupid);
- Separation of Concerns;
- Clean Code.

Esses princípios contribuirão para um código mais legível, reutilizável e de fácil manutenção.

---

# 17. Resultado Esperado

A aplicação consistente destes princípios permitirá que o **Migration Framework** seja uma solução reutilizável, modular e preparada para evoluções futuras.

O framework poderá ser utilizado em diferentes projetos de migração apenas alterando os arquivos de configuração e as consultas SQL, preservando o núcleo da aplicação e reduzindo significativamente o esforço necessário para novos clientes.
