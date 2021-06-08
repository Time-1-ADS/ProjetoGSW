from enum import unique
from flask_login import UserMixin
from uuid import uuid4

from sqlalchemy.orm import backref

from .init import db

class User(UserMixin, db.Model):
    __tablename__ = 'autenticacao'

    id = db.Column(primary_key=True, default=uuid4,)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    project = db.Column(db.String(255))
    
    roles = db.relationship('Role', backref='User', uselist=False)

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(primary_key=True, default=uuid4,)
    name = db.Column(db.String(100), unique=True)
    user_id = db.Column(db.Interger , db.ForeignKey('User.id'))


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

