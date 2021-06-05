from flask import Blueprint, render_template
from flask_login import login_required
# from funcoes import projet

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template('geral.html')

@main.route('/task')
@login_required
def profile():
    return render_template('Tasks.html')

@main.route('/collaborators')
@login_required
def collaborators():
    return render_template('colaboradores.html')

# @main.route('/project/')
# @main.route('/project/<nome>')
# @login_required
# def projetoname(nome):
#     projeto = projet( nome)
#     return projeto