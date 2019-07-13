from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from pyapp.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
loginManager = LoginManager()
loginManager.login_view = 'users.login'  # redirects to login page if not logged in when login_required decorator is
# used
loginManager.login_message_category = 'info'

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    loginManager.init_app(app)
    mail.init_app(app)

# Blueprint registration

    from pyapp.users.routes import users
    from pyapp.main.routes import main
    from pyapp.errors.handlers import errors
    from pyapp.items.routes import items

    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(items)

    return app


