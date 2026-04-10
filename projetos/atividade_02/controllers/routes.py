from flask import render_template, request, redirect, url_for

def init_app(app):
    
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/lista')
    def lista():
        linguagens = ["fyton","jyton","Hypescript","Portugues","Ingles","Brasileiro","C++++++++","C#"]
        return render_template('lista.html',
                               linguagens = linguagens)

    @app.route('/formulario')
    def formulario():
        return render_template('formulario.html')