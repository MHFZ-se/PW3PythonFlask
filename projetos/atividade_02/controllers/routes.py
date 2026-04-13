from flask import render_template, request, redirect, url_for

def init_app(app):
    
    listaLinguagem = [{"linguagem" : "C", "porque" : "Legal", "resposta" : "A efemera existência"}]
    
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/lista')
    def lista():
        linguagens = ["fyton","jyton","Hypescript","Portugues","Ingles","Brasileiro","C++++++++","C#"]
        return render_template('lista.html',
                               linguagens = linguagens)

    @app.route('/formulario', methods = ["GET","POST"])
    def formulario():
        if request.method == 'POST':
            listaLinguagem.append({
                'linguagem': request.form.get('linguagem'),
                'porque': request.form.get('porque'),
                'resposta': request.form.get('resposta')})
            return redirect(url_for('formulario'))
        
        return render_template('formulario.html', listaLinguagem = listaLinguagem)