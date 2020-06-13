from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .models import User

# init SQLAlchemy so we can use it later in our models

db = SQLAlchemy()

# flask finds a specific id from user that we have stored

app = Flask(__name__)
app.config.from_object('config')

# added config related info in config.py
# app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


# blueprint for auth routes in our app
from .auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .routes import unauth_routes as routes_blueprint

app.register_blueprint(routes_blueprint)

# blueprint/routes for executives parts of app
from .executives import executives as exec_blueprint

app.register_blueprint(exec_blueprint)

# blueprint/routes for cashier parts of app
from .cashier import cashier as cashier_blueprint

app.register_blueprint(cashier_blueprint)
