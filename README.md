# 🎵 **Music Recommender por Emoção** 🎶

Este é um projeto interativo que combina o poder da inteligência artificial com a API do Spotify para oferecer recomendações personalizadas de músicas, artistas e álbuns. Basta descrever como você está se sentindo, e o sistema cuidará de sugerir conteúdos musicais que se alinhem ao seu estado emocional. 

---

## 🚀 **Funcionalidades**
- **🎤 Descrição Natural**: Descreva como você está se sentindo em uma frase ou palavras-chave.
- **🎧 Recomendação Personalizada**: Receba sugestões de músicas, artistas e álbuns com base na emoção detectada.
- **🔄 Resultados Aleatórios**: Cada busca traz resultados únicos, mesmo com descrições semelhantes.
- **🌟 UI Moderna**: Interface simples, bonita e responsiva, construída com **TailwindCSS**.

---

## 🛠️ **Tecnologias Utilizadas**
- **Backend**: 
  - [Python](https://www.python.org/) + [Flask](https://flask.palletsprojects.com/)
  - Integração com a [API do Spotify](https://developer.spotify.com/documentation/web-api/)
  - Integração com o [Google Gemini](https://cloud.google.com/ai-generative)
- **Frontend**: 
  - HTML5 + TailwindCSS
  - JavaScript puro para interações dinâmicas
- **Outras Ferramentas**:
  - Gerenciamento de dependências com `pip` e `venv`
  - Variáveis de ambiente com `dotenv`

---

## ⚙️ **Como Configurar e Rodar o Projeto**

### Pré-requisitos
1. Python 3.7+
2. Conta no [Spotify Developer](https://developer.spotify.com/) para obter as credenciais (Client ID e Client Secret).
3. Google Cloud configurado para utilizar o Google Gemini.

### Configuração do Ambiente
1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/music-recommender.git
    cd music-recommender
    ```

2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
    ```
    CLIENT_ID=seu_client_id_do_spotify
    CLIENT_SECRET=seu_client_secret_do_spotify
    GOOGLE_API_KEY=sua_chave_do_google_gemini
    ```

### Executando o Projeto
1. Inicie o servidor Flask:
    ```bash
    python app.py
    ```

2. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:3000
    ```

---



