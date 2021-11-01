import flask
import os
import random
import json
from myApp import fetch_data, id_check
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    current_user,
)

app = flask.Flask(__name__, static_folder="./build/static")
# This tells our Flask app to look at the results of `npm build` instead of the
# actual files in /templates when we're looking for the index page file. This allows
# us to load React code into a webpage. Look up create-react-app for more reading on
# why this is necessary.
bp = flask.Blueprint("bp", __name__, template_folder="./build")

url = os.getenv("DATABASE_URL")
if url and url.startswith("postgres://"):
    url = url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = url

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("Secret_Key")

"""
login_manager = LoginManager()
login_manager.init_app(app)
"""

db = SQLAlchemy(app)

# Table to hold usernames for user validation
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)


# Table to hold favorite artist ids
class Artist_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    artist_id = db.Column(db.String(80))


db.create_all()


@bp.route("/index")
def index():

    DATA = fetch_data("6eUKZXaKkcviH0Ku9w2n3V")
    data = json.dumps(DATA)
    return flask.render_template(
        "index.html",
        data=data,
    )


app.register_blueprint(bp)

"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route('/signup')
def signup():
	return flask.render_template("signup.html")

@app.route('/signup', methods=["POST"])
def signup_post():
	username = flask.request.form.get("s_username")
    user = User(username=username)
    # Check to see if username already exists
    exists = User.query.filter_by(username=user.username).first()
    if exists:
        return flask.redirect(flask.url_for("index"))
    else:
        db.session.add(user)
        db.session.commit()
        return flask.redirect(flask.url_for("login"))

@app.route('/login')
def login():
    return flask.render_template("login.html")

@app.route('/login', methods=["POST"])
def login_post():
	username = flask.request.form.get("l_username")
    user = User.query.filter_by(username=username).first()

    # Check to see if username is registered
    exists = user
    error = False
    if exists:
        login_user(user)
        return flask.redirect(flask.url_for("index"))
    else:
        error = True
        return flask.render_template("login.html", error=error)

@app.route('/save', methods=["POST"])
def save():
    ...


@app.route('/')
def main():
	...
"""

def check_ids(id_list):
    

app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8081)),
)
