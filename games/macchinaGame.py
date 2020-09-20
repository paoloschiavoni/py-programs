import pygame
import random
pygame.init()

SCHERMO=pygame.display.set_mode((1000, 500))
FPS=150
FONT=pygame.font.SysFont("Comin Sans Ms", 30, bold=True)


car=pygame.image.load("C:/Users/Diego/Pictures/Corsa/car.png")
sfondo=pygame.image.load("C:/Users/Diego/Pictures/Corsa/sfondo.png")
ostacolo=pygame.image.load("C:/Users/Diego/Pictures/Corsa/ostacolo01.png")
base=pygame.image.load("C:/Users/Diego/Pictures/Corsa/base01.png")
sconfitta=pygame.image.load("C:/Users/Diego/Pictures/Corsa/hai_perso.PNG")


class ostacolo_classe:

    def __init__(self):
        self.x=1000

    def avanza_e_disegna(self):
        self.x-=VEL_AVANZ
        SCHERMO.blit(ostacolo, (self.x, 376))

    def schianta(self):
        car_lato_dx=carx+100
        car_lato_sx=carx
        car_lato_su=cary
        car_lato_giu=cary+34

        ostacolo_lato_dx=self.x+100
        ostacolo_lato_sx=self.x+10
        ostacolo_lato_su=374

        if car_lato_dx>ostacolo_lato_sx and car_lato_sx< ostacolo_lato_dx:
            if car_lato_giu>ostacolo_lato_su:
                hai_perso()

def hai_perso():
    SCHERMO.blit(sconfitta, (0, 57))
    aggiorna()
    ricomincia=False
    while not ricomincia:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                inizializza()
                ricomincia=True
            if event.type==pygame.QUIT:
                pygame.quit()
    
def inizializza():
    global VEL_AVANZ, carx, cary, vely, basex, salto, ostacoli, punti, spiccata_in_alto
    VEL_AVANZ=15
    carx=200
    cary=356
    vely=0
    basex=0
    salto=True
    ostacoli=[]
    ostacoli.append(ostacolo_classe())
    punti=0
    spiccata_in_alto=20

inizializza()


def disegna():
    SCHERMO.blit(sfondo, (0, 0))
    SCHERMO.blit(car, (carx, cary))
    SCHERMO.blit(base, (basex, 400))
    for o in ostacoli:
        o.avanza_e_disegna()
    punti_render=FONT.render(str(punti), 1, (0, 0, 0))
    SCHERMO.blit(punti_render, (900, 20))

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

while True:

    #base
    basex-=VEL_AVANZ
    if basex<-55:
        basex=0

    #salto
    for event in pygame.event.get():
        if salto==True:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
                vely=-spiccata_in_alto
                salto=False
        if event.type==pygame.QUIT:
            pygame.quit()

    cary+=vely
    vely+=2
    if cary>=356:
        vely=0
        cary=356
        salto=True

    #aggiungo altri ostacoli
    distanza=random.randint(-1000, 700)
    if ostacoli[-1].x<distanza:
        ostacoli.append(ostacolo_classe())


    #scontro con ostacoli
    for o in ostacoli:
        o.schianta()

    punti+=1
    if punti%300==0:
        VEL_AVANZ+=1
        spiccata_in_alto+=1
    
    
    disegna()
    aggiorna()
