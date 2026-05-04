#Importando o render template
# ele serve como o motor para renderizar as paginas
from flask import render_template, request, redirect, url_for

def init_app(app):
    #simulando um banco de dados
    listaGames = [{"titulo": "CS-GO", "ano": 2012, "categoria" : "fps online"}]

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
        #isto pode ser chamado de dicionario ou objeto
        jogo = {'Título': 'Hades', 'Ano': 2019, 'Categoria':'roguelike'}
        #isto é um objeteto, ele assossia as chaves(nomes dos valoress) aos valore
        #
        jogadores = ["Henri", "Herick","Kafka","Zahir","Mafalda"]

        return render_template("games.html",
        #enviando as vars para a pag html
        titulo = titulo,
        ano = ano,
        categoria = categoria,
        jogadores = jogadores,
        jogo = jogo)

    @app.route('/consoles')
    def consoles():
        consoles = ["Nintendo switch", "playstation", "Xbox", "Superblai","Pc"]
        return render_template("consoles.html",
                            consoles=consoles)
    #rota da pagina de cadastro
    @app.route('/cadgames', methods = ["GET","POST"])
    def cadgames():
        # se o metodo da requisição for post
        if request.method == 'POST':
            listaGames.append({
                'titulo': request.form.get('titulo'),
                'ano': request.form.get('ano'),
                'categoria': request.form.get('categoria')})
            return redirect(url_for('cadgames'))
            #recebendo os dados do forulario
        return render_template('cadgames.html',
                               listaGames = listaGames)
    # o arroba faz com que a rota 0 chame a função home