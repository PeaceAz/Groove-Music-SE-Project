from dotenv import load_dotenv
import os
import base64
from requests import post
import json
import requests

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#print(client_id, client_secret)

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")  # encode using base64
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")


    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,  # get authorisation token correct
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=2"  # gives json object with artists, followers etc.as 1 artist result

    query_url = url + query
    result = requests.get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    # print(json_result) # to confirm if run - gives one artist result

    if len(json_result) == 0:  # we give else statement so if result not found it says no artist
        print("No artist with this name exists...")
        return None
    
    return json_result[0]  # otherwise return the json result/first result


def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
# looking for specific artist, top track and i pass a country to see the top track in the country
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

token = get_token()
print("Token...................................")

print(token)   # to see if code run to get token

print("Token...................................")
result = search_for_artist(token, "ACDC")
# print(result)  # should give the individual artist now - done! it run to show the artist
# print(result["name"])  # print artist name as ACDC -  run!
artist_id = result["id"]
songs = get_songs_by_artist(token, artist_id)
print (songs)  # it run! although the tracks are not so readable, we print now in readable form
# and show how many tracks

for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}") # perfect!


