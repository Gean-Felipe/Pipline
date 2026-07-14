#trabalha com os caminhos e arquivos e pastas
from pathlib import Path

# lê os arquivos .yaml arquivo de configuração utilizado pelo framework para armazenar parâmetros da aplicação, como conexões com bancos de dados e regras de processamento, mantendo as configurações separadas do código.
import yaml 

from pathlib import Path
import yaml


class ConfigManager:
    """
    Responsável por carregar todos os arquivos de configuração do framework.
    """

    def __init__(self):
        """
        Inicializa o ConfigManager carregando todos os arquivos
        de configuração necessários para o framework.
        """

        # Define o caminho absoluto da pasta "config" do projeto.
        # Exemplo: C:\projeto\config
        self.base_path = Path(__file__).resolve().parents[2] / "config"

        # Carrega as configurações de conexão com os bancos de dados
        # (origem e destino).
        self.database = self._load_yaml("database.yaml")

        # Carrega as configurações gerais do framework,
        # como parâmetros de execução e comportamento da aplicação.
        self.framework = self._load_yaml("framework.yaml")

        # Carrega as regras utilizadas durante a normalização
        # das categorias extraídas da base de origem.
        self.normalize = self._load_yaml("normalize.yaml")

    def _load_yaml(self, filename: str) -> dict:
        """
        Lê um arquivo YAML e retorna seu conteúdo
        convertido para um dicionário Python.
        """

        # Monta o caminho completo até o arquivo.
        # Exemplo: C:\projeto\config\database.yaml
        file_path = self.base_path / filename

        # Abre o arquivo em modo de leitura utilizando UTF-8.
        with open(file_path, "r", encoding="utf-8") as file:

            # Converte o conteúdo do YAML em um dicionário Python
            # e retorna o resultado para quem chamou o método.
            return yaml.safe_load(file)

if __name__ == "__main__":

    config = ConfigManager()

    print("Banco de dados:")
    print(config.database)

    print("\nFramework:")
    print(config.framework)

    print("\nNormalização:")
    print(config.normalize)
