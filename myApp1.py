import requests
import os 
import random
import json
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def fetch_data():
    
    #Spotify Authorization

    URL_AUTH = "https://accounts.spotify.com/api/token"
    
    #POST to obtain access token
    authorization_response = requests.post(URL_AUTH, {
        "grant_type": 'client_credentials',
        "client_id": os.getenv("Spotify_Client_ID"),
        "client_secret": os.getenv("Spotify_Client_Secret")
    })

    response = authorization_response.json()
    access_token = response["access_token"]

    header1 = {
        "Authorization" : "Bearer {}".format(access_token)
    }
    parameter1 = {
        "market" : "US"
    }

    #Artist ids of TheWeekend, Travis Scott, Ed Sheeran
    id_list =["1Xyo4u8uXC1ZmMpatF05PJ", "0Y5tJX1MQlPlqiwlOH1tJY","6eUKZXaKkcviH0Ku9w2n3V"]
    rand_num1 = random.randint(0,2)
    
    #Randon id chosen
    id = id_list[rand_num1]

    URL_SPOTIFY = f"https://api.spotify.com/v1/artists/{id}/top-tracks"

    spotify_response = requests.get(URL_SPOTIFY, params = parameter1, headers = header1)

    #Obtaining data from Spotify

    spotify_data = spotify_response.json()

    rand = random.randint(0,9)

    try:
        song_name = spotify_data["tracks"][rand]["name"]
        song_artist = spotify_data["tracks"][rand]["album"]["artists"][0]["name"]
        song_picture = spotify_data['tracks'][rand]['album']['images'][1]['url']
        song_player = spotify_data['tracks'][rand]['preview_url']
    except KeyError:
        print("Couldn't fetch track details")

    #Genius Authorization

    header2 = {
        "Authorization" : "Bearer {}".format(os.getenv("Genius_Client_Access_Token"))
    }
    parameter2 = {
        "q" : song_name + song_artist
    }
    URL_GENIUS = "https://api.genius.com/search"

    genius_response = requests.get(URL_GENIUS, params=parameter2, headers=header2)

    #Obtaining data from Genius

    genius_data = genius_response.json() 
    try:
        lyrics_data = genius_data['response']['hits'][0]['result']['url']
    except KeyError:
        print("Couldn't fetch the lyrics page")
    
    #Return dictionary with relevant info for webpage
    return {
        "name_song" : song_name,
        "artist_name" : song_artist,
        "picture_song" : song_picture,
        "player" : song_player,
        "lyrics_url" : lyrics_data
    }


    