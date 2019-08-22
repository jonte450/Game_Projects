import pygame
import random
from Ball import ball
from Paddle import paddle

class Pong:

    screen_height = 500
    screen_width = 900

    paddle_h = 100
    paddle_w = 10

    ball_a = 0
    ball_speed = 1
    ball_w = 10
    paddle_color = (0,255,0)
    paddle_velocity = 13


    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.time = pygame.time.Clock()
        self.Balls = []

    def add_ball(self):
        self.Balls.append(ball(self.ball_speed, random.randint(0,self.screen_width),random.randint(0,self.screen_height),self.ball_w,self.ball_w))

    def reset_game(self):
        global paddle_1, paddle_2
        paddle_1.reset_pos(0, self.screen_height / 2 - self.paddle_h)
        paddle_2.reset_pos(self.screen_width-self.paddle_w, self.screen_height / 2 - self.paddle_h / 2)
        self.add_ball()
        for ball in self.Balls:
            ball.increase_speed()

    def check_walls(self):
        global paddle_1, paddle_2
        index = 0
        while index < len(self.Balls):

            if self.Balls[index].x < 0:
                paddle_2.increase_score()
                self.Balls[index].set_ball_pos(random.randint(0,self.screen_width),random.randint(0,self.screen_height))
                self.reset_game()
                break

            if self.Balls[index].x > self.screen_width:
                paddle_1.increase_score()
                self.Balls[index].set_ball_pos(random.randint(0,self.screen_width),random.randint(0,self.screen_height))
                self.reset_game()
                break

            if self.Balls[index].y > self.screen_height - self.ball_w or self.Balls[index].y < 0:
                self.Balls[index].angle = -self.Balls[index].angle

            index += 1

    def check_paddle(self):
        global paddle_1, paddle_2
        index = 0
        while index < len(self.Balls):
            #Left Paddle
            if self.Balls[index].colliderect(paddle_1):
                self.Balls[index].velocity = -self.Balls[index].velocity
                self.Balls[index].angle = random.randint(-10,10)
            #Right Paddle
            if self.Balls[index].colliderect(paddle_2):
                self.Balls[index].velocity = -self.Balls[index].velocity
                self.Balls[index].angle = random.randint(-10, 10)
            index += 1


    def move_balls(self):
        index = 0
        while index < len(self.Balls):
            self.Balls[index].move_ball()
            pygame.draw.rect(self.window,(0,255,255),self.Balls[index])
            index += 1


    def start_game(self):
        global paddle_1, paddle_2
        paddle_1 = paddle(self.paddle_velocity,pygame.K_w,pygame.K_s,0,self.screen_height / 2 - self.paddle_h / 2,self.paddle_w,self.paddle_h)
        paddle_2 = paddle(self.paddle_velocity,pygame.K_i, pygame.K_k, self.screen_width-self.paddle_w, self.screen_height / 2 - self.paddle_h / 2,self.paddle_w, self.paddle_h)
        font = pygame.font.SysFont("comicsansms", 25)

        self.add_ball()

        while True:
            for action in pygame.event.get():
                if action.type == pygame.QUIT:
                    pygame.quit()
            print(len(self.Balls))
            self.check_paddle()
            self.check_walls()

            self.window.fill((0,0,0))

            text1 = font.render("Player one: " + str(paddle_1.get_score()), True, (0, 128, 0))
            text2 = font.render("Player two: " + str(paddle_2.get_score()), True, (0, 128, 0))
            self.window.blit(text1, (0,self.screen_height-20))
            self.window.blit(text2, (self.screen_width-115, self.screen_height-20))

            paddle_1.move(self.screen_height)
            pygame.draw.rect(self.window,self.paddle_color,paddle_1)

            paddle_2.move(self.screen_height)
            pygame.draw.rect(self.window,self.paddle_color,paddle_2)

            self.move_balls()
            pygame.draw.rect(self.window,(255,0,255),pygame.Rect(self.screen_width/2,0,1,self.screen_height))

            pygame.display.flip()
            self.time.tick(50)
