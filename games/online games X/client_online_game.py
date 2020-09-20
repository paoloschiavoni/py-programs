import pygame
from network_online_game import Network

pygame.init()

width=500
height=500
win=pygame.display.set_mode((width, height))

pygame.display.set_caption('client')

client_number=0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.rect=(x, y, width, height)
        self.vel=3
    
    def update(self):
        self.rect=(self.x, self.y, self.width, self.height)

def read_pos(self, str):
    str=str.split(',')
    return int(str[0]), int(str(1))

def make_pos(self, tup):
    return str(tup[0])+','+str(tup[1])

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x-=self.vel
        if keys[pygame.K_RIGHT]:
            self.x+=self.vel
        if keys[pygame.K_DOWN]:
            self.y+=self.vel
        if keys[pygame.K_UP]:
            self.y-=self.vel

        self.update()

def redrawWindow(win, p, p2):
    win.fill((0, 0, 0))
    p.draw(win)
    p2.draw(win)
    pygame.display.update()

p=Player(50, 50, 100, 100, (0, 0, 255))

def main():
    run=True
    clock=pygame.time.Clock()
    n=Network()
    start_pos = read_pos(n.getPos())
    p=Player(start_pos[0], start_pos[1], 100, 100, (0, 0, 255))
    p2=Player(0, 0, 100, 100, (0, 0, 255))
    n=Network()
    startPos=read_pos(n.getPos())

    while run:
        clock.tick(60)

        p2_pos=read_pos(n.send(make_pos(p.x, p.y)))
        p2.x=p2_pos[0]
        p2.y=p2_pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
        p.move()
        
        redrawWindow(win, p)

main()