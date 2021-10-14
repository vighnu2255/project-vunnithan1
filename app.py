import flask
import os
from myApp import fetch_data
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("Database_Uri")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True)


class Artist_Info(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120))
    artist_id = db.Column(db.String(80))

db.create_all()

'''
@app.route("/signup")
def signup():


@app.route("/signup", methods = ["POST"])
def signup_post():


@app.route("/login")
def login():


@app.route("/login_post", methods = ["POST"])
def login_post():

'''
@app.route("/")
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

app.run(
    host = '0.0.0.0',
    port = int(os.getenv("PORT", 8080))
)