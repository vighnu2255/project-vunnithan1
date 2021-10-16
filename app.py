import flask
import os
import random
from myApp import fetch_data, id_check
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user

app = flask.Flask(__name__)

url = os.getenv("DATABASE_URL") 
if url and url.startswith("postgres://"): 
    url = url.replace("postgres://", "postgresql://", 1) 
app.config["SQLALCHEMY_DATABASE_URI"] = url

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

db.session.query(Artist_Info).delete()
db.session.commit()



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def signup():
    return flask.render_template("signup.html")

@app.route("/", methods = ["POST"])
def signup_post():
    username = flask.request.form.get('s_username')
    user = User(username=username)

    exists = User.query.filter_by(username=user.username).first() 
    if exists:
        return flask.redirect(flask.url_for('welcome'))
    else:
        db.session.add(user)
        db.session.commit()
        return flask.redirect(flask.url_for('login'))


@app.route("/login")
def login():
    return flask.render_template("login.html")

@app.route("/login", methods = ["POST"])
def login_post():
    username = flask.request.form.get('l_username')
    user = User.query.filter_by(username=username).first()

    exists = user
    error = False
    if exists:
        login_user(user)
        return flask.redirect(flask.url_for('welcome'))
    else:
        error = True
        return flask.render_template("login.html", error=error)
        '''
        flask.flash("Invalid User Id entered")
        return flask.redirect(flask.url_for('login'))
        '''

@app.route("/welcome", methods = ["POST"])
@login_required
def welcome_post():
    if flask.request.method == "POST":
        art_name = flask.request.form.get('artist')
        user_artist = Artist_Info(username=current_user.username, artist_id=art_name)
        
        error1 = False
        check = id_check(art_name)
        if check != art_name:
            error1 = True
            return flask.render_template("welcome.html", error1 = error1, error2 = False)
        
        error2 = False
        exists = Artist_Info.query.filter_by(username=user_artist.username, artist_id=art_name).first()
        if exists:
            error2 = True
            return flask.render_template("welcome.html", error1 = False, error2 = error2)
        else:
            db.session.add(user_artist)
            db.session.commit()
            return flask.redirect(flask.url_for('welcome'))

@app.route("/welcome")
@login_required
def welcome():
    return flask.render_template("welcome.html")


@app.route("/homepage")
@login_required
def homepage():
    ids = Artist_Info.query.filter_by(username=current_user.username).all()
    id_list = []
    for el in ids:
        id_list.append(el.artist_id)
    rand = random.randint(0, len(id_list) - 1)
    current_id = id_list[rand]
    data = fetch_data(current_id)
    print(data)
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