import pygame
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
pygame.init()
win = pygame.display.set_mode((500,480))
pygame.display.set_caption('First Game')
x = 50
y = 400
width = 40
hight = 60
vel = 7
isjump = False
jumpcnt = 10
run = True
right = False
left = False
walkcount = 0
clk = pygame.time.Clock()
def redrowgamewindow():
    global walkcount
    win.blit(bg , (0,0))
    if walkcount + 1 > 27 :
        walkcount = 0
        win.blit(walkRight[walkcount//3],(x,y))
    if left:
        win.blit(walkLeft[walkcount//3] , (x,y))
        walkcount +=1
    elif right :
        win.blit(walkRight[walkcount//3] , (x,y))
        walkcount +=1
    pygame.display.update()

while run:
    
    clk.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel-1:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x<500-vel-width+1:
        x += vel
        left = False
        right = True
    else :
        left = False
        right = False
        walkcount = 0
    if not isjump:
        
        if  keys[pygame.K_SPACE]:
            isjump = True
            left = False
            right = False
            walkcount = 0
    else:
        if jumpcnt >= -10:
            neg = 1
            if jumpcnt < 0 :
                 neg = -1 
                
            y -= (jumpcnt ** 2)*0.5 * neg
            jumpcnt -= 1
        else:
            isjump = False
            jumpcnt = 10
      
    redrowgamewindow()
pygame.quit()
