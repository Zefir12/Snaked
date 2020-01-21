import sys
import random
from settings import *





def redraw_game(r, g, b):
    pygame.Surface.fill(obraz, [r, g, b])


def off():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('settings.txt', 'wb') as obiekt:
                pickle.dump(Config, obiekt)
            sys.exit(0)
    pygame.display.flip()
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        return False
    else:
        return True

def napisy(co, x, y,rozmiar):
    nazwa = str(co)
    kolor_napisu = [0, 0, 0]
    if rozmiar == 1:
        label2 = czcionka.render(nazwa, 1, kolor_napisu)
    else:
        label2 = czcionkaBIG.render(nazwa, 1, kolor_napisu)
    obraz.blit(label2, [x, y])


def przycisk(x, y, sizex, sizey, zmiennax, zmiennay, event, zmiennatrue=True, zmiennafalse=False, r=0, g=0, b=0, text=None, textsize=1):
    pygame.draw.rect(obraz, [r, g, b], [x, y, sizex, sizey])
    if text is not None:
        napisy(text, x, y, textsize)
    if x < zmiennax < x+sizex and y < zmiennay < y + sizey and event:
        return zmiennatrue
    else:
        return zmiennafalse

def generateBackground(lista,kolormin, kolormax, number, heightmin, heightmax, thickmin, thickmax, classs):
    while True:
        a = random.randint(heightmin, heightmax)
        kolor = random.randint(kolormin, kolormax)
        lista.append(
            classs(random.randint(-szerokoscOkna, szerokoscOkna * 2), wysokoscOkna - a, [kolor, kolor, kolor * 1.5],
                       a, random.randint(thickmin, thickmax)))
        if len(lista) > number:
            break