import pygame

red = (255, 0, 0)
yellow = (255,255,0)
width = 500
height = 500



class Plqyer(pygame.sprite.Sprite):
    def init(self):
        pygame.sprite.Sprite.init(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (width/ 2, height/ 2)



    def update(self):
        if self.rect.left>width:
            self.rect.left = 0 
        
        if self.rect.right<0:
            self.rect.left=width
        
        if self.rect.top>height:
            self.rect.bottom = 0 

        if self.rect.bottom<0:
            self.rect.top = height

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        
        if keys[pygame.K_DOWN]:
            self.rect.y += 5



pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Новая игра")
all_sprites = pygame.sprite.Group()
player = Plqyer()
all_sprites.add(player)

running = True
while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill(red)
    all_sprites.draw(screen)

    pygame.display.flip()
pygame.quit()