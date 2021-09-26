import flask
from myApp1 import fetch_data

app = flask.Flask(__name__)

@app.route("/")

def index():
    data = fetch_data()
    return flask.render_template(
        "index1.html",
        name = data["name_song"],
        artist = data["artist_name"],
        image_song = data["picture_song"],
        player = data["player"],
        lyrics_page = data["lyrics_url"]
    )

app.run(debug = True)