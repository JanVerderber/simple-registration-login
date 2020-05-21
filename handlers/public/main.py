import bcrypt
from flask import request, render_template, redirect, url_for
from models.user import User

def login(**params):
    if request.method == "GET":
        return render_template('public/main/index.html', **params)

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:
            # checks if user with this username and password exists
            user = User.query.filter_by(username=username).first()

            if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
                return redirect(url_for("admin.users.users_list"))
            else:
                return render_template("public/auth/registration.html", **params)
