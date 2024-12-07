# 🎵 **Music Recommender por Emoção** 🎶

Este é um projeto interativo que combina o poder da inteligência artificial com a API do Spotify para oferecer recomendações personalizadas de músicas, artistas e álbuns. Basta descrever como você está se sentindo, e o sistema cuidará de sugerir conteúdos musicais que se alinhem ao seu estado emocional.

Além disso, o sistema permite que você se cadastre, escolha seus gostos musicais e receba recomendações mais assertivas com base nas suas preferências.

---

## 🚀 **Funcionalidades**
- **🎤 Descrição Natural**: Descreva como você está se sentindo em uma frase ou palavras-chave.
- **🎧 Recomendação Personalizada**: Receba sugestões de músicas, artistas e álbuns com base na emoção detectada e no seu histórico de gostos musicais.
- **📝 Cadastro de Usuário**: Crie um perfil com seu nome e selecione seus estilos musicais favoritos para recomendações mais precisas.
- **🔄 Resultados Aleatórios**: Cada busca traz resultados únicos, mesmo com descrições semelhantes.
- **🌟 UI Moderna**: Interface simples, bonita e responsiva, construída com **TailwindCSS**.

---

## 🛠️ **Tecnologias Utilizadas**
- **Backend**: 
  - [Python](https://www.python.org/) + [Flask](https://flask.palletsprojects.com/)
  - Integração com a [API do Spotify](https://developer.spotify.com/documentation/web-api/)
  - Integração com o [Google Gemini](https://cloud.google.com/ai-generative)
  - Banco de dados para armazenar informações de usuários e preferências musicais
- **Frontend**: 
  - HTML5 + TailwindCSS
  - JavaScript puro para interações dinâmicas
- **Outras Ferramentas**:
  - Gerenciamento de dependências com `pip` e `venv`
  - Variáveis de ambiente com `dotenv`
  - Banco de dados para armazenar usuários e gostos musicais

---

## ⚙️ **Como Configurar e Rodar o Projeto**

### Pré-requisitos
1. Python 3.7+
2. Conta no [Spotify Developer](https://developer.spotify.com/) para obter as credenciais (Client ID e Client Secret).
3. Google Cloud configurado para utilizar o Google Gemini.
4. Banco de dados configurado (SQLite ou PostgreSQL recomendado).

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
    DATABASE_URL=sua_url_do_banco_de_dados
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

## 👤 **Cadastro de Usuário**

Para fornecer recomendações mais precisas, os usuários podem se cadastrar no sistema e escolher seus estilos musicais preferidos. Isso permite que o sistema personalize as sugestões com base no histórico de gostos musicais.

### Fluxo de Cadastro
1. O usuário preenche o nome de usuário e escolhe seus estilos musicais favoritos.
2. As preferências são salvas no banco de dados.
3. Após o cadastro, o usuário pode receber recomendações de músicas baseadas em seus gostos e sentimentos.

---

## 🎧 **Recomendações Musicais por Emoção**

Além das preferências de estilo, o sistema também oferece recomendações baseadas nas emoções descritas pelo usuário. Ao informar como se sente, o sistema, com o auxílio da API do Google Gemini, detecta a emoção e faz sugestões personalizadas de músicas, artistas e álbuns.

---

## 🌍 **Exemplo de Uso**

1. **Cadastro de Usuário**:
   - Nome: João
   - Estilos Musicais: Rock, Pop, Jazz
   - Recebe recomendações mais precisas baseadas em suas escolhas.

2. **Recomendação por Emoção**:
   - Descrição: "Estou me sentindo muito animado hoje!"
   - O sistema sugere músicas energéticas de Pop e Rock.

---

## Contribuindo

Se você deseja contribuir para o projeto, sinta-se à vontade para abrir issues ou pull requests. Certifique-se de testar suas alterações antes de enviá-las.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito com ❤️ por [Miguel Estevam](https://github.com/MiguelEstevam)
