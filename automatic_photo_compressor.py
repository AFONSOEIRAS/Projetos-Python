import PIL
from PIL import Image
from tkinter.filedialog import *
#Abrir uma caixa de diálogo Windows para ao usuário selecionar múltiplos arquivos
fl=askopenfilenames()
img = Image.open(fl[0])
#Diminuir o tamanho de uma imagem compactando-a – mantendo sua qualidade.
img.save("output.jpg", "JPEG", optimize = True, quality = 10)