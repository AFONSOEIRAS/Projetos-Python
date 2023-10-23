from pygame import mixer
from gtts import gTTS

def main(texto):
   tts = gTTS(text=texto, lang='pt')
   tts.save('output.mp3')
   mixer.init()
   mixer.music.load('output.mp3')
   mixer.music.play()
   
if __name__ == "__main__":
   texto = "Olá, este é um exemplo de reprodução de áudio em português."
   main(texto)