import flask
import os
from myApp import fetch_data
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("Database_Uri")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv("Secret_Key")

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True)


class Artist_Info(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120))
    artist_id = db.Column(db.String(80))

db.create_all()


@app.route("/")
def signup():
    return flask.render_templates("signup.html")

@app.route("/", methods = ["POST"])
def signup_post():
    username = flask.request.form.get('s_username')
    user = User(username=username)

    exists = User.query.filter_by(username=user.username) is not None
    if exists:
        flask.redirect(flask.url_for('/login'))
    else:
        db.session.add(user)
        db.commit()

@app.route("/login")
def login():
    return flask.render_templates("login.html")

@app.route("/login_post", methods = ["POST"])
def login_post():
    username = flask.request.form.get('l_username')
    user = User(username=username)
    user_check = User.query.filter_by(username=user.username)
    if user_check.is_authenticated():
        login_user(user_check)
        flask.redirect(flask.url_for('/homepage'))
    else:
        flask.flash("Invalid User Id entered")


@app.route("/homepage")
@login_required
def index():
    data = fetch_data()
    return flask.render_template(
        "index.html",
        name = data["name_song"],
        artist = data["artist_name"],
        image_song = data["picture_song"],
        player = data["player"],
        lyrics_page = data["lyrics_url"]
    )

if __name__ == '__main__':
    app.run(
        debug = True,
        host = '0.0.0.0',
        port = int(os.getenv("PORT", 8080))
    )