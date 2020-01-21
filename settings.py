import pygame
import pickle

class settings:
    def __init__(self):
        self.gravity = 0.5
        self.przyspieszenie = 0.1
        self.limitpredkosci = 49
        self.dlugoscgracza = 12
        self.snakeupforce = 0.9
        self.snakedownforce = 1.5
        self.canfly = False


class config:
    def __init__(self):
        self.name = None

Settings = settings()



with open('settings.txt', 'rb') as obiekt:
    Config = pickle.load(obiekt)



szerokoscOkna = 1900
wysokoscOkna = 1000
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
czcionka = pygame.font.Font("Czcionki/Montserrat-ExtraBold.otf", 10)
czcionkaBIG = pygame.font.Font("Czcionki/Montserrat-ExtraBold.otf", 40)
obraz = pygame.display.set_mode([szerokoscOkna, wysokoscOkna])
tlo = pygame.image.load('tlo.png')