import os
import requests
import base64
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
import time

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Chaves de API do Spotify e Gemini
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Cache do token do Spotify
SPOTIFY_TOKEN = {"access_token": None, "expires_at": 0}

# Configuração do Flask
app = Flask(__name__)

# Inicializa o cliente do Google Gemini
def initialize_gemini_client():
    try:
        genai.configure(api_key=GEMINI_API_KEY)
    except Exception as e:
        raise Exception(f"Erro ao configurar o cliente Google Gemini: {e}")

# Função para obter o token de acesso do Spotify com cache
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
        raise Exception(f"Erro ao obter token do Spotify: {response.json()}")

# Função para analisar o sentimento do usuário com o Google Gemini
def analyze_emotion_with_gemini(user_input):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content({
            "parts": [
                {"text": f"Classifique o sentimento na seguinte descrição: '{user_input}'. "
                         "Responda com uma das opções: feliz, triste, motivado, relaxado, ansioso ou amor."}
            ]
        })
        emotion = response.text.strip().lower()
        return emotion
    except Exception as e:
        raise Exception(f"Erro ao analisar sentimento com Google Gemini: {e}")

# Rota inicial
@app.route('/')
def home():
    return render_template("index.html")

# Rota para recomendar músicas/artistas/albuns com base na emoção do usuário
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        user_description = request.form.get('description')
        if not user_description:
            return jsonify({"error": "Descrição não fornecida"}), 400

        if len(user_description) > 500:
            return jsonify({"error": "Descrição muito longa. Máximo de 500 caracteres."}), 400

        # Use o Google Gemini para identificar o sentimento
        detected_emotion = analyze_emotion_with_gemini(user_description)
        EMOTION_TO_QUERY = {
            "feliz": "happy",
            "triste": "sad",
            "motivado": "motivational",
            "relaxado": "chill",
            "ansioso": "calm",
            "amor": "love"
        }
        if detected_emotion not in EMOTION_TO_QUERY:
            return jsonify({"error": f"Sentimento não reconhecido: {detected_emotion}"}), 400

        query = EMOTION_TO_QUERY[detected_emotion]

        # Obter o token do Spotify
        access_token = get_spotify_access_token()

        # Configura cabeçalhos para a API do Spotify
        headers = {"Authorization": f"Bearer {access_token}"}
        
        # Buscar músicas/artistas/albuns usando a API do Spotify
        response = requests.get(
            f"https://api.spotify.com/v1/search?q={query}&type=track,artist,album&limit=5",
            headers=headers
        )

        if response.status_code != 200:
            return jsonify({"error": "Erro ao buscar informações no Spotify"}), response.status_code

        # Processar a resposta da API Spotify
        response_data = response.json()
        
        tracks = response_data.get('tracks', {}).get('items', [])
        artists = response_data.get('artists', {}).get('items', [])
        albums = response_data.get('albums', {}).get('items', [])

        # Filtrar resultados válidos
        results = []

        # Adicionar músicas
        for track in tracks:
            results.append({
                'type': 'track',
                'name': track['name'],
                'url': track['external_urls']['spotify'],
                'image': track['album']['images'][0]['url'] if track['album']['images'] else 'Sem imagem'
            })

        # Adicionar artistas
        for artist in artists:
            results.append({
                'type': 'artist',
                'name': artist['name'],
                'url': artist['external_urls']['spotify'],
                'image': artist['images'][0]['url'] if artist['images'] else 'Sem imagem'
            })

        # Adicionar álbuns
        for album in albums:
            results.append({
                'type': 'album',
                'name': album['name'],
                'url': album['external_urls']['spotify'],
                'image': album['images'][0]['url'] if album['images'] else 'Sem imagem'
            })

        # Retornar os resultados
        return jsonify(results), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Inicializa o servidor Flask
if __name__ == '__main__':
    initialize_gemini_client()
    app.run(debug=True, port=3000)
