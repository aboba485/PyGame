import pygame
import sys



FPS = 180
pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('pinga-ponga')


# тут мы рисуем круг

score = 0
black = 0, 0, 0
white = 255, 255, 255
green = 0, 0, 255
orange = 125, 125, 0
screen.fill(white)

pygame.display.update()
play = True
posx = 0
speed_plus = 1.3
speed_minus = 0.7
posy = 0
x_ball = 300
y_ball = 200
naprav_x = 1
naprav_y = 1
speed_of_the_ball = 1
pl = pygame.Rect((250, 330, 120, 20))
pl1 = pygame.Rect((260, 0, 80, 10))

#def show_score(self, choice=1):
#    """показываем результат"""
##   s_font = pygame.font.SysFont('monaco', 24)
#  s_surf = s_font.render(
#        'Score: {0}'.format(self.score), True, self.black)
#    s_rect = s_surf.get_rect()
#    # дефолт случ отображаем результат слева сверху
#    if choice == 1:
#        s_rect.midtop = (80, 10)
    # при game_overe отображаем результат по центру
    # под надписью game over
    #else:
        #s_rect.midtop = (360, 120)
    # рисуем прямоугольник поверх та
    #self.play_surface.blit(s_surf, s_rect)

def game_over(screen):
    """Функция для вывода надписи Game Over и результатов
    в случае завершения игры и выход из игры"""
    go_font = pygame.font.SysFont('monaco', 72)
    go_surf = go_font.render('Game over', score , True, 'red')
    go_rect = go_surf.get_rect()
    go_rect.midtop = (300, 130)
    screen.blit(go_surf, go_rect)
    pygame.display.flip()
    pygame.time.delay(1000)
    pygame.quit()
    sys.exit()

while play:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    screen.fill(white)

    pygame.draw.circle(screen, (black), (x_ball, y_ball), 10)
    x_ball += speed_of_the_ball*naprav_x
    y_ball += speed_of_the_ball*naprav_y

    # отрисовка платформы
    pygame.draw.rect(screen, (black), pl)

    #отрисовка овала
    pygame.draw.rect(screen,(black),pl1)

    # движение платформы
    pressedkeys = pygame.key.get_pressed()
    if pressedkeys[pygame.K_LEFT]:
        pl.x -= speed_minus
    elif pressedkeys[pygame.K_RIGHT]:
        pl.x += speed_plus
    if pl.x >= 560:
        pl.x = 0
    elif pl.x <= 0:
        pl.x = 480




#--------------------------------------------------


#Это если удар был о правильную штуку

    if  260<=x_ball<=340:
        score+=1
        

#-------------------------------------------------- 

    # удар о бортики
    if x_ball >= 590:
        # Меняем направление при ударе о левый бок
        naprav_x = naprav_x*-1
        #о левый бок
    elif x_ball <= 10:
        naprav_x = naprav_x*-1
        #о верхний бок
    elif y_ball <= 10:
        naprav_y = naprav_y*-1

    elif y_ball >= 390:
        game_over(screen)
    elif pl.x <= x_ball <= pl.x+120 and 330 <= y_ball <= 350 or 330<=y_ball<=350 and pl.x <= x_ball <=pl.x+1 or 330<=y_ball<=350 and pl.x <= x_ball<=pl.x+120 and pl.x+119<=x_ball<=pl.x+120:
        naprav_y = naprav_y*-1
        if pressedkeys[pygame.K_RIGHT]:
            naprav_x = naprav_x*1
        else:
            naprav_x = naprav_x*1
        speed_of_the_ball=speed_of_the_ball*1.05
        speed_plus = speed_plus*1.009
        speed_minus = speed_minus*0.009




    pygame.display.update()

pygame.quit()