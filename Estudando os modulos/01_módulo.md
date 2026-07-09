# ConfigManager

O `ConfigManager` é o primeiro módulo do framework. Sua responsabilidade é carregar todos os arquivos de configuração (`.yaml`) e disponibilizar essas informações para os demais módulos do sistema.

---

# Componentes do ConfigManager

| Código                     | O que faz                                                     |
| -------------------------- | ------------------------------------------------------------- |
| `from pathlib import Path` | Trabalha com caminhos de arquivos e pastas.                   |
| `import yaml`              | Lê arquivos no formato `.yaml`.                               |
| `class ConfigManager`      | Classe responsável por gerenciar as configurações do projeto. |
| `__init__()`               | Executa automaticamente quando a classe é instanciada.        |
| `self.base_path`           | Armazena o caminho da pasta `config`.                         |
| `self.database`            | Carrega o arquivo `database.yaml`.                            |
| `self.framework`           | Carrega o arquivo `framework.yaml`.                           |
| `self.normalize`           | Carrega o arquivo `normalize.yaml`.                           |
| `_load_yaml()`             | Método responsável por ler um arquivo YAML.                   |
| `file_path`                | Monta o caminho completo até o arquivo.                       |
| `open()`                   | Abre o arquivo para leitura.                                  |
| `yaml.safe_load()`         | Converte o conteúdo do YAML em um dicionário Python.          |
| `return`                   | Retorna o conteúdo carregado para quem chamou o método.       |

---

# Fluxo de funcionamento

Sempre visualize o processo abaixo:

```text
database.yaml
        │
        ▼
Path()              → Localiza o arquivo
        │
        ▼
open()              → Abre o arquivo
        │
        ▼
yaml.safe_load()    → Converte o YAML em um dicionário Python
        │
        ▼
return              → Entrega os dados ao ConfigManager
```

---

# Resumo

O `ConfigManager` possui uma única responsabilidade: **carregar as configurações do framework**.

O processo ocorre em quatro etapas:

1. O `Path` localiza o arquivo de configuração.
2. O `open()` abre o arquivo.
3. O `yaml.safe_load()` interpreta o conteúdo e o converte para um dicionário Python.
4. O `return` devolve essas informações para que possam ser utilizadas pelos demais módulos do framework.

Após a criação do `ConfigManager`, nenhum outro módulo precisará abrir arquivos `.yaml` diretamente. Todos utilizar
