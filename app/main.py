from flask import Blueprint, render_template
from flask_login import login_required
from .funcoes import projet
from werkzeug import secure_filename
import os

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template('geral.html')

@main.route('/task')
@login_required
def tasks():
    return render_template('Tasks.html')

@main.route('/horas')
@login_required
def horas():
    return render_template('dedicatedhours.html')

@main.route('/project/')
@main.route('/project/<nome>')
@login_required
def projetoname(nome):
    projeto = projet( nome)
    return projeto

