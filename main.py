from functions import *
from classes import Obiekt, Przeszkoda, Background
from settings import *



listaobiektow = []
listaprzeszkod = []

while True:
    a = random.randint(0, 150)
    listaprzeszkod.append(Przeszkoda(random.randint(-szerokoscOkna,szerokoscOkna*2), wysokoscOkna - a, 50, a))
    if len(listaprzeszkod) > 7:
        break

listablokow = []
listablokowbeta = []
listaszarychblokow = []
generateBackground(listablokow, 60, 150, 25, 130, 160, 80, 100, Background)
generateBackground(listablokowbeta, 10, 50, 25, 300, 450, 100, 200, Background)
generateBackground(listaszarychblokow, 8, 20, 25, 400, 700, 400, 900, Background)



pint = [szerokoscOkna/2, wysokoscOkna - 10]
pintvx = 0
pintvy = 0
offset = 0



while True:
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    clock.tick(60)
    obraz.blit(tlo, [0, 0])
    if przycisk(1530, 373, 330, 60, mouse[0], mouse[1], click[0], text='Play', r=50, textsize=0):
        Run = True
        while Run:
            if Settings.canfly:
                stycznosc_zpodlozem = True
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            clock.tick(60)
            redraw_game(90, 90, 90)
            napisy(Config.name, 0, 0, 0)
            for b in listaszarychblokow:
                b.rysuj()
                b.x += offset / 2.5
                if b.x > szerokoscOkna * 2:
                    b.x = -szerokoscOkna
                if b.x < -szerokoscOkna * 1.5:
                    b.x = szerokoscOkna * 1.5

            for b in listablokowbeta:
                b.rysuj()
                b.x += offset / 2
                if b.x > szerokoscOkna * 2:
                    b.x = -szerokoscOkna
                if b.x < -szerokoscOkna * 1.5:
                    b.x = szerokoscOkna * 1.5

            for b in listablokow:
                b.rysuj()
                b.x += offset/1.5
                if b.x > szerokoscOkna * 2:
                    b.x = -szerokoscOkna
                if b.x < -szerokoscOkna * 1.5:
                    b.x = szerokoscOkna * 1.5

            for b in listaprzeszkod:
                b.rysuj()
                b.x += offset
                if b.x > szerokoscOkna * 2:
                    b.x = -szerokoscOkna
                if b.x < -szerokoscOkna * 1.5:
                    b.x = szerokoscOkna * 1.5

            pint[1] += pintvy
            if pint[0] > szerokoscOkna / 2 and pintvx > 0:
                offset = -pintvx

            elif pint[0] < szerokoscOkna / 2 and pintvx < 0:
                offset = -pintvx
            else:
                offset = 0
                pint[0] += pintvx
            if pygame.key.get_pressed()[pygame.K_w] and stycznosc_zpodlozem:
                pintvy -= Settings.snakeupforce
            if pygame.key.get_pressed()[pygame.K_s]:
                pintvy += Settings.snakedownforce
            if pygame.key.get_pressed()[pygame.K_d] and pintvx < Settings.limitpredkosci:
                pintvx += Settings.przyspieszenie
            else:
                if pintvx > 0:
                    pintvx -= 0.05
            if pygame.key.get_pressed()[pygame.K_a] and pintvx > -Settings.limitpredkosci:
                pintvx -= Settings.przyspieszenie
            else:
                if pintvx < 0:
                    pintvx += 0.05
            if pint[1] < wysokoscOkna - 12:
                pintvy += Settings.gravity
            if pint[1] >= wysokoscOkna - 9:
                pint[1] = wysokoscOkna - 8
                if not pygame.key.get_pressed()[pygame.K_w]:
                    pintvy *= -0.4  # sprezystosc

            listaobiektow.append(Obiekt(pint[0], pint[1], 100))
            stycznosc_zpodlozem = False
            for a in listaobiektow:
                a.offset += offset
                a.rysuj()
                a.update()
                a.grawitacja()

                if a.y >= wysokoscOkna - 9:
                    a.y = wysokoscOkna - 8
                    a.vy *= -0.5  # sprezystosc

                if a.y >= wysokoscOkna - 12:
                    stycznosc_zpodlozem = True
                    a.kolor = [200, 0, 0]
                else:
                    a.kolor = [0, 0, 0]
            xdi = 0
            for b in listaobiektow:
                xdi += 1
                if xdi < len(listaobiektow) - Settings.dlugoscgracza:
                    listaobiektow.remove(b)

            for b in listaprzeszkod:
                if b.x - 9 < pint[0]+pintvx < b.x + 59 and pint[1] > b.y:
                    pintvx *= -0.7
                if pint[1]+pintvy >= b.y - 9 and b.x - 9 < pint[0]+pintvx < b.x + 59:
                    pintvy *= -0.7
                for a in listaobiektow:
                    if b.x - 9 < a.x + a.vx < b.x + 59 and a.y > b.y:
                        a.vx *= -0.7
                    if a.y + a.vy >= b.y - 9 and b.x - 9 < a.x < b.x + 59:
                        a.vy *= -0.7


            Run = off()
    off()

