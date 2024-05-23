from flask import Flask, request, jsonify, redirect, session
from flask_restful import Api, Resource
import psycopg2
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
api = Api(app)

load_dotenv()
app.secret_key = os.getenv("FLASK_SECRET_KEY")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="musicapp",
        user="musicuser",
        password="password"
    )
    return conn

# Creating APIs below, route is an endpoint to get different type of data
@app.route('/login')
def login():
    auth_url = "https://accounts.spotify.com/authorize"
    params = {
        "client_id": SPOTIFY_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": SPOTIFY_REDIRECT_URI,
        "scope": "user-library-read user-top-read"
    }
    return redirect(f"{auth_url}?{urlencode(params)}")

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": SPOTIFY_REDIRECT_URI
    }
    r = requests.post(token_url, headers=headers, data=data)
    response_data = r.json()
    session['token'] = response_data['access_token']
    return redirect('/profile')

@app.route

@app.route('/profile')
def profile():
    headers = {
        "Authorization": "Bearer " + session['token']
    }
    user_profile = requests.get("https://api.spotify.com/v1/me", headers=headers).json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (username, spotify_id) VALUES (%s, %s) RETURNING id;',
                (user_profile['display_name'], user_profile['id']))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(user_id=user_id, username=user_profile['display_name'])



class ArtistList(Resource):
    def get(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM artists;')
        artists = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(artists)

    def post(self):
        new_artist = request.json
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO artists (name, spotify_id) VALUES (%s, %s) RETURNING id;',
                    (new_artist['name'], new_artist['spotify_id']))
        artist_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(artist_id=artist_id)

class SongList(Resource):
    def get(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM songs;')
        songs = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(songs)

    def post(self):
        new_song = request.json
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO songs (title, artist_id, spotify_id, genre, release_date) VALUES (%s, %s, %s, %s, %s) RETURNING id;',
                    (new_song['title'], new_song['artist_id'], new_song['spotify_id'], new_song['genre'], new_song['release_date']))
        song_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(song_id=song_id)

api.add_resource(ArtistList, '/artists')
api.add_resource(SongList, '/songs')

if __name__ == '__main__':
    app.run(debug=True)
