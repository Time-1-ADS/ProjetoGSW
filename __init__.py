from .models import User
from flask import Flask
from flask_login.utils import login_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bpsmtcqxmfmpkk:366912623f7544e3e44dd108d11de2bfd29a1552df3144f6703cae6498622084@ec2-54-225-228-142.compute-1.amazonaws.com:5432/d50t6hunnte85q"
    
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

        
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

