# Problema Atual

> Framework para Descoberta, Normalização e Migração de Categorias para o Edocman

---

# 1. Introdução

O processo atual de migração de categorias é predominantemente manual, exigindo análise individual de cada banco de dados de origem para identificar como as categorias estão armazenadas e como devem ser relacionadas ao sistema de destino.

Cada cliente possui uma estrutura própria, o que torna inviável a utilização de uma única consulta SQL ou de uma única regra de migração para todos os projetos.

Como consequência, grande parte do tempo de uma migração é consumida na identificação, padronização e validação das categorias antes mesmo da criação dos relacionamentos no Edocman.

---

# 2. Cenário Atual

Em um processo típico de migração, o desenvolvedor recebe apenas o banco de dados do cliente.

A partir desse banco é necessário compreender sua estrutura, localizar as tabelas relacionadas aos documentos e identificar onde as categorias estão armazenadas.

Em muitos casos, não existe uma tabela específica de categorias. A informação da categoria está presente na própria tabela de documentos ou distribuída entre diferentes campos, exigindo análise manual para determinar qual informação representa a categoria correta.

Após identificar a categoria, inicia-se um processo de comparação com as categorias existentes no banco de destino, buscando encontrar a correspondência adequada para cada documento.

Somente após essa etapa é possível criar o relacionamento entre documentos e categorias na tabela `GWS_edocman_document_category`.

---

# 3. Fluxo Atual

Atualmente o processo pode ser representado pelo seguinte fluxo:

```text
Recebimento do Banco de Dados
            │
            ▼
Análise da Estrutura
            │
            ▼
Identificação da Tabela de Documentos
            │
            ▼
Identificação da Categoria
            │
            ▼
Normalização Manual
            │
            ▼
Comparação com as Categorias do Edocman
            │
            ▼
Localização do category_id
            │
            ▼
Criação do INSERT
            │
            ▼
Execução da Migração
            │
            ▼
Validação Manual
```

---

# 4. Principais Problemas

O processo atual apresenta diversas limitações.

## Estruturas diferentes

Cada banco de origem possui uma modelagem diferente.

Uma categoria pode estar armazenada:

- em uma tabela própria;
- em uma coluna da tabela de documentos;
- no título do documento;
- no caminho do arquivo (`storage_path`);
- em campos personalizados.

Essa diversidade impede a reutilização direta das consultas SQL.

---

## Processo Manual

Grande parte das atividades depende da análise do desenvolvedor.

Entre elas:

- localizar a categoria;
- interpretar a estrutura da origem;
- comparar categorias;
- validar resultados;
- ajustar inconsistências.

Esse processo aumenta significativamente o tempo de migração.

---

## Falta de Padronização

As categorias apresentam diferenças de nomenclatura entre clientes.

Exemplos:

```text
Ata de Registro de Preço

Ata Registro de Preços

Ata Registro Preço

ATA REGISTRO DE PREÇO

Ata de Registro de Preço 2025
```

Embora representem o mesmo assunto, essas diferenças dificultam a localização automática da categoria correspondente.

---

## Dependência de Conhecimento

Atualmente o processo depende do conhecimento adquirido em migrações anteriores.

Boa parte das regras utilizadas não está documentada, dificultando a manutenção e o treinamento de novos desenvolvedores.

---

## Baixa Reutilização

Cada novo cliente exige adaptações específicas.

Na prática, muitas consultas SQL e regras de transformação precisam ser recriadas, aumentando o esforço necessário para cada projeto.

---

## Alto Tempo de Execução

Uma parcela significativa do tempo de migração é consumida em atividades que poderiam ser automatizadas.

Entre elas:

- análise da origem;
- identificação das categorias;
- normalização;
- comparação;
- validação.

---

# 5. Impactos

Os problemas atuais geram diversos impactos.

## Técnicos

- Código pouco reutilizável;
- Grande quantidade de regras específicas;
- Alto custo de manutenção;
- Baixa escalabilidade.

---

## Operacionais

- Migrações demoradas;
- Retrabalho frequente;
- Maior possibilidade de erro humano;
- Processo dependente de validações manuais.

---

## Organizacionais

- Dependência de conhecimento individual;
- Dificuldade para documentar regras;
- Curva de aprendizado elevada para novos integrantes da equipe.

---

# 6. Necessidade da Solução

Diante desse cenário, torna-se necessário desenvolver um framework capaz de automatizar as etapas repetitivas da migração.

A solução deverá permitir que o desenvolvedor concentre seus esforços na definição das regras específicas de cada cliente, enquanto o framework executa automaticamente as tarefas de extração, normalização, localização da categoria e criação dos relacionamentos.

Com essa abordagem será possível reduzir significativamente o tempo necessário para cada migração, aumentar a confiabilidade dos resultados e reutilizar o mesmo núcleo de processamento em diferentes projetos.

---

# 7. Objetivo da Mudança

A proposta do Migration Framework é substituir um processo manual por um fluxo automatizado, padronizado e reutilizável.

Fluxo atual:

```text
Banco de Origem
        │
        ▼
Análise Manual
        │
        ▼
Comparação Manual
        │
        ▼
Normalização Manual
        │
        ▼
Criação Manual do Relacionamento
        │
        ▼
Validação Manual
```

Fluxo proposto:

```text
Banco de Origem
        │
        ▼
Extração Automática
        │
        ▼
Discovery
        │
        ▼
Normalização
        │
        ▼
Busca da Categoria
        │
        ▼
Criação do Relacionamento
        │
        ▼
Validação
        │
        ▼
Relatórios
```

---

# 8. Resultado Esperado

Com a implantação do framework espera-se:

- reduzir significativamente o tempo de migração;
- eliminar atividades repetitivas;
- padronizar o processo entre diferentes clientes;
- reutilizar regras de negócio;
- reduzir erros de classificação;
- facilitar a manutenção do código;
- permitir a evolução contínua do framework.

---

# Resumo

Atualmente, a maior dificuldade das migrações não está na inserção dos dados no banco de destino, mas na identificação e padronização das categorias presentes na base de origem.

O **Migration Framework** surge para automatizar esse processo, transformando uma atividade manual e dependente de conhecimento específico em um fluxo padronizado, reutilizável e escalável.
