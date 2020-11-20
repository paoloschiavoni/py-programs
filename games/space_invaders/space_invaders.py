import pygame
import random

pygame.init()

FPS=90
SCHERMO=pygame.display.set_mode((800, 600))
FONT=pygame.font.SysFont("Comin Sans Ms", 30, bold=True)
contatore_per_vite=0

nave=pygame.image.load("C:/Users/Paolo.Schiavoni/source/repos/py programs/games/space_invaders/navicella01.png")
nemico=pygame.image.load("C:/Users/Paolo.Schiavoni/source/repos/py programs/games/space_invaders/nemico.png")
sfondo=pygame.image.load("C:/Users/Paolo.Schiavoni/source/repos/py programs/games/space_invaders/sfondo.jpg")
raggio=pygame.image.load("C:/Users/Paolo.Schiavoni/source/repos/py programs/games/space_invaders/raggio01.png")
raggio_nemico=pygame.image.load("C:/Users/Paolo.Schiavoni/source/repos/py programs/games/space_invaders/raggio.png")
eliminato=pygame.image.load("C:/Users/Paolo.Schiavoni/source/repos/py programs/games/space_invaders/eliminato.jpg")
game_over=pygame.image.load("C:/Users/Paolo.Schiavoni/source/repos/py programs/games/space_invaders/game_over.jpg")
sfera=pygame.image.load("C:/Users/Paolo.Schiavoni/source/repos/py programs/games/space_invaders/raggio.png")
cuore=pygame.image.load("C:/Users/Paolo.Schiavoni/source/repos/py programs/games/space_invaders/cuore.png")
cuore_che_scende=pygame.image.load("C:/Users/Paolo.Schiavoni/source/repos/py programs/games/space_invaders/cuore_che_scende.png")

class vite_classe:
    def __init__(self):
        self.vite=3

def disegna_punti():
    punti_render=FONT.render("Punti: "+str(punti), 1, (255, 255, 255))
    punti_di_fila_render=FONT.render("Di fila: "+str(punti_di_fila), 1, (255, 255, 255))
    migliore_sequenza_render=FONT.render("Migliore sequenza: "+str(migliore_sequenza), 1, (255, 255, 255))
    SCHERMO.blit(punti_render, (50, 485))
    SCHERMO.blit(punti_di_fila_render, (50, 510))
    SCHERMO.blit(migliore_sequenza_render, (50, 535))

def nuovo_nemico():
    nemici.append(nemici_classe())

class nemici_classe:
    def __init__(self):
        lista=[-200, 1000]
        self.nemicox=random.choice(lista)
        self.nemicoy=random.randint(20, 300)
        self.x=self.nemicox
        self.y=self.nemicoy
        self.dasx_sparo_min=150
        self.dasx_sparo_max=550
        self.dadx_sparo_min=250
        self.dadx_sparo_max=650

        if self.nemicox==-200:
            self.sparox=random.randint(self.dasx_sparo_min, self.dasx_sparo_max)
        if self.nemicox==1000:
            self.sparox=random.randint(self.dadx_sparo_min, self.dadx_sparo_max)
        self.sparoy=self.nemicoy+45

    def schianto_nemico(self):
        navedx=navex+70
        navesx=navex
        navesu=navey
        navegiu=navey+64

        nemicodx=self.x+75
        nemicosx=self.x
        nemicosu=self.y
        nemicogiu=self.y+55
        if navedx>nemicosx and navesx<nemicodx:
            if navesu<nemicogiu and navegiu>nemicosu:
                hai_perso()

    def spara_raggio_nemico(self):
        if self.nemicox==-200:#dasx
            if self.x>self.sparox+20:
                return True
            else:
                return False
        if self.nemicox==1000:#dadx
            if self.x<self.sparox:
                return True
            else:
                return False

    def raggio_nemico_colpisce(self):
        self.raggio_nemicosu=self.sparoy
        self.raggio_nemicogiu=self.sparoy+50
        self.raggio_nemicodx=self.sparox+24
        self.raggio_nemicosx=self.sparox

        self.navesu=navey
        self.navegiu=navey+70
        self.navedx=navex+64
        self.navesx=navex

        if self.raggio_nemicosu<self.navegiu and self.raggio_nemicogiu>self.navesu:
            if self.raggio_nemicodx>self.navesx and self.raggio_nemicosx<self.navedx:
                hai_perso()

def cuore_colpisce():
    global scendi_cuore, posx_cuore_che_scende, posy_cuore_che_scende, vite
    cuore_su=posy_cuore_che_scende
    cuore_giu=cuore_su+25
    cuore_sx=posx_cuore_che_scende
    cuore_dx=cuore_sx+25

    nave_su=navey
    nave_giu=nave_su+70
    nave_sx=navex
    nave_dx=nave_sx+64

    if cuore_su<nave_giu and cuore_giu>nave_su:
        if cuore_sx<nave_dx and cuore_dx>nave_sx:
            scendi_cuore=False
            return True
    else:
        return False

def hai_perso():
    global vite
    vite-=1
    if vite==0:
        SCHERMO.blit(game_over, (0, 0))
        disegna_punti()
        aggiorna()
        ricomincia=False
        while not ricomincia:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type==pygame.KEYDOWN and event.key==pygame.K_c:
                    start()
                    start_punti()
                    ricomincia=True
    else:
        start()


def start():
    global navex, navey, raggioy, raggiox, spara, raggi
    global nemici, dasx, dadx, ricomincia, conta_round
    global spara_nemico, posx_cuore1, scendi_cuore
    global posy_cuore_che_scende, posx_cuore_che_scende
    navex=350
    navey=450
    raggioy=navey-10
    raggiox=navex+30
    spara=False
    raggi=[]
    nemici=[]
    nemici.append(nemici_classe())
    dasx=False
    dadx=False
    ricomincia=False
    spara_nemico=False
    posx_cuore1=50
    scendi_cuore=False
    posy_cuore_che_scende=0
    posx_cuore_che_scende=0
start()

def start_punti():#altrimenti si resettano con la perdita della vita
    global punti, punti_di_fila, migliore_sequenza
    global VEL_NEMICO, VEL_RAGGIO, VEL_RAGGIO_NEMICO
    punti=0
    punti_di_fila=0
    migliore_sequenza=0
    VEL_NEMICO=7
    VEL_RAGGIO=30
    VEL_RAGGIO_NEMICO=10

start_punti()

def disegna():
    SCHERMO.blit(sfondo, (0, 0))
    SCHERMO.blit(nave, (navex, navey))
    for vita in range(vite):
        pixel_da_aggiungere_cuore=0
        pixel_da_aggiungere_cuore=vita*50
        SCHERMO.blit(cuore, (posx_cuore1+pixel_da_aggiungere_cuore, 60))

    if dasx:
        SCHERMO.blit(nemico, (nemici[-1].x, nemici[-1].y))
        nemici[-1].x+=VEL_NEMICO
    if dadx:
        SCHERMO.blit(nemico, (nemici[-1].x, nemici[-1].y))
        nemici[-1].x-=VEL_NEMICO

    disegna_punti()

    if spara_nemico==True:
        SCHERMO.blit(raggio_nemico, (nemici[-1].sparox, nemici[-1].sparoy))
        nemici[-1].sparoy+=VEL_RAGGIO_NEMICO

    global scendi_cuore, posx_cuore_che_scende, posy_cuore_che_scende#lo devo fare altrimenti mi da variable referenced before assigment
    if scendi_cuore:
        SCHERMO.blit(cuore_che_scende, (posx_cuore_che_scende, posy_cuore_che_scende))
        posy_cuore_che_scende+=5


    aggiorna()

class raggio_classe:
    def __init__(self):
        self.x=raggiox
        self.y=raggioy
        self.aggiungi_punti=False

    def spara_raggio(self):
        while self.y>-10:
            SCHERMO.blit(raggio, (self.x, self.y))
            aggiorna()
            disegna()
            self.y-=VEL_RAGGIO

    def raggio_colpisce(self):
        raggiosu=self.y
        raggiogiu=self.y+25
        raggiodx=self.x+25
        raggiosx=self.x

        nemicosx, nemicosu=nemici[-1].x-20, nemici[-1].y
        nemicodx=nemicosx+122
        nemicogiu=nemicosu+55
        if raggiosu<nemicogiu:
            if nemicodx>raggiosx and nemicosx<raggiodx:
                nuovo_nemico()
                self.aggiungi_punti=True

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

while True:

    if contatore_per_vite==0:
        contatore_per_vite+=1
        vite=vite_classe().vite

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            raggi.append(raggio_classe())
            raggi[-1].spara_raggio()
            raggi[-1].raggio_colpisce()

            if raggi[-1].aggiungi_punti:
                punti_di_fila+=1
                raggi[-1].aggiungi_punti=False
                punti+=1

                if punti%3==0 and punti>1:
                    if VEL_NEMICO<38:
                        VEL_NEMICO+=2
                        VEL_RAGGIO+=3
                        VEL_RAGGIO_NEMICO+=3
                        nemici[-1].dasx_sparo_min-=15
                        nemici[-1].dasx_sparo_max-=15
                        nemici[-1].dadx_sparo_min+=15
                        nemici[-1].dadx_sparo_max+=15

                if punti%10==0:
                    posy_cuore_che_scende=0
                    posx_cuore_che_scende=random.randint(200, 600)
                    scendi_cuore=True
            else:
                if punti_di_fila>migliore_sequenza:
                    migliore_sequenza=punti_di_fila
                punti_di_fila=0

        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            navex+=60
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            navex-=60
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            navey-=60
        if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            navey+=60

        if event.type==pygame.KEYDOWN and event.key==pygame.K_c:
            start()

    #nemici
    if nemici[-1].nemicox==-200:
        dasx=True
    if nemici[-1].nemicox==1000:
        dadx=True


    for nemico_che_si_sposta in nemici:
        nemico_che_si_sposta.schianto_nemico()


    spara_nemico=nemici[-1].spara_raggio_nemico()
    nemici[-1].raggio_nemico_colpisce()

    if dasx:
        if nemici[-1].x>800:
            spara_nemico=False
            nuovo_nemico()
            dasx=False

    if dadx:
        if nemici[-1].x<-100:
            spara_nemico=False
            nuovo_nemico()
            dadx=False

    if cuore_colpisce():
        scendi_cuore=False
        posy_cuore_che_scende=0
        posx_cuore_che_scende=0

        vite+=1

    if posy_cuore_che_scende>620:
        scendi_cuore=False


    raggiox=navex+30
    raggioy=navey-10


    disegna()
    aggiorna()
