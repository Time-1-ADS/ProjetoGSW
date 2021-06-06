from flask import Flask
from flask_login.utils import login_required
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from flask_login import LoginManager
import os

db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://administrador:teste321@dashboard-gsw-fatec.cyrmoymsjutf.sa-east-1.rds.amazonaws.com/myDatabase'


db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

    
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)


from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
