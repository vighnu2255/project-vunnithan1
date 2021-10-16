import requests
import os
import random
import json
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def id_check(a_id):

    URL_AUTH = "https://accounts.spotify.com/api/token"

    # POST to obtain access token
    authorization_response = requests.post(
        URL_AUTH,
        {
            "grant_type": "client_credentials",
            "client_id": os.getenv("Spotify_Client_ID"),
            "client_secret": os.getenv("Spotify_Client_Secret"),
        },
    )

    response = authorization_response.json()
    access_token = response["access_token"]

    header = {"Authorization": "Bearer {}".format(access_token)}
    params = {"id": a_id}

    ARTIST_URL = f"https://api.spotify.com/v1/artists/{a_id}"

    name_request = requests.get(ARTIST_URL, headers=header, params=params)
    name_data = name_request.json()
    print(name_data)

    try:
        result = name_data["error"]["status"]
        return result
    except KeyError:
        return a_id


def fetch_data(a_id):

    # Spotify Authorization

    URL_AUTH = "https://accounts.spotify.com/api/token"

    # POST to obtain access token
    authorization_response = requests.post(
        URL_AUTH,
        {
            "grant_type": "client_credentials",
            "client_id": os.getenv("Spotify_Client_ID"),
            "client_secret": os.getenv("Spotify_Client_Secret"),
        },
    )

    response = authorization_response.json()
    access_token = response["access_token"]

    header1 = {"Authorization": "Bearer {}".format(access_token)}
    parameter1 = {"market": "US"}

    URL_SPOTIFY = f"https://api.spotify.com/v1/artists/{a_id}/top-tracks"

    spotify_response = requests.get(URL_SPOTIFY, params=parameter1, headers=header1)

    # Obtaining data from Spotify

    spotify_data = spotify_response.json()
    print(spotify_data)

    rand = random.randint(0, 9)

    try:
        song_name = spotify_data["tracks"][rand]["name"]
        song_artist = spotify_data["tracks"][rand]["album"]["artists"][0]["name"]
        song_picture = spotify_data["tracks"][rand]["album"]["images"][1]["url"]
        song_player = spotify_data["tracks"][rand]["preview_url"]
    except KeyError:
        return "Couldn't fetch track details"

    # Genius Authorization

    header2 = {
        "Authorization": "Bearer {}".format(os.getenv("Genius_Client_Access_Token"))
    }
    parameter2 = {"q": song_name + song_artist}
    URL_GENIUS = "https://api.genius.com/search"

    genius_response = requests.get(URL_GENIUS, params=parameter2, headers=header2)

    # Obtaining data from Genius

    genius_data = genius_response.json()
    try:
        lyrics_data = genius_data["response"]["hits"][0]["result"]["url"]
    except KeyError:
        print("Couldn't fetch the lyrics page")

    # Return dictionary with relevant info for webpage
    return {
        "name_song": song_name,
        "artist_name": song_artist,
        "picture_song": song_picture,
        "player": song_player,
        "lyrics_url": lyrics_data,
    }
