import pygame


class ball(pygame.Rect):

    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = 0
        super().__init__(*args, **kwargs)

    def increase_speed(self):
        self.velocity += 1

    def move_ball(self):
        self.y += self.angle
        self.x += self.velocity


    def get_velocity(self):
        return self.y

    def set_ball_pos(self,x_pos ,y_pos):
        self.x = x_pos
        self.y = y_pos


