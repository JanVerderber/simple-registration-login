import hashlib
from models.user import User
from flask import request, make_response, redirect, url_for, render_template

def logout(**params):
    # logout should accept POST only (don't do logout via GET, to avoid pre-fetching issues in browsers)
    if request.method == "POST":
        # get the session token from the cookie
        token = request.cookies.get('my-simple-app-session')

        # delete the session token from the User object
        success, message = User.delete_session(token)

        if success:
            # prepare the response
            response = make_response(redirect(url_for("public.main.login")))

            # remove session cookie
            response.set_cookie('my-simple-app-session', '', expires=0)

            return response
        else:
            params["error_message"] = message
            return render_template("public/auth/error_page.html", **params)
