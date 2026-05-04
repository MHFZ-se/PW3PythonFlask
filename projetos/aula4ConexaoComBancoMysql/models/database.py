#importando o sqlalchemy
from flask_sqlalchemy import SQLAlchemy
#criando uma instancia do SQLAlchemy
#carregando o SQLAlchemy em uma variavel
db = SQLAlchemy()

#Criando a classe para representar a entidade Games no banco de dados (tabela game)
class Game(db.Model):
    #colunas da tabela
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    
#Metodo construtor 
def __init__(self, titulo, ano, categoria, plataforma,preco,quantidade):
    self.id = id
    self.titulo = titulo
    self.ano = ano
    self.categoria = categoria 
    self.plataforma = plataforma
    self.preco = preco
    self.quantidade = quantidade