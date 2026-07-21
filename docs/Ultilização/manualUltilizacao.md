# Manual de Utilização

## Objetivo

Este manual tem como objetivo orientar a utilização do Framework de Migração de Dados.

Ao final deste documento, o usuário será capaz de:

- Configurar uma nova migração.
- Conectar ao banco de origem.
- Conectar ao banco de destino.
- Executar os scripts de extração.
- Migrar os dados.
- Validar o resultado da migração.

---

# Público-alvo

Este manual é destinado a:

- Analistas de Banco de Dados;
- Analistas de Migração;
- Desenvolvedores responsáveis pela execução de migrações.

---

# Pré-requisitos

Antes de utilizar o framework, verifique se os seguintes requisitos foram atendidos.

## Software

- Python 3.12 ou superior
- Git
- Ambiente virtual (venv)

## Bibliotecas

Instale todas as dependências do projeto.

```bash
pip install -r requirements.txt
```

---

# Estrutura do Projeto

O framework deve possuir a seguinte estrutura.

```text
migration_framework/

config/

docs/

logs/

sql/

src/

tests/

README.md

requirements.txt
```

---

# Fluxo Geral da Migração

Toda migração segue o mesmo fluxo.

```text
Receber Banco de Dados

↓

Configurar database.yaml

↓

Criar Scripts SQL

↓

Executar o Framework

↓

Validar Dados

↓

Gerar Relatório
```

---

# Etapas da Migração

A utilização do framework é dividida em etapas.

## Etapa 1 – Receber o Banco de Dados

Obtenha o banco de dados do sistema de origem.

O banco poderá ser fornecido em diferentes formatos, como:

- Dump SQL;
- Backup;
- Banco local;
- Servidor remoto.

---

## Etapa 2 – Restaurar o Banco

Caso o banco seja fornecido em formato de dump, restaure-o em um servidor compatível.

Exemplo:

MySQL

MariaDB

PostgreSQL

SQL Server

---

## Etapa 3 – Configurar o Banco de Origem

Edite o arquivo:

```text
config/database.yaml
```

Preencha as informações do banco de origem.

```yaml
source:

host:

port:

database:

username:

password:
```

---

## Etapa 4 – Configurar o Banco de Destino

No mesmo arquivo, informe os dados do banco de destino.

```yaml
destination:

host:

port:

database:

username:

password:
```

---

## Etapa 5 – Criar os Scripts SQL

Os scripts responsáveis pela extração devem ser armazenados em:

```text
sql/extract/
```

Exemplo:

```text
attachments.sql

categories.sql

documents.sql
```

---

## Etapa 6 – Executar a Migração

Execute o framework.

```bash
python main.py
```

Durante a execução o framework irá:

- Ler as configurações.
- Abrir conexão com os bancos.
- Executar os scripts SQL.
- Carregar os dados em DataFrames.
- Normalizar os dados.
- Inserir os registros no destino.
- Registrar logs.

---

## Etapa 7 – Validar a Migração

Após a conclusão da execução, verifique:

- Quantidade de categorias.
- Quantidade de documentos.
- Quantidade de anexos.
- Relacionamentos.
- Logs de erro.

---

# Logs

Os arquivos de log serão armazenados em:

```text
logs/
```

Esses arquivos auxiliam na identificação de erros durante a migração.

---

# Problemas Comuns

## Não foi possível conectar ao banco.

Verifique:

- Host;
- Porta;
- Usuário;
- Senha;
- Firewall;
- Permissões.

---

## Script SQL apresentou erro.

Verifique:

- Nome das tabelas;
- Nome das colunas;
- Compatibilidade com o banco de origem.

---

## Migração concluída com sucesso

Ao término da migração, recomenda-se validar todas as informações importadas antes da disponibilização do sistema ao cliente.
