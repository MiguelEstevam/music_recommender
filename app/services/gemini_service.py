import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def find_common_styles(user_descriptions):
    try:
        # Definindo o prompt para o modelo
        prompt = (
            f"Com base nas seguintes descrições de estilos musicais fornecidas por diferentes usuários: "
            f"{', '.join(user_descriptions)}, identifique gêneros musicais compartilhados e compatíveis. "
            f"Inclua gêneros como Rock, Pop, Jazz, Hip-Hop, Clássica, Eletrônica, R&B, Reggae, Blues, Funk, "
            f"Soul, Country, Metal, Indie, Alternativa, Música Latina, Música Folclórica, K-Pop e World Music. "
            f"Responda apenas com os gêneros musicais comuns separados por vírgulas, sem frases adicionais."
        )

        # Usando o modelo Gemini para gerar os estilos comuns
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content({
            "parts": [
                {
                    "text": prompt
                }
            ]
        })

        # Processando a resposta para extrair os estilos
        common_styles = response.parts[0].text.strip().lower().split(", ")
        return common_styles

    except Exception as e:
        raise Exception(f"Erro ao processar dados no Gemini: {e}")
