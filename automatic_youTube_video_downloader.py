import pytube

link = 'https://www.youtube.com/watch?v=06kE4_9JDTo'
video_download = pytube.YouTube(link)

# Listar todas as streams disponíveis
streams = video_download.streams

# Escolher a stream com a maior resolução
video_stream = streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Fazer o download da stream selecionada
video_stream.download()

print('Video Downloaded', link)
