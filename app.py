from flask import Flask
from models.user import db
from handlers.admin import users
from handlers.public import main as public_main, auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_database.db'
db.init_app(app)
with app.app_context():
    db.create_all()

# PUBLIC URLS

# HOME PAGE (LOGIN)
app.add_url_rule(rule="/", endpoint="public.main.login", view_func=public_main.login, methods=["GET", "POST"])

# REGISTRATION
app.add_url_rule(rule="/registration", endpoint="public.auth.registration", view_func=auth.registration, methods=["GET", "POST"])


# PRIVATE URLS

# USERS LIST (NEEDS TO BE LOGGED IN)
app.add_url_rule(rule="/admin/users", endpoint="admin.users.users_list", view_func=users.users_list,
                 methods=["GET"])