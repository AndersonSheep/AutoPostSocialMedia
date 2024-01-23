import os
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Configurar as credenciais
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CLIENT_SECRET_FILE = "client_secret.json"  # Substitua pelo seu arquivo de credenciais
API_NAME = "youtube"
API_VERSION = "v3"
CREDENTIALS_FILE = "client_secret.json"  # Substitua pelo seu arquivo de credenciais

creds = None
if os.path.exists(CREDENTIALS_FILE):
    creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
    with open(CREDENTIALS_FILE, "w") as token:
        token.write(creds.to_json())

# Criar um serviço YouTube Data API
youtube = build(API_NAME, API_VERSION, credentials=creds)

# Parâmetros do vídeo
video_file_path = "videos/001.mp4"  # Substitua pelo caminho do seu vídeo
video_title = "Título do Vídeo"
video_description = "Descrição do Vídeo"
video_tags = ["tag1", "tag2"]

# Upload do vídeo
request_body = {
    "snippet": {
        "title": video_title,
        "description": video_description,
        "tags": video_tags,
        "categoryId": "22",  # Categoria do vídeo (consulte a documentação)
    },
    "status": {
        "privacyStatus": "private",  # Configuração de privacidade (public, private, unlisted)
    },
}

media = MediaFileUpload(video_file_path, chunksize=-1, resumable=True)
videos_insert_response = youtube.videos().insert(
    part=",".join(request_body.keys()), body=request_body, media_body=media
).execute()

print("Vídeo enviado com sucesso! Video ID:", videos_insert_response["id"])
