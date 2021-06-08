from flask import Blueprint, render_template, redirect, url_for
from flask.globals import request
from flask_login import login_required
from werkzeug.utils import redirect
from .funcoes import projet
from werkzeug import secure_filename
from .init import app
import os

main = Blueprint('main', __name__, static_folder= 'static')

upload_folder = 'static/files'

app.config['upload_folder'] = upload_folder

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

# @main.route('/upload', methods = ['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file[]']
#         if file:
#             filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['upload_folder'], filename))
#         return redirect(url_for('main.index'))


@ app.route ('/uploader', methods = ['GET', 'POST']) 
def upload_file () : 
    if request.method == 'POST' :       
        f = request.files [ 'file' ]       
        f.save (secure_filename (f.filename)) 
        return redirect(url_for('main.index'))