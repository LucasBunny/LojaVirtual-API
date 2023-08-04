import os
import mysql.connector
from dotenv import load_dotenv

# Coleta as configurações do Banco de Dados no .env
config_db = load_dotenv(".env")


# Classe que executa conexao com o Banco de Dados
class Conexao:
    host = os.environ["mysql_host"]
    user = os.environ["mysql_user"]
    password = os.environ["mysql_pass"]
    database = os.environ["mysql_db"]

    def conection_start(self):
        mycon = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        return mycon
