# comentario
# para importar flask
from flask import Flask, render_template # é a ferramenta encarregada de renderizar paginas htnl

#carregando o flask em uma variavel

app = Flask(__name__, template_folder='views')#uma abreviação que facilta, name é uma variavel que serve como o arquivo atual
#template_folder define o arquivo da busca
# __name__ é uma variavel do pyton que tem o nome do módulo atual

#criando a rota p do website (importante!)
@app.route('/')# a rota principal, ponto zero, onde tudo começa

# def funciona para poder criar funções
def home():
    return render_template("index.html")

@app.route('/games')
def games():
    # criando variaveis q passam infos de jogo
    titulo = "Hades"
    ano = 2019
    categoria = "Roguelike" 
    jogadores = ["Henri", "Herick","Kafka","Zahir","Mafalda"]

    return render_template("games.html",
    #enviando as vars para a pag html
    titulo = titulo,
    ano = ano,
    categoria = categoria,
    jogadores = jogadores)

@app.route('/consoles')
def consoles():
    consoles = ["Nintendo switch", "playstation", "Xbox", "Superblai","Pc"]
    return render_template("consoles.html",
                           consoles=consoles)
# o arroba faz com que a rota 0 chame a função home
#iniciando um server web local, como apache o xampp
if __name__ == '__main__':# main seria o arquivo principal, tipo o index
    app.run(debug=True)#.run inicia um servidor, modo de depuração = verdadeiro
    # Caso app.py for o arquivo principal o servidor se inicia