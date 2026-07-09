#trabalha com os caminhos e arquivos e pastas
from pathlib import Path

# lê os arquivos .yaml
import yaml 

class ConfigManager:

  """
    Responsavel por carregar todas as configurações do framework.

  """
  class ConfigManager:
    """
    Responsável por carregar todos os arquivos de configuração do framework.
    """

    def __init__(self):

        # Caminho até a pasta "config" do projeto
        self.base_path = Path(__file__).resolve().parents[2] / "config"

        # Carrega as configurações do banco de dados
        self.database = self._load_yaml("database.yaml")

        # Carrega as configurações gerais do framework
        self.framework = self._load_yaml("framework.yaml")

        # Carrega as regras de normalização
        self.normalize = self._load_yaml("normalize.yaml")


    def _load_yaml(self, filename: str) -> dict:
        """
        Lê um arquivo YAML e retorna seu conteúdo como um dicionário.
        """

        # Monta o caminho completo do arquivo
        file_path = self.base_path / filename

        # Abre o arquivo para leitura
        with open(file_path, "r", encoding="utf-8") as file:

            # Converte o YAML em um dicionário Python
            return yaml.safe_load(file)


