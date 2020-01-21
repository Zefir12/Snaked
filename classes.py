from functions import *
from settings import *

class Obiekt:
    def __init__(self, x, y, m, vx=0, vy=0):
        self.x = x
        self.y = y
        self.xstart = x
        self.vx = vx
        self.vy = vy
        self.offset = 0
        self.mass = m
        self.gravity = Settings.gravity
        self.kolor = [0, 0, 0]

    def rysuj(self):
        pygame.draw.circle(obraz, self.kolor, [int(self.x), int(self.y)], 10)

    def update(self):
        self.xstart += self.vx
        self.x = self.xstart + self.offset
        self.y += self.vy

    def grawitacja(self):
        self.vy += Settings.gravity

class Background:
    def __init__(self, x, y, kolor, height, thicc):
        self.x = x
        self.y = y
        self.kolor = kolor
        self.height = height
        self.thicc = thicc

    def rysuj(self):
        pygame.draw.rect(obraz, self.kolor, [self.x, self.y, self.thicc, self.height])

class Przeszkoda:
    def __init__(self, x, y, sizex, sizey):
        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.kolor = [200, 40, 10]

    def rysuj(self):
        pygame.draw.rect(obraz, self.kolor, [self.x, self.y, self.sizex, self.sizey])