from flask import Flask, render_template, request, url_for
from data import db_session, add_user_api, users
import json
import hashlib
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'



def main():
    db_session.global_init("db/data.sqlite")
    app.register_blueprint(add_user_api.blueprint)
    app.run()

@app.route('/', methods=['GET', 'POST'])
def index():
    global now_user
    if request.method == 'GET':
        return render_template('index.html', style=url_for('static', filename='css/main.css'))
    elif request.method == 'POST':
        print(add_user_api.get_users(request.form["user"]))
        if add_user_api.get_users(request.form["user"]) == '{}':
            user = users.User()
            user.name = request.form["user"].lower()
            user.hashed_password = hashlib.md5(bytes(request.form["hashed_password"], 'utf-8')).hexdigest()

            session = db_session.create_session()
            session.add(user)
            session.commit()
            now_user = request.form["user"]
            return render_template('index.html', style=url_for('static', filename='css/main.css'), text_in_login="OK")
        else:
            now_user = request.form["user"]
            nick = request.form["user"]
            d = dict(json.loads(add_user_api.get_users(nick)))
            if hashlib.md5(bytes(request.form["hashed_password"], 'utf-8')).hexdigest() == str(d[str(nick)]):
                return render_template('index.html', style=url_for('static', filename='css/main.css'), text_in_login="Успешно!")
            else:
                return render_template('index.html', style=url_for('static', filename='css/main.css'), text_in_login="Логин занят, пароль неверный")

@app.route('/api/geolocation')
def geo():
    return render_template('get_geo.html')

@app.route('/game')
def game():
    global now_user
    sess = sessions.Session()
    sess.name = now_user
    sess.time_from = time.time()

    session = db_session.create_session()
    session.add(sess)
    session.commit()
    return 'Здесь будет игра.'


print(__name__)
if __name__ == '__main__':
    main()


'''type="submit"
 action="/api/add_user" method="POST"
'''


