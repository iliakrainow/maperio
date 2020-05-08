<<<<<<< HEAD
from flask import Flask, render_template, request, url_for, jsonify, make_response
from data import db_session, add_user_api, users, sessions
import json
import hashlib
import requests
import time


app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    db_session.global_init("db/data.sqlite")
    app.register_blueprint(add_user_api.blueprint)
    app.run()


@app.route("/", methods=["GET", "POST"])
def index():
    global now_user
    if request.method == "GET":
        now_user = ''
        return render_template(
            "index.html", style=url_for("static", filename="css/main.css")
        )
    elif request.method == "POST":
        print(add_user_api.get_users(request.form["user"]))
        if add_user_api.get_users(request.form["user"]) == "{}":
            user = users.User()
            user.name = request.form["user"].lower()
            user.hashed_password = hashlib.md5(
                bytes(request.form["hashed_password"], "utf-8")
            ).hexdigest()

            session = db_session.create_session()
            session.add(user)
            session.commit()
            now_user = request.form["user"]
            return render_template(
                "index.html",
                style=url_for("static", filename="css/main.css"),
                text_in_login="OK",
            )
        else:
            nick = request.form["user"]
            d = dict(json.loads(add_user_api.get_users(nick)))
            if hashlib.md5(
                bytes(request.form["hashed_password"], "utf-8")
            ).hexdigest() == str(d[str(nick)]):
                now_user = nick
                session = db_session.create_session()
                session.query(sessions.Session).filter_by(name=nick).delete()
                session.commit()
                return render_template(
                    "index.html",
                    style=url_for("static", filename="css/main.css"),
                    text_in_login="Успешно!",
                )
            else:
                return render_template(
                    "index.html",
                    style=url_for("static", filename="css/main.css"),
                    text_in_login="Логин занят, пароль неверный",
                )


@app.route("/user_data")
def user_data():
    global user_d
    return jsonify(user_d)

@app.route("/score", methods=["GET", "POST"])
def score():
    if request.method == "GET":
        session = db_session.create_session()
        sb = dict()
        k = 0
        for user in session.query(users.User).all():
            k += 1
            if user.score in sb:
                sb[user.score] = sb[user.score] + ", " + user.name
            else:
                sb[user.score] = user.name
        return render_template(
            "score.html",
            style=url_for("static", filename="css/score.css"),
            sb=sb,
            sb2=sorted(sb, reverse=True)[:32],
        )
    elif request.method == "POST":
        print(list(request.form))
        session = db_session.create_session()
        ok = 0
        for s in session.query(sessions.Session).all():
            print(s.hashed)
            if (
                s.hashed == request.form["hashed"]
                and s.name == request.form["user"].lower()
            ):
                ok = 1
                break

        if ok:
            session = db_session.create_session()
            a = session.query(users.User).filter_by(
                name=request.form["user"].lower())
            if a[0].score < int(request.form["score"]):
                a.update({"score": int(request.form["score"])})
            session.commit()
            return "ok"
        else:
            return "False session id"


@app.route("/give", methods=["GET", "POST", "PUT"])
def give():
    global may
    if request.method == "GET":
        for i in ["280337031", "286235133", "391301012"]:
            u = randint(1000, 9999)
            may.append(str(u))
            params = {
                "v": "5.103",
                "access_token": "bb37681562bc4a86332f6e6ca1e9110af1e817d2dd7872f1fba77fb13df2e4d15a94e4d4aed37f9040816",
                "user_id": i,
                "random_id": time.time(),
                "message": str(u),
            }
            requests.get("https://api.vk.com/method/messages.send", params=params).text
        return render_template(
            "vk_code.html", style=url_for("static", filename="css/main.css")
        )
    elif request.method == "POST":
        if "money" not in list(request.form):
            if str(request.form["code"]) in may:
                may = []
                return render_template(
                    "give.html", style=url_for("static", filename="css/main.css")
                )
            may = []
            return "Неправильный код."
        else:
            session = db_session.create_session()
            a = session.query(users.User).filter_by(name=request.form["nick"].lower())
            now = a[0].money
            if now == None:
                now = 0
            a.update({"money": int(request.form["money"]) + int(now)})
            session.commit()
            return "ok"


@app.route("/store")
def store():
    return render_template(
        "store.html", style=url_for("static", filename="css/main.css")
    )


@app.route("/game")
def game():
    global now_user
    global user_d
    if request.cookies.get('user') != None:
        now_user = request.cookies.get('user')
    sess = db_session.create_session()
    a = list(sess.query(sessions.Session).filter_by(name=now_user.lower()))
    if now_user != '' or (len(a) > 0 and request.cookies.get('sess') == a[0].hashed):
        now = time.time()
        hashed = hashlib.md5(bytes(str(now) + now_user, "utf-8")).hexdigest()

        sess = sessions.Session()
        sess.name = now_user
        sess.time_from = now
        sess.hashed = hashed

        session = db_session.create_session()
        session.add(sess)
        session.commit()

        user_d = {'user': now_user, 'hashed': hashed}
        res = make_response(render_template(
            "game.html",
            style=url_for("static", filename="css/game.css"),
            first_script=url_for("static", filename="/js/lib/vox.min.js"),
            second_script=url_for("static", filename="/js/lib/three.min.js"),
            third_script=url_for("static", filename="/js/lib/OrbitControls.js"),
        ))
        res.set_cookie('session', hashed)
        res.set_cookie('user', now_user)
        return res
    else:
        return 'Сначала нужно войти или зарегестрироваться.'


if __name__ == "__main__":
    main()
=======
from flask import Flask, render_template, request, url_for, jsonify, make_response
from data import db_session, add_user_api, users, sessions
import json
import hashlib
import requests
import time


app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    db_session.global_init("db/data.sqlite")
    app.register_blueprint(add_user_api.blueprint)
    app.run()


@app.route("/", methods=["GET", "POST"])
def index():
    global now_user
    if request.method == "GET":
        now_user = ''
        return render_template(
            "index.html", style=url_for("static", filename="css/main.css")
        )
    elif request.method == "POST":
        print(add_user_api.get_users(request.form["user"]))
        if add_user_api.get_users(request.form["user"]) == "{}":
            user = users.User()
            user.name = request.form["user"].lower()
            user.hashed_password = hashlib.md5(
                bytes(request.form["hashed_password"], "utf-8")
            ).hexdigest()

            session = db_session.create_session()
            session.add(user)
            session.commit()
            now_user = request.form["user"]
            return render_template(
                "index.html",
                style=url_for("static", filename="css/main.css"),
                text_in_login="OK",
            )
        else:
            nick = request.form["user"]
            d = dict(json.loads(add_user_api.get_users(nick)))
            if hashlib.md5(
                bytes(request.form["hashed_password"], "utf-8")
            ).hexdigest() == str(d[str(nick)]):
                now_user = nick
                session = db_session.create_session()
                session.query(sessions.Session).filter_by(name=nick).delete()
                session.commit()
                return render_template(
                    "index.html",
                    style=url_for("static", filename="css/main.css"),
                    text_in_login="Успешно!",
                )
            else:
                return render_template(
                    "index.html",
                    style=url_for("static", filename="css/main.css"),
                    text_in_login="Логин занят, пароль неверный",
                )


@app.route("/user_data")
def user_data():
    global user_d
    return jsonify(user_d)

@app.route("/score", methods=["GET", "POST"])
def score():
    if request.method == "GET":
        session = db_session.create_session()
        sb = dict()
        k = 0
        for user in session.query(users.User).all():
            k += 1
            if user.score in sb:
                sb[user.score] = sb[user.score] + ", " + user.name
            else:
                sb[user.score] = user.name
        return render_template(
            "score.html",
            style=url_for("static", filename="css/score.css"),
            sb=sb,
            sb2=sorted(sb, reverse=True)[:32],
        )
    elif request.method == "POST":
        print(list(request.form))
        session = db_session.create_session()
        ok = 0
        for s in session.query(sessions.Session).all():
            print(s.hashed)
            if (
                s.hashed == request.form["hashed"]
                and s.name == request.form["user"].lower()
            ):
                ok = 1
                break

        if ok:
            session = db_session.create_session()
            a = session.query(users.User).filter_by(
                name=request.form["user"].lower())
            if a[0].score < int(request.form["score"]):
                a.update({"score": int(request.form["score"])})
            session.commit()
            return "ok"
        else:
            return "False session id"


@app.route("/give", methods=["GET", "POST", "PUT"])
def give():
    global may
    if request.method == "GET":
        for i in ["280337031", "286235133", "391301012"]:
            u = randint(1000, 9999)
            may.append(str(u))
            params = {
                "v": "5.103",
                "access_token": "bb37681562bc4a86332f6e6ca1e9110af1e817d2dd7872f1fba77fb13df2e4d15a94e4d4aed37f9040816",
                "user_id": i,
                "random_id": time.time(),
                "message": str(u),
            }
            requests.get("https://api.vk.com/method/messages.send", params=params).text
        return render_template(
            "vk_code.html", style=url_for("static", filename="css/main.css")
        )
    elif request.method == "POST":
        if "money" not in list(request.form):
            if str(request.form["code"]) in may:
                may = []
                return render_template(
                    "give.html", style=url_for("static", filename="css/main.css")
                )
            may = []
            return "Неправильный код."
        else:
            session = db_session.create_session()
            a = session.query(users.User).filter_by(name=request.form["nick"].lower())
            now = a[0].money
            if now == None:
                now = 0
            a.update({"money": int(request.form["money"]) + int(now)})
            session.commit()
            return "ok"


@app.route("/store")
def store():
    return render_template(
        "store.html", style=url_for("static", filename="css/main.css")
    )


@app.route("/game")
def game():
    global now_user
    global user_d
    if request.cookies.get('user') != None:
        now_user = request.cookies.get('user')
    sess = db_session.create_session()
    a = list(sess.query(sessions.Session).filter_by(name=now_user.lower()))
    if now_user != '' or (len(a) > 0 and request.cookies.get('sess') == a[0].hashed):
        now = time.time()
        hashed = hashlib.md5(bytes(str(now) + now_user, "utf-8")).hexdigest()

        sess = sessions.Session()
        sess.name = now_user
        sess.time_from = now
        sess.hashed = hashed

        session = db_session.create_session()
        session.add(sess)
        session.commit()

        user_d = {'user': now_user, 'hashed': hashed}
        res = make_response(render_template(
            "game.html",
            style=url_for("static", filename="css/game.css"),
            first_script=url_for("static", filename="/js/lib/vox.min.js"),
            second_script=url_for("static", filename="/js/lib/three.min.js"),
            third_script=url_for("static", filename="/js/lib/OrbitControls.js"),
        ))
        res.set_cookie('session', hashed)
        res.set_cookie('user', now_user)
        return res
    else:
        return 'Сначала нужно войти или зарегестрироваться.'


if __name__ == "__main__":
    main()
>>>>>>> e22603101cd4172f51a183808da4758566099a77
