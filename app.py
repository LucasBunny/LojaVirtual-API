from flask import Flask
from Routes.routes import init_app
from Models.mysql_connect import Conexao

# Instância de conexão com o Banco de Dados
conexao = Conexao().conection_start()


# Instâncias da Aplicação
app = Flask(__name__)
init_app(app, conexao)


if __name__ == "__main__":
    app.run(debug=True)
