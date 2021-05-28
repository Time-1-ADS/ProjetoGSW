from flask import Flask, redirect, url_for, render_template
import os
from funcoes import projet



app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('geral.html')

@app.route('/project/')
@app.route('/project/<nome>')
def projetoname(nome):
    projeto = projet( nome)
    return projeto


@app.route('/collaborators')
def collaborators():
    return render_template('colaboradores.html')


@app.route('/task')
def tasks():
    return render_template('Tasks.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)