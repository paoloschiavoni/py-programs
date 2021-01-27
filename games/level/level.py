#all'avvio del programma fare invio altrimenti resta fermo

import os
os.chdir('C:/Users/Paolo.Schiavoni/source/repos/py programs/games/level')
import pygame
pygame.init()

walkright=[pygame.image.load('r01.png'), pygame.image.load('r02.png'), pygame.image.load('r03.png'), \
pygame.image.load('r04.png'), pygame.image.load('r05.png'), pygame.image.load('r06.png'), pygame.image.load('r07.png'), \
pygame.image.load('r08.png')]

walkleft=[pygame.transform.flip(walkright[0], True, False), pygame.transform.flip(walkright[1], True, False), \
pygame.transform.flip(walkright[2], True, False), pygame.transform.flip(walkright[3], True, False), \
pygame.transform.flip(walkright[4], True, False), pygame.transform.flip(walkright[5], True, False), \
pygame.transform.flip(walkright[6], True, False), pygame.transform.flip(walkright[7], True, False)]

standr=[pygame.image.load('stand01.png'), pygame.image.load('stand02.png'), pygame.image.load('stand03.png'), pygame.image.load('stand04.png')]
standl=[pygame.transform.flip(standr[0], True, False), pygame.transform.flip(standr[1], True, False), \
pygame.transform.flip(standr[2], True, False), pygame.transform.flip(standr[3], True, False)]

atkr=[pygame.image.load('atk01.png'), pygame.image.load('atk02.png'), pygame.image.load('atk03.png'), pygame.image.load('atk04.png')]
atkl=[pygame.transform.flip(atkr[0], True, False), pygame.transform.flip(atkr[1], True, False), \
pygame.transform.flip(atkr[2], True, False), pygame.transform.flip(atkr[3], True, False), \
pygame.transform.flip(atkr[3], True, False)]

ewalkright=[pygame.image.load('er01.png'), pygame.image.load('er02.png'), pygame.image.load('er03.png'), \
pygame.image.load('er04.png'), pygame.image.load('er05.png'), pygame.image.load('er06.png'), pygame.image.load('er07.png'), \
pygame.image.load('er08.png'), pygame.image.load('er09.png'), pygame.image.load('er10.png'), pygame.image.load('er11.png'), \
pygame.image.load('er12.png')]

ewalkleft=[pygame.transform.flip(ewalkright[0], True, False), pygame.transform.flip(ewalkright[1], True, False), \
pygame.transform.flip(ewalkright[2], True, False), pygame.transform.flip(ewalkright[3], True, False), \
pygame.transform.flip(ewalkright[4], True, False), pygame.transform.flip(ewalkright[5], True, False), \
pygame.transform.flip(ewalkright[6], True, False), pygame.transform.flip(ewalkright[7], True, False), \
pygame.transform.flip(ewalkright[8], True, False), pygame.transform.flip(ewalkright[9], True, False), \
pygame.transform.flip(ewalkright[10], True, False), pygame.transform.flip(ewalkright[11], True, False)]

edeathr=[pygame.image.load('edeath01.png'), pygame.image.load('edeath02.png'), pygame.image.load('edeath03.png'), \
pygame.image.load('edeath04.png')]

edeathl=[pygame.transform.flip(edeathr[0], True, False), pygame.transform.flip(edeathr[1], True, False), \
pygame.transform.flip(edeathr[2], True, False), pygame.transform.flip(edeathr[3], True, False)]

bg=pygame.image.load('bgtramonto.jpg')

ground01=pygame.image.load('ground01.png')
ground02=pygame.image.load('ground02.png')
ground03=pygame.image.load('ground03.png')

pltfrm=pygame.image.load('pltfrm.png')
block=pygame.image.load('block.png')

cuore=pygame.image.load('cuore.png')

key01=pygame.image.load('key01.png')
key02=pygame.image.load('key02.png')
key03=pygame.image.load('key03.png')
key04=pygame.image.load('key04.png')
key05=pygame.image.load('key05.png')

forziere=[pygame.image.load('forziere06.png'), pygame.image.load('forziere05.png'), pygame.image.load('forziere04.png'), \
pygame.image.load('forziere03.png'), pygame.image.load('forziere02.png'), pygame.image.load('forziere01.png')]

sconfitta=[pygame.image.load('sconfitta07.png'), pygame.image.load('sconfitta06.png'), pygame.image.load('sconfitta05.png'), \
pygame.image.load('sconfitta04.png'), pygame.image.load('sconfitta03.png'), pygame.image.load('sconfitta02.png'), \
pygame.image.load('sconfitta01.png')]

vittoria=[pygame.image.load('vittoria07.png'), pygame.image.load('vittoria06.png'), pygame.image.load('vittoria05.png'), \
pygame.image.load('vittoria04.png'), pygame.image.load('vittoria03.png'), pygame.image.load('vittoria02.png'), \
pygame.image.load('vittoria01.png')]

block01=[640, 320, 665, 345]
block02=[540, 320, 565, 345]
block03=[480, 270, 505, 300]
block04=[420, 220, 445, 265]
block05=[360, 170, 385, 225]
#la 4 e la 5 sono diverse da quelle che sono disegnate perchè altrimenti col
#salto si trova troppo in altro e al posto di modificare le coordinate (cosa
#che potrebbe portare problemi come ha già fatto, cambio quelle dei blocchi
#che vengono disgnati, quindi non si vede nulla)
blocklist=[block01, block02, block03, block04, block05]
pltfrm_hitbox=[30, 250, 80, 238]

screen_width=800#800
screen_height=450#450
screen=pygame.display.set_mode((screen_width, screen_height))

clock=pygame.time.Clock()

contatore=0

class Enemy(object):
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=3
        self.walkcount=0
        self.facing=1#1=right, -1=left
        self.hitbox=[self.x, self.y, self.x+self.width, self.y+self.height]
        self.deathcount=0
        self.dead=False
        self.drawenemy=True

    def draw(self, screen):
        if self.walkcount>35:
            self.walkcount=0
        if self.facing==1:
            screen.blit(ewalkright[self.walkcount//3], (self.x, self.y))
            self.walkcount+=1
            if self.walkcount//3<7:
                self.x+=self.vel
            if self.x>150:
                self.facing=-1
        if self.facing==-1:
            if self.walkcount//3>=10:
                screen.blit(ewalkleft[self.walkcount//3], (self.x-50, self.y))
            if self.walkcount//3<10:
                screen.blit(ewalkleft[self.walkcount//3], (self.x, self.y))
            if self.walkcount//3<7:
                self.x-=self.vel
            self.walkcount+=1
            if self.x<2:
                self.facing=1
        self.hitbox=[self.x, self.y, self.x+self.width, self.y+self.height]


class player(object):
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.left=False
        self.right=True
        self.walkcountr=0
        self.walkcountl=0
        self.standing=True
        self.jumpcount=8
        self.isjump=False
        self.waitjump=0
        self.standcount=0
        self.isatk=False
        self.atkcount=0
        self.waitatk=25
        self.hitbox=[self.x, self.y, self.x+self.width, self.y+self.height]
        self.moveleft=1
        self.moveright=1
        self.whichonblock=None
        self.whichunderblock=None
        self.isonblock=False
        self.isunderblock=False
        self.fall=False
        self.fallcount=8
        self.lives=3
        self.contatore_chiave=0
        self.pltfrm_y=250
        self.canmove=True#is False when he gets on the elevator
        self.forziere_wait=0
        self.forziere_count=0
        self.movekey=False#when the key needs to move from the man to the treasure
        self.key_x=430
        self.sconfitta_count=0
        self.sconfitta_contatore=0
        self.sconfitta=False
        self.sconfitta_x=350
        self.sconfitta_y=210
        self.vittoria=False
        self.vittoria_x=350
        self.vittoria_y=210
        self.vittoria_count=0
        self.vittoria_contatore=0

    def draw(self, screen):

        if self.walkcountr>23:
            self.walkcountr=0
        if self.walkcountl>23:
            self.walkcountl=0


        if not(self.standing):
            if self.left:
                screen.blit(walkleft[self.walkcountl//3], (self.x, self.y))
                self.walkcountl+=1
            elif self.right:
                screen.blit(walkright[self.walkcountr//3], (self.x, self.y))
                self.walkcountr+=1

        if self.standing:
            if man.right:
                if self.standcount>19:
                    self.standcount=0
                screen.blit(standr[self.standcount//5], (self.x, self.y-10))
                self.standcount+=1
            if man.left:
                if self.standcount>19:
                    self.standcount=0
                screen.blit(standl[self.standcount//5], (self.x, self.y-10))
                self.standcount+=1

        self.hitbox=[self.x, self.y, self.x+self.width, self.y+self.height]

    def atk(self, screen):

        while self.atkcount<400:
            if self.right:
                screen.blit(atkr[self.atkcount//100], (self.x, self.y-100))
                if self.atkcount%50==0:
                    self.x+=1
            if self.left:
                if self.atkcount//100>=2:
                    screen.blit(atkl[self.atkcount//100], (self.x-50, self.y-100))
                if self.atkcount//100<2:
                    screen.blit(atkl[self.atkcount//100], (self.x, self.y-100))
                if self.atkcount%50==0:
                    self.x-=1

            if self.atkcount%100==0:
                if enemy.drawenemy:
                    enemy.draw(screen)
            screen.blit(ground03, (0, 250))
            screen.blit(block, (640, 310))
            screen.blit(block, (540, 310))
            screen.blit(block, (480, 265))
            screen.blit(block, (420, 210))
            screen.blit(block, (360, 165))

            for count in range(man.lives):
                screen.blit(cuore, (630+(50*count), 30))

            if not(enemy.drawenemy):
                screen.blit(ground02, (80, 150))
                screen.blit(pltfrm, (30, man.pltfrm_y))
                screen.blit(forziere[man.forziere_count], (500, 113))
                screen.blit(key01, (man.x-10, man.y-40))

            pygame.display.update()

            self.hitbox=[self.x, self.y, self.x+self.width, self.y+self.height]

            self.atkcount+=1
        self.isatk=False
        self.atkcount=0

    def isonblock_function(self):
        for box in blocklist:
            if self.hitbox[0]<box[2] and self.hitbox[2]>box[0]:
                if abs(self.hitbox[3]-box[1])<7:
                    self.whichonblock=box
                    self.isonblock=True

    def isunderblock_function(self):
        for box in blocklist:
            if self.hitbox[0]<box[2] and self.hitbox[2]>box[0]:
                if abs(self.hitbox[1]-box[3])<10:
                    self.isunderblock=True
                    self.whichunderblock=box

    def fall_function(self):
        if not(self.isjump) and self.y<350:

            if self.x>=665:
                if self.y<350:
                    man.fall=True

            if self.x>=590 and self.x<665:
                if self.y<230:
                    man.fall=True
                if self.hitbox[0]>block01[2] or self.hitbox[2]<block01[0]:
                    if self.y<350:
                        man.fall= True

            if self.x>=510 and self.x<590:
                if self.y<230:
                    man.fall=True
                if self.hitbox[0]+10>block02[2] or self.hitbox[2]<block02[0]:
                    if self.y<350:
                        man.fall= True

            if self.x>=450 and self.x<510:
                if self.y<185:
                    man.fall=True
                if self.hitbox[0]>block03[2] or self.hitbox[2]<block03[0]:
                    if self.y<214:
                        man.fall= True

            if self.x>=390 and self.x<450:
                if self.y<135:
                    man.fall=True
                if self.hitbox[0]>block04[2] or self.hitbox[2]<block04[0]:
                    if self.y<156:
                        man.fall= True

            if self.x>=330 and self.x<390:
                if self.hitbox[0]>block05[2] or self.hitbox[2]<block05[0]:
                    if self.y<80:
                        man.fall= True

            if self.x>=270 and self.x<330:
                if self.y<350:
                    man.fall=True

            if self.x<270:
                if self.y<170:
                    man.fall=True

    def fall_function_corta(self):
        self.fall_function()
        if not(self.fall):
            self.fallcount=8
        if self.fall:
            self.y+=self.fallcount
            self.fallcount+=3
            self.fall=False

    def gethit(self):
        if not (self.isatk):
            if self.hitbox[0]<enemy.hitbox[2] and self.hitbox[2]-10>enemy.hitbox[0]:
                self.lives-=1
                self.x=50
                self.y=350
                if self.lives==0:
                    self.canmove=False
                    self.sconfitta=True
        if self.isatk:
            if self.hitbox[0]-40<enemy.hitbox[2] and self.hitbox[2]>enemy.hitbox[0]:
                enemy.dead=True

    def elevator_function(self):
        if self.y<350 and self.jumpcount==8:
            if self.hitbox[0]+15>pltfrm_hitbox[0] and self.hitbox[2]+5<pltfrm_hitbox[2]:
                if self.pltfrm_y>145:
                    self.canmove=False
                    self.pltfrm_y-=3
                    man.standing=True
                    man.walkcount=0
                else:
                    self.canmove=True

    def forziere_function(self):
        man.canmove=False
        self.forziere_wait+=1
        man.movekey=True
        if man.key_x<490:
            man.key_x+=2
        if self.forziere_wait%10==0 and self.forziere_count!=5:
            self.forziere_count+=1
        if self.forziere_count==5:
            self.vittoria=True
            self.canmove=False

    def sconfitta_function(self):
        self.sconfitta=True
        self.canmove=False
        if self.sconfitta_count<6:
            screen.blit(sconfitta[self.sconfitta_count], (100, 100))
            self.sconfitta_contatore+=1
            if self.sconfitta_contatore%10==0:
                self.sconfitta_count+=1



enemy=Enemy(1, 168, 74, 85)
man=player(50, 350, 33, 64)#50, 350

def disegna():
    screen.blit(bg, (0, 0))
    screen.blit(ground01, (-1, 414))

    if not(man.isatk):
        man.draw(screen)
    if man.isatk:
        man.atk(screen)

    if not(enemy.dead) and enemy.drawenemy:
        enemy.draw(screen)
    if enemy.dead and enemy.drawenemy:
        if enemy.deathcount<20:
            if enemy.facing==1:
                screen.blit(edeathr[enemy.deathcount//5], (enemy.x, enemy.y))
            if enemy.facing==-1:
                screen.blit(edeathl[enemy.deathcount//5], (enemy.x, enemy.y))
            enemy.deathcount+=1
        if enemy.deathcount==20:
            enemy.drawenemy=False

    screen.blit(ground03, (0, 250))

    screen.blit(block, (640, 310))
    screen.blit(block, (540, 310))
    screen.blit(block, (480, 265))
    screen.blit(block, (420, 210))
    screen.blit(block, (360, 165))

    for count in range(man.lives):
        screen.blit(cuore, (630+(50*count), 30))

    if contatore<=7:
        screen.blit(key01, (enemy.x-10, enemy.y-40))
    if contatore>7 and contatore<=14:
        screen.blit(key02, (enemy.x-4, enemy.y-35))
    if contatore>14 and contatore<=21:
        screen.blit(key03, (enemy.x+2, enemy.y-30))
    if contatore>21 and contatore<=28:
        screen.blit(key04, (enemy.x+8, enemy.y-25))
    if contatore>28 and contatore<=35:
        screen.blit(key05, (enemy.x+14, enemy.y-18))

    if not(enemy.drawenemy):

        if man.contatore_chiave<=7:
            screen.blit(key05, (man.x+14, man.y-18))
        if man.contatore_chiave>7 and man.contatore_chiave<=14:
            screen.blit(key04, (man.x+8, man.y-25))
        if man.contatore_chiave>14 and man.contatore_chiave<=21:
            screen.blit(key03, (man.x+2, man.y-30))
        if man.contatore_chiave>21 and man.contatore_chiave<=28:
            screen.blit(key02, (man.x-4, man.y-35))
        if man.contatore_chiave>28:
            screen.blit(ground02, (80, 150))
            screen.blit(pltfrm, (30, man.pltfrm_y))
            screen.blit(forziere[man.forziere_count], (500, 113))

            if not(man.movekey):
                screen.blit(key01, (man.x-10, man.y-40))
            if man.movekey:
                screen.blit(key01, (man.key_x, man.y-40))
        man.contatore_chiave+=1

    if man.sconfitta:
        screen.blit(sconfitta[man.sconfitta_count], (man.sconfitta_x, man.sconfitta_y))
        man.sconfitta_contatore+=1
        if man.sconfitta_contatore%5==0:
            if man.sconfitta_count<6:
                man.sconfitta_x-=25
                man.sconfitta_count+=1

    if man.vittoria:
        screen.blit(vittoria[man.vittoria_count], (man.vittoria_x, man.vittoria_y))
        man.vittoria_contatore+=1
        if man.vittoria_contatore%5==0:
            if man.vittoria_count<6:
                man.vittoria_x-=25
                man.vittoria_count+=1

    pygame.display.update()


while True:
    clock.tick(30)

    keys=pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            break

    #per ogni comando sulle x, comparo l'hitbox con quelle del blocco e la stessa cosa per le y

    if keys[pygame.K_LEFT] and man.canmove:
        man.fall_function_corta()
        for box in blocklist:
            if man.hitbox[1]<box[3] and man.hitbox[3]>box[1]:#le y
                if man.hitbox[0]-man.vel<box[2] and man.hitbox[2]>box[0]:
                    man.moveleft*=-1
        if man.moveleft==1:
            man.left=True
            man.right=False
            man.x-=man.vel
            man.standing=False

        man.moveleft=1


    if keys[pygame.K_RIGHT] and man.canmove:
        man.fall_function_corta()
        for box in blocklist:
            if man.hitbox[1]<box[3] and man.hitbox[3]>box[1]:
                if man.hitbox[0]<box[2] and man.hitbox[2]+30>box[0]:
                    man.moveright*=-1
        if man.moveright==1:
            man.right=True
            man.left=False
            man.standing=False
            man.x+=man.vel
        man.moveright=1

    if keys[pygame.K_UP] and man.canmove:
        if man.waitjump>15:
            man.isjump=True
            man.waitjump=0

    if man.isjump:

        #parte da terra e sale sul primo blocco eventualmente

        if man.jumpcount>=-8:

            man.y-=(man.jumpcount*abs(man.jumpcount)) / 2
            man.jumpcount-=1
            man.isonblock_function()
            man.isunderblock_function()

            if man.isonblock:
                man.y=man.whichonblock[1]-man.height-20
                man.isjump=False
                man.jumpcount=8
                man.isonblock=False

            if man.isunderblock:
                man.y=350
                man.isjump=False
                man.jumpcount=8
                man.isunderblock=False
        else:
            man.isjump=False
            man.jumpcount=8

    if keys[pygame.K_SPACE] and man.canmove:
        if man.waitatk>25:
            man.isatk=True
            man.waitatk=0

    if not(keys[pygame.K_RIGHT]) and not(keys[pygame.K_LEFT]) and not(keys[pygame.K_UP]):
        man.fall_function_corta()
        man.standing=True
        man.walkcount=0

    man.waitatk+=1
    man.waitjump+=1

    if man.y>340:
        man.y=350

    if man.x<300 and man.y<350 and man.jumpcount==8:
        if not(enemy.dead):
            man.gethit()

    contatore+=1

    if enemy.dead:
        man.elevator_function()
        man.y=man.pltfrm_y-65
        if man.hitbox[2]>465:
            man.forziere_function()

    disegna()

pygame.quit()
