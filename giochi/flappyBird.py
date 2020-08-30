#gioco flabby bird

import pygame
import random

pygame.init()

#creo gli elementi principali e assegno un'immagine ad essi
sfondo=pygame.image.load("C:/Users/Diego/Pictures/flappy_bird/sfondo.jpg")
uccello=pygame.image.load("C:/Users/Diego/Pictures/flappy_bird/uccello.png")
base=pygame.image.load("C:/Users/Diego/Pictures/flappy_bird/base.png")
game_over=pygame.image.load("C:/Users/Diego/Pictures/flappy_bird/game_over.jpg")
tubo_su=pygame.image.load("C:/Users/Diego/Pictures/flappy_bird/tubo.png")
tubo_giu=pygame.transform.flip(tubo_su, False, True)#false per la x e true per la y

#creo la facciata di gioco
SCHERMO=pygame.display.set_mode((288, 512))
FPS=150
FONT=pygame.font.SysFont("Comin Sans Ms", 50, bold=True)

class tubi_classe:
    def __init__(self):
        self.x=300
        self.y=random.randint(-20, 150)

    def avanza_e_disegna(self):
        self.x -= VEL_AVANZ
        SCHERMO.blit(tubo_giu, (self.x, self.y-210))
        SCHERMO.blit(tubo_su, (self.x, self.y+210))

    def schianta(self, uccello, uccellox, uccelloy):
        tolleranza=5#per aggiustare i confini dell'uccello
        uccello_lato_dx=uccellox+uccello.get_width()-tolleranza
        uccello_lato_sx=uccellox+tolleranza
        tubo_lato_dx=self.x+tubo_giu.get_width()
        tubo_lato_sx=self.x
        uccello_lato_su=uccelloy+tolleranza
        uccello_lato_giu=uccelloy+uccello.get_height()-tolleranza
        tubo_lato_su=self.y
        tubo_lato_giu=self.y+210
        if uccello_lato_dx>tubo_lato_sx and uccello_lato_sx<tubo_lato_dx:#sovrapposti orizzontalmente
            if uccello_lato_su<tubo_lato_su or uccello_lato_giu>tubo_lato_giu:
                hai_perso()

    def fra_i_tubi(self, uccello, uccellox):#non conta la posizione verticale, tanto se si schianta si ferma prima
        tolleranza=5#per aggiustare i confini dell'uccello
        uccello_lato_dx=uccellox+uccello.get_width()-tolleranza
        uccello_lato_sx=uccellox+tolleranza
        tubo_lato_dx=self.x+tubo_giu.get_width()
        tubo_lato_sx=self.x
        if uccello_lato_dx>tubo_lato_sx and uccello_lato_sx<tubo_lato_dx:#sovrapposti orizzontalmente:
            return True
        
def hai_perso():
    SCHERMO.blit(game_over, (50, 200))
    aggiorna()

    #entro in un ciclo while infinito ed esco finchè non viene premuto spazio
    #in questo modo la scritta non lampeggia e rimane fissa, come il resto del gioco
    ricomincia=False
    while not ricomincia:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                inizializza()
                ricomincia=True
            if event.type==pygame.QUIT:
                pygame.quit()

def disegna_oggetti():
    SCHERMO.blit(sfondo, (0, 0))
    for t in tubi:
        t.avanza_e_disegna()
    SCHERMO.blit(uccello, (uccellox, uccelloy))
    SCHERMO.blit(base, (basex, 420))#basex è una variabile perchè il terreno avanza
    #i punti
    punti_render=FONT.render(str(punti), 1, (255, 255, 255))
    SCHERMO.blit(punti_render, (144, 5))

def inizializza():#definisco la posizione x e y dell'uccello e la sua velocità y
    global uccellox, uccelloy, uccello_vely
    global basex
    global tubi
    global punti
    global fra_i_tubi
    global VEL_AVANZ
    uccellox=60
    uccelloy=150
    uccello_vely=-5
    basex=0
    tubi=[]
    tubi.append(tubi_classe())
    punti=0
    fra_i_tubi=False
    VEL_AVANZ=3

    
inizializza()

    
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
    

while True:
    #aggiungo la forza di gravità
    uccello_vely += 0.3
    uccelloy += uccello_vely
    basex -= VEL_AVANZ
    if basex<-45:
        basex=0


    #colpisce la base
    if uccelloy>405:#in teoria 400, ma devo considerare lo spessore dell'immagine
        hai_perso()
    
    #pulsante cliccato?
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            uccello_vely=-6
        if event.type==pygame.QUIT:
            pygame.quit()
    
    #aggiungo l'oggetto
    disegna_oggetti()
    #aggiorno costantemente lo schermo, in base ai fps
    aggiorna()

    #aggiungo il tubo appena l'ultimo raggiunge la coordinata x=150
    if tubi[-1].x<140:
        tubi.append(tubi_classe())

    #scontro con i tubi
    for t in tubi:
        t.schianta(uccello, uccellox, uccelloy)

    #aumento i punti quando avviene il passaggio da false a true della variabile tra i tubi
    if not fra_i_tubi:#non è fra i tubi
        for t in tubi:
            if t.fra_i_tubi(uccello, uccellox):#se entra
                fra_i_tubi=True#valore diventa true
    if fra_i_tubi:#è fra i tubi
        fra_i_tubi=False
        for t in tubi:
            if t.fra_i_tubi(uccello, uccellox):
                fra_i_tubi=True
                break
        if not fra_i_tubi:#uccello appena uscito dai tubi
            punti+=1
            if punti%15==0:
                VEL_AVANZ+=0.5


#tutti gli errori che vengono dati alla fine ci sono perche vengono
#usati dei numeri float e non interi, quindi probabilmete in una versione
#successiva daranno un vero errore.
