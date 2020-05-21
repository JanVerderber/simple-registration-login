from models.user import User
from flask import render_template

def users_list(**params):
    params["users"] = User.get_users()

    return render_template("admin/users/users-list.html", **params)