# comentario
# para importar flask
from flask import Flask, render_template # é a ferramenta encarregada de renderizar paginas htnl
from controllers import routes
#carregando o flask em uma variavel
#importando o py mysql
import pymysql

from models.database import db, Game


app = Flask(__name__, template_folder='views')#uma abreviação que facilta, name é uma variavel que serve como o arquivo atual
#template_folder define o arquivo da busca
# __name__ é uma variavel do pyton que tem o nome do módulo atual

#Definindo o nome do banco de dados
DB_NAME = 'thegames'

#passando o nome do banco para o flask ]

app.config['DATABASE_NAME'] = DB_NAME

# Passando o endereço do banco para o flask

app.config['SQLALCHEMY_DATABASE_URI']= f'mysql://root@localhost/{DB_NAME}'


# Enviando a variavel app para as rotas
routes.init_app(app)

# Iniciando o servidor web
if __name__ == '__main__':
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass = pymysql.cursors.DictCursor)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print("O Banco de Dados foi criado com sucesso!")
    except Exception as error:
        print(f"Erro ao criar o Banco de Dados: {error}")
    finally:
        connection.close()
        
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
        
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#enviando a variavel app (flask) para as rotas
routes.init_app(app)
#iniciando um server web local, como apache o xampp
if __name__ == '__main__':# main seria o arquivo principal, tipo o index
    app.run(debug=True, port="8081")#.run inicia um servidor, modo de depuração = verdadeiro
    # Caso app.py for o arquivo principal o servidor se inicia