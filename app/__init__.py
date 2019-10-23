from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.config import config_options




db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'





def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.users.routes import users
    from app.main.routes import main
    from app.comments.routes import comments
    from app.pitches.routes import pitches

    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(comments)
    app.register_blueprint(pitches)

    return app