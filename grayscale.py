from PIL import Image
import numpy as np
import os
import math


def verificar_imagem(nome):
    if os.path.isfile(nome):
        return True
    else:
        return False


def verificar_diretorio(nome):
    caminho = os.path.exists(nome)
    if caminho:
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
                imagem_cinza.append(((coordenadas[0]+1, coordenadas[1]+1), int(media_das_cores)))
            elif media_das_cores == 0:
                imagem_cinza.append(((coordenadas[0]+1, coordenadas[1]+1), int(media_das_cores)))
            elif (media_das_cores % 1) > 0.5:
                imagem_cinza.append(((coordenadas[0]+1, coordenadas[1]+1), int(math.ceil(media_das_cores))))
            elif (media_das_cores % 1) < 0.5:
                imagem_cinza.append(((coordenadas[0]+1, coordenadas[1]+1), int(math.floor(media_das_cores))))
    print(imagem_cinza)

    return imagem_cinza


def importar_imagem(imagem):
    imagem_inicial = "Resources/" + imagem
    """print(imagem_inicial)"""
    with Image.open(imagem_inicial) as imagem_canais:
        print("imagem bands ", Image.Image.getbands(imagem_canais))
        canais_convertidos = imagem_canais.convert()
        r, g, b = canais_convertidos.split()
        return r, g, b


def canaistamanho_imagem():

    if verificar_diretorio("Resources"):
        r, g, b, = importar_imagem("morango.png")
        l_im, a_im = verificar_tamanho_imagem("Resources/morango.png")
        return r, g, b, l_im, a_im

    else:
        print("Pasta não existe...")
        exit()


def salvar_imagem(imagem, tamanho):
    """imagem_bytes = bytes(imagem)
    print(imagem_bytes)
    imagem_cinza_nova = Image.frombytes("L", tamanho, imagem_bytes)"""
    imagem_cinza_nova = Image.new("L", tamanho)
    for j in range(tamanho[1]):
            imagem_cinza_nova.putpixel(imagem[j])
    print(imagem_cinza_nova.size)
    imagem_cinza_nova.show()
    exit()


r_out, g_out, b_out, l_im_out, a_im_out = canaistamanho_imagem()
r_out.show(), g_out.show(), b_out.show()
print(l_im_out, a_im_out)
coordenadas_globais = int(l_im_out), int(a_im_out)
imagem_cinza_out = media_dos_pixels(r_out, b_out, g_out, l_im_out, a_im_out)
"""print(imagem_cinza)"""
salvar_imagem(imagem_cinza_out, coordenadas_globais)

"""print(imagem_cinza)"""
