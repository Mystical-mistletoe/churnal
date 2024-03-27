
from flask import Flask, url_for
from flask import request
from flask_wtf import FlaskForm
from data import db_session
from flask import render_template
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


def main():

    db_session.global_init("db/blogs.db")
    app.run(debug=True)

if __name__ == '__main__':
    main()











