from flask import Blueprint, render_template


geralapp = Blueprint('geral', __name__, template_folder='templates', static_folder='static')


geralapp.route('/')
def index(page):
    return render_template('index.html')