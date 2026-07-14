# Salvar Alterações no Git

Depois de editar seus arquivos, siga estes passos:

## 1. Adicionar as alterações

```bash
git add .
```

## 2. Salvar as alterações (Commit)

```bash
git commit -m "Descrição das alterações"
```

Exemplos:

```bash
git commit -m "Corrige erro na conexão com banco"
```

```bash
git commit -m "Adiciona módulo de configuração"
```

O **commit** cria um ponto de salvamento no histórico do Git. As alterações ficam registradas localmente no seu computador, mas **ainda não foram enviadas para o GitHub**.

## 3. Enviar para o repositório

```bash
git push
```

---

# Resumo

```bash
git add .
git commit -m "Descrição das alterações"
git push
```

- **`git add .`** → Seleciona os arquivos alterados.
- **`git commit -m "mensagem"`** → Salva as alterações no histórico local do Git.
- **`git push`** → Envia os commits para o repositório remoto (GitHub, GitLab, etc.).
