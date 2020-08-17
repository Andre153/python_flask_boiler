from .model import User
from datetime import datetime as dt
from .. import db


def create_new_user(user_data):
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        created=dt.now()
    )

    db.session.add(new_user)
    db.session.commit()


def get_user_by_id(id):
    return User.query.get(id)


def get_all_users():
    return User.query.all()
