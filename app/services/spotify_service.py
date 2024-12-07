import os
import requests
import time
import base64
import random

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

SPOTIFY_TOKEN = {"access_token": None, "expires_at": 0}

def get_spotify_access_token():
    global SPOTIFY_TOKEN
    if SPOTIFY_TOKEN['access_token'] and SPOTIFY_TOKEN['expires_at'] > time.time():
        return SPOTIFY_TOKEN['access_token']

    url = "https://accounts.spotify.com/api/token"
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_base64 = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')

    headers = {
        'Authorization': f'Basic {auth_base64}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {'grant_type': 'client_credentials'}
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        json_response = response.json()
        SPOTIFY_TOKEN['access_token'] = json_response['access_token']
        SPOTIFY_TOKEN['expires_at'] = time.time() + json_response['expires_in']
        return SPOTIFY_TOKEN['access_token']
    else:
        raise Exception(f"Erro ao obter token do Spotify: {response.status_code} - {response.text}")

def search_recommendations(styles):
    token = get_spotify_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    query = " OR ".join(styles)
    offset = random.randint(0, 100)  # Define um valor aleatório de início
    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=10&offset={offset}"

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        tracks = response.json().get("tracks", {}).get("items", [])
        if tracks:
            return tracks
        else:
            raise Exception("Nenhuma recomendação encontrada.")
    else:
        raise Exception(f"Erro ao buscar recomendações no Spotify: {response.status_code} - {response.text}")
