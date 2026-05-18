#Importando o render template
# ele serve como o motor para renderizar as paginas
from flask import render_template, request, redirect, url_for
#importandoo model game e o SQLAlchemy
from models.database import Game,db,Console
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
    
    
    
    @app.route("/estoque-jogos", methods=['GET','POST'])
    @app.route("/estoque-jogo/delete/<int:id>")
    def estoque_jogos(id=None):
        if id:
            game = Game.query.get(id)
            
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque_jogos'))
                #verifincando o tipo da requisião
        if request.method == 'POST':
            #coletando os dados do form
            dados_form = request.form.to_dict()
            newGame = Game(
                dados_form['titulo'],
                dados_form['ano'],
                dados_form['categoria'],
                dados_form['plataforma'],
                dados_form['preco'],
                dados_form['quantidade'],
            )
            #faz uma alteração no banco
            db.session.add(newGame)
            #salva a alteração
            db.session.commit()
            #recarregando a pagina cm as alterações
            return redirect(url_for('estoque_jogos'))
            #selecionando todos os jogos do banco
            #select * from games

        games = Game.query.all()
        return render_template('estoque-jogos.html', games = games)
    
    @app.route("/estoque-consoles", methods=['GET','POST'])
    @app.route("/estoque-consoles/delete/<int:id>")
    def estoque_consoles():
        if id:
            console = Console.query.get(id)
            
            db.session.delete(console)
            db.session.commit()
            return redirect(url_for('estoque_consoles'))
        if request.method == 'POST':
            #coletando os dados do form
            dados_form = request.form.to_dict()
            newConsole = Console(
                dados_form['nome'],
                dados_form['ano'],
                dados_form['fabricante'],
                dados_form['preco'],
                dados_form['quantidade'],
            )
            db.session.add(newConsole)
            db.session.commit()
            return redirect(url_for('estoque_consoles'))
        consoles = Console.query.all()
        return render_template('/estoque-consoles.html')
    