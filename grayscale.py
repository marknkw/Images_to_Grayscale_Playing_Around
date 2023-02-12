"""Initial commit of the program"""
from PIL import Image
import os

def verificar_imagem(nome):
    if os.path.isfile(nome):
        return True
    else:
        return False
def verificar_diretorio(nome):
    caminho = os.path.exists(nome)
    if caminho == True:
        if verificar_imagem("Resources/imagetest.png"):
            return True
        else:
            return False
    else:
        return False

def verificar_tamanho_imagem(imagem):
    return (Image.open(imagem)).size

def importar_imagem(imagem):
    imagem_inicial = "Resources/" + imagem
    print(imagem_inicial)
    with Image.open(imagem_inicial) as imagem_canais:
        canais_convertidos = imagem_canais.convert("RGB")
        r, g, b = canais_convertidos.split()
        return r, g, b


if verificar_diretorio("Resources") == True:
    r, g, b = importar_imagem("imagetest.png")
    r.show()
    l_im, a_im = verificar_tamanho_imagem("Resources/imagetest.png")
    print(l_im, a_im)

else:
    print("Pasta não existe...")
    exit()