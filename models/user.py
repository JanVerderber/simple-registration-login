import bleach
import bcrypt
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    session_token_hash = db.Column(db.String(50))
    session_expiration_date = db.Column(db.DateTime, default=datetime.now)

    @classmethod
    def create(cls, username, password):
        # sanitize username
        username = bleach.clean(username, strip=True)

        # checks if user with this username already exists
        user = cls.query.filter_by(username=username).first()

        if not user:  # if user does not yet exist, create one
            hashed = None
            if password:
                # use bcrypt to hash the password
                hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
                password_hash = hashed.decode('utf8')

                user = cls(username=username, password=password_hash)
                db.session.add(user)
                db.session.commit()

                return True, user, "Success"  # success, user, message
        else:
            return False, user, "User with this email address is already registered. Please go to the " \
                            "Login page and try to log in."

    @classmethod
    def get_users(cls):
        users = cls.query.all()

        return users