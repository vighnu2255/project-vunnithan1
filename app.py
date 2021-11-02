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


login_manager = LoginManager()
login_manager.init_app(app)


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

    # artist id list to hold all artists for a specific user
    ids = Artist_Info.query.filter_by(username=current_user.username).all()
    id_list = []
    # Loop to append all relevant ids
    for el in ids:
        id_list.append(el.artist_id)
    rand = random.randint(0, len(id_list) - 1)
    # Choosing a random artist from the list
    current_id = id_list[rand]
    # Fetching song data
    DATA = fetch_data(current_id)
    data = json.dumps(DATA)
    return flask.render_template(
        "index.html",
        data=data,
    )


app.register_blueprint(bp)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def signup():
    return flask.render_template("signup.html")


@app.route("/", methods=["POST"])
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


@app.route("/login")
def login():
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
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


@app.route("/save", methods=["POST"])
def save():
    removed_ids = []
    curr_user = current_user.username

    react_response = request.json
    print(react_response)
    artist_id_react = react_response["artists"]
    artist_id_react = check_ids(artist_id_react)

    db_artist_ids = get_all_records(curr_user)
    for record in artist_id_react:
        if record not in db_artist_ids:
            db_artist_ids.append(record)

    for record in db_artist_ids:
        if record not in artist_id_react:
            removed_ids.append(record)

    delete_records(removed_ids, curr_user)

    rem_ids = Artist_Info.query.filter_by(username=username).all()
    rem_id_list = []
    for id in rem_ids:
        rem_id_list.append(id.artist_id)

    rand = random.randint(0, len(rem_id_list) - 1)
    current_id = rem_id_list[rand]
    DATA = fetch_data(current_id)
    data = json.dumps(DATA)

    return jsonify(data)
    """
    return jsonify(
        {
            "artist_id": rem_id_list,
            "name_song": song_name,
            "artist_name": song_artist,
            "picture_song": song_picture,
            "player": song_player,
            "lyrics_url": lyrics_data,
        }
    )
    """


def check_ids(id_list):
    for id in id_list:
        if id_check(id) == 400:
            list(filter(lambda a: a != id, id_list))
    return id_list


def get_all_records(username):
    records = Artist_Info.query.filter_by(username=username).all()
    record_list = []
    for record in records:
        record_list.append(record.artist_id)
    return record_list


def add_records(newList, username):
    for record in newList:
        artist_record = Artist_Info(username=username, artist_id=record)
        db.session.add(artist_record)
        db.session.commit()


def delete_records(newList, username):
    for record in newList:
        db.session.query(Artist_Info).filter_by(
            username=username, artist_id=record
        ).delete()
        db.session.commit()


app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8081)),
)
