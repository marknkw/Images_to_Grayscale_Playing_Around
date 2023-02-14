from PIL import Image
import os
import math

def verificar_imagem(nome):
    if os.path.isfile(nome):
        return True
    else:
        return False
def verificar_diretorio(nome):
    caminho = os.path.exists(nome)
    if caminho == True:
        if verificar_imagem("Resources/morango.png"):
            return True
        else:
            return False
    else:
        return False

def verificar_tamanho_imagem(imagem):
    return (Image.open(imagem)).size

def media_dos_pixels(r, g, b, l_im, a_im):
    imagem_cinza = []
    for i in range(0, l_im):
        for j in range(0, a_im):
            coordenadas = x, y = i, j
            red, green, blue = float(r.getpixel(coordenadas)), float(g.getpixel(coordenadas)), float(b.getpixel(coordenadas))
            media_das_cores = ((red+green+blue)/3)
            if (media_das_cores % 1) == 0:
                imagem_cinza.append(media_das_cores)
            elif (media_das_cores % 1) > 0.5:
                imagem_cinza.append(math.ceil(media_das_cores))
            elif (media_das_cores % 1) < 0.5:
                imagem_cinza.append(math.floor(media_das_cores))

    return imagem_cinza

def importar_imagem(imagem):
    imagem_inicial = "Resources/" + imagem
    """print(imagem_inicial)"""
    with Image.open(imagem_inicial) as imagem_canais:
        canais_convertidos = imagem_canais.convert("RGB")
        r, g, b = canais_convertidos.split()
        return r, g, b

def canaistamanho_imagem():
    if verificar_diretorio("Resources") == True:
        r, g, b, = importar_imagem("morango.png")
        l_im, a_im = verificar_tamanho_imagem("Resources/morango.png")
        return r, g, b, l_im, a_im

    else:
        print("Pasta não existe...")
        exit()


def salvar_imagem(imagem, tamanho):
    imagem_bytes = bytes(imagem)
    imagem_cinza_nova = Image.frombytes("L", tamanho, imagem_bytes)
    imagem_cinza_nova.show()
    exit()


r, g, b, l_im, a_im = canaistamanho_imagem()
r.show(), g.show(), b.show()
coordenadas_globais = int(l_im), int(a_im)
imagem_cinza = media_dos_pixels(r, b, g, l_im, a_im)
"""print(imagem_cinza)"""
salvar_imagem(imagem_cinza, coordenadas_globais)

"""print(imagem_cinza)"""
