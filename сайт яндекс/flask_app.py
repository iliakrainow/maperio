from flask import Flask, render_template, request, url_for
from data import db_session, add_user_api, users
import json
import hashlib
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'



def main():
    db_session.global_init("db/data.sqlite")
    app.register_blueprint(add_user_api.blueprint)
    app.run()

@app.route('/', methods=['GET', 'POST'])
def index():
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
            return render_template('index.html', style=url_for('static', filename='css/main.css'), text_in_login="OK")
        else:
            nick = request.form["user"]
            d = dict(json.loads(add_user_api.get_users(nick)))
            if hashlib.md5(bytes(request.form["hashed_password"], 'utf-8')).hexdigest() == str(d[str(nick)]):
                return render_template('index.html', style=url_for('static', filename='css/main.css'), text_in_login="Успешно!")
            else:
                return str(hash(request.form["hashed_password"])) + ' ' + str(d[str(nick)])
                return render_template('index.html', style=url_for('static', filename='css/main.css'), text_in_login="Логин занят, пароль неверный")

@app.route('/api/geolocation')
def geo():
    return render_template('get_geo.html')



@app.route('/store', methods=['GET', 'POST'])
def store():
    if request.method == 'GET':
        return render_template('store.html', style=url_for('static', filename='css/main.css'))
    elif request.method == 'POST':
        print(request.form["count"])
        sign = ['user', 'RUB', 'донат', str(request.form["count"]), '546db56179690bff7ecc07e9b75d0f54']
        sign = hashlib.sha256(bytes('{up}'.join(sign), 'utf-8')).hexdigest()
        payload = {'sum': request.form["count"], 'desc': 'донат', 'account': 'user', 'currency': 'RUB', 'signature': sign}
        r = requests.get('https://unitpay.ru/pay/258091-9c3d7', params=payload)
        return f'''{r.url}
        <META HTTP-EQUIV="REFRESH" CONTENT="1; URL={r.url}>'''


if __name__ == '__main__':
    main()
