from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask.helpers import flash
from flask_user import roles_required
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash, Unauthorized
from .models import User, Role, UserRoles
from .init import db
import email_validator


auth = Blueprint('auth', __name__)



@auth.route('/login')
def login():
    return render_template('Login.html')


@auth.route('/signup')
#@login_required
#@roles_required('Administrador')
def signup():
    return render_template('cadastro.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')


    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user)

    return redirect(url_for('main.index'))


@auth.route('/signup', methods = ['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    project = request.form.get('project')
    role = request.form.get('cargo')
    db.create_all()

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email já cadastrado')
        return redirect(url_for('auth.signup'))

    def_role = Role(name=role)
    
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), project=project)
    new_user.roles = [def_role]
    db.session.add(new_user)
    db.session.commit()
    

    return redirect(url_for('main.index'))