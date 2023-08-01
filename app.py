# Imports
import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask

from routes import init_app

# Conexão com o Banco de Dados
config_db = load_dotenv('.env')
mycon = mysql.connector.connect(
    host=os.environ['mysql_host'],
    user=os.environ['mysql_user'],
    password=os.environ['mysql_pass'],
    database=os.environ['mysql_db'],
)


# Instâncias / Configurações
app = Flask(__name__)
init_app(app, mycon)


if __name__ == '__main__':
    app.run(debug=True)