import random, os
music_dir = r'D:\Hotfa\RPA\Projetos-Python\Playing Random Music\Music Directory'
#Gera uma lista de arquivo
#OBS:filtrar por MP3
list_songs = os.listdir(music_dir)

#Gera um numero aleatório de lista de 0 até len -1
song = random.randint(0,len(list_songs)-1)
print(len(list_songs))
# Print Nome da Musica
print(list_songs[song])  

# Iniciar Arquivo MP3 
os.startfile(os.path.join(music_dir, list_songs[song])) 