import pygame
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
pygame.init()
win = pygame.display.set_mode((500,480))
pygame.display.set_caption('This man walks!')

class Person(object):
    def __init__(self, x , y ,width , hight , vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.width = width
        self.hight = hight
        self.isjump = False
        self.jumpcnt = 10
        self.run = True
        self.right = False
        self.left = False
        self.walkcount = 0

        
    def drow(self,win): 
        win.blit(bg , (0,0))
        if self.walkcount + 1 > 27 :
            self.walkcount = 0
            win.blit(walkRight[self.walkcount//3],(self.x,self.y))
        if man.left:
            win.blit(walkLeft[self.walkcount//3] , (self.x,self.y))
            self.walkcount += 1 
        elif man.right :
            win.blit(walkRight[self.walkcount//3] , (self.x,self.y))
            self.walkcount += 1
    

def redrowgamewindow():
    win.blit(bg , (0,0))
    man.drow(win)
    pygame.display.update()

        
man = Person(300,410,64,64,5)
clk = pygame.time.Clock()

while man.run: 
    clk.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            man.run = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and man.x  > man.vel - 1:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.vel - man.width+1:
        man.x += man.vel
        man.left = False
        man.right = True
    else :
        man.left = False
        man.right = False
        man.walkcount = 0
    if not man.isjump: 
        if  keys[pygame.K_SPACE]:
            man.isjump = True
            man.left = False
            man.right = False
            man.walkcount = 0
    else:
        if man.jumpcnt >= -10:
            neg = 1
            if man.jumpcnt < 0 :
                 neg = -1 
                
            man.y -= (man.jumpcnt ** 2)*0.5 * neg
            man.jumpcnt -= 1
        else:
            man.isjump = False
            man.jumpcnt = 10
      
    redrowgamewindow()
pygame.quit()
