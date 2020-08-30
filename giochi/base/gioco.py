import pygame
pygame.init()

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

bulletsound=pygame.mixer.Sound('bullet.wav')
hitsound=pygame.mixer.Sound('hit.wav')
music=pygame.mixer.music.load('music.wav')

pygame.mixer.music.play(-1)#in loop

screen_width=852
screen_height=480
screen=pygame.display.set_mode((screen_width, screen_height))
score=0
shoot_loop=0


class enemy(object):
    walkLeft=[pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]
    walkRight=[pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x=x
        self.y=y
        self.width=width
        self.end=end
        self.path=[self.x, self.end]
        self.walk_count=3
        self.vel=3
        self.health=9
        self.visible=True
        self.hitbox=(self.x+17, self.y+3, 30, 55)
        
    def draw(self, screen):
        self.move()
        if self.visible:
            if self.walk_count+1>=28:
                self.walk_count=0
            if self.vel>0:
                screen.blit(self.walkRight[self.walk_count//3], (self.x, self.y))
                self.walk_count+=1
            else:
                screen.blit(self.walkLeft[self.walk_count//3], (self.x, self.y))
                self.walk_count+=1
            
            self.hitbox=(self.x+17, self.y+3, 30, 55)#rectangle: x, y, width, height
            #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
            pygame.draw.rect(screen, (255, 0, 0), (self.hitbox[0], self.hitbox[1]-20, 45, 10 ))
            pygame.draw.rect(screen, (0, 130, 0), (self.hitbox[0], self.hitbox[1]-20, self.health*5, 10 ))
    
    def move(self):
        if self.vel>0:
            if self.x+self.vel<self.path[1]:#almeno sarebbe appena prima di superare il confine
                self.x+=self.vel
            else:
                self.vel*=-1
                self.walkcount=0
        else:
            if self.x-self.vel>self.path[0]:
                self.x+=self.vel
            else:
                self.vel*=-1
                self.walk_count=0
    
    def hit(self):
    
        hitsound.play()
        
        if self.health>0:
            self.health-=1
        else:
            self.visible=False


class player(object):
    
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.left=False
        self.right=True
        self.walk_count=0
        self.isJump=False
        self.jump_count=10
        self.standing=True
        self.hitbox=(self.x+18, self.y+12, 26, 49)
    
    def draw(self, screen):
    
        if self.walk_count+1>=27:
            self.walk_count=0
            
        if not(man.standing):
            if self.left:
                screen.blit(walkLeft[self.walk_count//3], (self.x, self.y))
                self.walk_count+=1
            elif self.right:
                screen.blit(walkRight[self.walk_count//3], (self.x, self.y))
                self.walk_count+=1
        else:
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                screen.blit(walkLeft[0], (self.x, self.y))
        
        self.hitbox=(self.x+18, self.y+12, 26, 49)#rectangle: x, y, width, height
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
    
    def hit(self):
        self.x=60
        self.y=400
        self.walkcount=0
        self.isJump=False
        self.jump_count=10
        
        font1=pygame.font.SysFont('comicsams', 30)
        text1=font1.render('-5', 1, (255, 0, 0))
        screen.blit(text1, (250, 50))
        
        pygame.display.update()
            
        i=0
        while i < 100:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=301
                    pygame.quit()


class projectile(object):

    def __init__(self, x, y, radius, color, facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing#1 o -1
        self.vel=8*facing
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)



man=player(400, 400, 64, 64)
goblin=enemy(200, 406, 64, 64, 600)
run=True
clock=pygame.time.Clock()


def disegna():
    screen.blit(bg, (0, 0))
    text=font.render('score: '+str(score), 1, (255, 255, 255))
    screen.blit(text, (100, 50))
    for bullet in bullets:
        bullet.draw(screen)
    man.draw(screen)
    goblin.draw(screen)
    
    
    
    pygame.display.update()



bullets=[]
font=pygame.font.SysFont('comicsams', 30, True)


while run:
    clock.tick(27)#in disegna dividi per gli fps
    
    if man.hitbox[0]<goblin.hitbox[0]+goblin.hitbox[2] and man.hitbox[0]+man.hitbox[2]>goblin.hitbox[0] and goblin.visible:
        if man.hitbox[1]<goblin.hitbox[1]+goblin.hitbox[3] and man.hitbox[1]+man.hitbox[3]>goblin.hitbox[1]:#uso gli hitbox perchè sono più precisi
            man.hit()
            score-=5
    
    if shoot_loop>0:
        shoot_loop+=1
    if shoot_loop>3:
        shoot_loop=0#in questo modo posso sparare ogni 3 fps
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    keys=pygame.key.get_pressed()
    
    if goblin.visible:
        for bullet in bullets:
            if bullet.y - bullet.radius<goblin.hitbox[1]+goblin.hitbox[3] and bullet.y+bullet.radius>goblin.hitbox[1]:
                if bullet.x - bullet.radius>goblin.hitbox[0] and bullet.x + bullet.radius < goblin.hitbox[0]+goblin.hitbox[2]:
                    score+=1
                    bullets.remove(bullet)
                    goblin.hit()
    
    for bullet in bullets:
    
        if bullet.x<852 and bullet.x>0:
            bullet.x+=bullet.vel
        else:#the bullet is off the screen
            bullets.remove(bullet)
    
    if keys[pygame.K_SPACE] and shoot_loop==0:
        if len(bullets)<5:
            bulletsound.play()
            if man.left:
                facing=-1
            else:
                facing=1
            bullets.append(projectile(round(man.x+man.width//2), round(man.y+man.height//2), 5, (0, 0, 0), facing))
        shoot_loop=1
    
    if keys[pygame.K_LEFT] and man.x>man.vel:
        man.left=True
        man.right=False
        man.x-=man.vel
        man.standing=False
        
    elif keys[pygame.K_RIGHT] and man.x<screen_width-man.width-man.vel:
        man.right=True
        man.left=False
        man.x+=man.vel
        man.standing=False
    
    else:
        man.walk_count=0
        man.standing=True
    
    if not(man.isJump):#in questo modo non si sposta mentre salta
        if keys[pygame.K_UP]:
            man.isJump=True
            man.standin=True
            man.walk_count=0
            
    else:
        if man.jump_count>=-10:
            man.y-=(man.jump_count*abs(man.jump_count)) / 2
            man.jump_count-=1
        else:
            man.isJump=False
            man.jump_count=10
    disegna()
    


pygame.quit()