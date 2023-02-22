
import pygame
import sys
import random
import time


class Game():
    def __init__(self):

        self.screen_width = 720
        self.screen_height = 460

  
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)

        self.fps_controller = pygame.time.Clock()

        self.score = 0

    def init_and_check_for_errors(self):
        """стартовая позиция, иницилизирующая все послежущее мувы при этом нельзя муувить на 200процентов, иначе все улетит за дисплей"""
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Ok')

    def set_surface_and_title(self):
        """Задаем surface(поверхность поверх которой будет все рисоваться)
        и устанавливаем загаловок окна"""
        self.play_surface = pygame.display.set_mode((
            self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake Game')

    def event_loop(self, change_to):
        """Функция для отслеживания нажатий клавиш игроком"""

        # запускаем цикл по ивентам
        for event in pygame.event.get():
            # если нажали клавишу
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = "DOWN"
                # нажали escape
                #ringhqedahndnxfycnv bgfdgbmewt
                #ifd pruint('ya_dublin)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return change_to

    def refresh_screen(self):
        """обновляем экран и задаем фпс"""
        pygame.display.flip()
        game.fps_controller.tick(20)

    def show_score(self, choice=1):
        """показываем результат"""
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render(
            'Score: {0}'.format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        # дефолт случ отображаем результат слева сверху
        if choice == 1:
            s_rect.midtop = (80, 10)
        # при game_overe отображаем результат по центру
        # под надписью game over
        else:
            s_rect.midtop = (360, 120)
        # рисуем прямоугольник поверх та
        self.play_surface.blit(s_surf, s_rect)

    def game_over(self):
        """Функция для вывода надписи Game Over и результатов
        в случае завершения игры и выход из игры"""
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Game over', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.play_surface.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
class Snake():
    def __init__(self, snake_color):
        # важные переменные это позиция головы змеи и его тела
        self.snake_head_pos = [100, 50]  
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_color = snake_color

        self.direction = "RIGHT"

        self.change_to = self.direction

    def validate_direction_and_change(self):
        """Изменияем направление движения змеи только в том случае,
        если оно не прямо противоположно текущему"""
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

    def change_head_position(self):
        """Изменияем положение головы змеи"""
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 10
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 10

    def snake_body_mechanism(
            self, score, food_pos, screen_width, screen_height):

        self.snake_body.insert(0, list(self.snake_head_pos))
        # если съели еду
        if (self.snake_head_pos[0] == food_pos[0] and
                self.snake_head_pos[1] == food_pos[1]):
            # если съели еду то задаем новое положение еды случайным
            # образом и увеличивем score на один
            food_pos = [random.randrange(1, screen_width/10)*10,
                        random.randrange(1, screen_height/10)*10]
            score += 1
        else:
            # что будет если нет еды
            # что будет если еда есто
            self.snake_body.pop()
        return score, food_pos
        #print("8if so")

    def draw_snake(self, play_surface, surface_color):
        """Отображаем все сегменты змеи"""
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(
                play_surface, self.snake_color, pygame.Rect(
                    pos[0], pos[1], 10, 10))

    def check_for_boundaries(self, game_over, screen_width, screen_height):
        """Проверка, что столкунлись с концами экрана или сами с собой
        (змея закольцевалась)"""
        if any((
            self.snake_head_pos[0] > screen_width-10
            or self.snake_head_pos[0] < 0,
            self.snake_head_pos[1] > screen_height-10
            or self.snake_head_pos[1] < 0
                )):
            game_over()
        for block in self.snake_body[1:]:
            # елси змейка врезалась
            # то что будеь
            if (block[0] == self.snake_head_pos[0] and
                    block[1] == self.snake_head_pos[1]):
                game_over()


class Food():
    def __init__(self, food_color, screen_width, screen_height):
        """еду"""
        self.food_color = food_color
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [random.randrange(1, screen_width/10)*10,
                         random.randrange(1, screen_height/10)*10]

    def draw_food(self, play_surface):
        """вид еды"""
        pygame.draw.rect(
            play_surface, self.food_color, pygame.Rect(
                self.food_pos[0], self.food_pos[1],
                self.food_size_x, self.food_size_y))
            #print if an


game = Game()
snake = Snake(game.green)
food = Food(game.brown, game.screen_width, game.screen_height)

game.init_and_check_for_errors()
game.set_surface_and_title()
#print("if smth_pupil jkvsb ckjchc ")
while True:
    #if something or change
    snake.change_to = game.event_loop(snake.change_to)

    snake.validate_direction_and_change()
    snake.change_head_position()
    game.score, food.food_pos = snake.snake_body_mechanism(
        game.score, food.food_pos, game.screen_width, game.screen_height)
    snake.draw_snake(game.play_surface, game.white)

    food.draw_food(game.play_surface)

    snake.check_for_boundaries(
        game.game_over, game.screen_width, game.screen_height)

    game.show_score()
    game.refresh_screen()
    #print("Arseny av ")
    #a = input("sn")