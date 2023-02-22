import pygame
import random
FPS = 60
pygame.init()
size = width,height = 600,400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('game1')


def elka(x=190,y=300):
    pygame.draw.rect(screen,"#8B4513",(x,y,10,30))
    pygame.draw.polygon(screen, pygame.Color("#006400"), [(x-15,y), (x+25,y),(x+5,y-45)],0)

    
screen.fill("#d6b4c0")
screen.fill(pygame.Color("#d6b4c0"), (0,330,600,390))
pygame.draw.circle(screen,"yellow",(400,200),100)

for i in ("#0b9919","#82de2c","#437317","#e0ae2d","#4fa326","#40250d")*100000:
    x=random.randrange(1,600)
    y=random.randrange(330,600)
    pygame.draw.rect(screen,i,(x,y,2,2))

    
for i in range(20):
    elka(random.randrange(1,600), random.randrange(300,340))


pygame.display.update()
play = True
posx = 0
speed = 1
posy = 0
while play:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False


        screen.fill("#d6b4c0")



    pygame.draw.polygon( screen,(255, 22, 44), ( (0+posx, 100 + posy), (10+posx, 100+ posy), (10+posx,90+posy),(0+posx,90+posy)))  
    pressedkeys = pygame.key.get_pressed()

    if pressedkeys[pygame.K_LEFT]:
          posx -=speed
    elif pressedkeys[pygame.K_RIGHT]:
          posx +=speed
    if pressedkeys[pygame.K_UP]:
          posy -=speed      
    elif pressedkeys[pygame.K_DOWN]:
          posy +=speed



    pygame.display.update()
   
pygame.quit()