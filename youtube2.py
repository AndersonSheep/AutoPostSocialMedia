from googleapiclient.discovery import build
youTubeApiKey="xxxxxxxxxxxxxxxxxxxxxx"
youtube = build('youtube','v3', developerKey=youTubeApiKey)
# Extraindo videos de uma Playlist 
playlistId = 'xxxxxxxxxxxxxxxxxxxxx' #Dicas de Pandas Playlist
playlistName = 'Dicas de Pandas'
nextPage_token = None
playlist_videos = []

while True:
  res = youtube.playlistItems().list(part='snippet', playlistId = playlistId, maxResults=50, pageToken=nextPage_token).execute()
  playlist_videos += res['items']
  
  nextPage_token = res.get('nestPageToken')

  if nextPage_token is None:
    break
print(playlist_videos)
