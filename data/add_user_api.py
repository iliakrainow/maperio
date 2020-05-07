import flask
from flask import request
import hashlib
from . import db_session
from . import users

blueprint = flask.Blueprint("add_user_api", __name__, template_folder="templates")


@blueprint.route("/api/add_user", methods=["POST", "GET"])
def add_user():
    if request.method == "POST":
        if get_users(request.form["user"]) == '{}':
            user = users.User()
            user.name = request.form["user"]
            user.hashed_password = hash_object = hashlib.md5(bytes(request.form["hashed_password"], 'utf-8')).hexdigest()
            session = db_session.create_session()
            session.add(user)
            session.commit()
            return {
                "name": request.form["user"],
                "hashed_password": request.form["hashed_password"],
            }
        else:
            return {"error": "Nickname is used"}
    else:
        return {"error": "Method not alowed"}


def get_users(name):
    session = db_session.create_session()
    return (
        "{"
        + ", ".join(
            map(
                lambda x: '"' + x.name + '"' + ': "' + x.hashed_password + '"',
                session.query(users.User).filter(users.User.name == name),
            )
        )
        + "}"
    )
