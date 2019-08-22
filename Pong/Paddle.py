import pygame


class paddle(pygame.Rect):

    def __init__(self, move_space, Key_up, Key_down , *args, **kwargs):
        self.move_space = move_space
        self.score = 0
        self.Key_up = Key_up
        self.Key_down = Key_down
        super().__init__(*args, **kwargs)

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score


    def move(self,screen_height):
        bottom_paddle = self.y + self.move_space
        top_paddle = screen_height - self.height
        top_screen = self.y - self.move_space
        key_push = pygame.key.get_pressed()

        if key_push[self.Key_down]:
            if bottom_paddle < top_paddle:
                self.y += self.move_space

        if key_push[self.Key_up]:
            if top_screen > 0:
                self.y -= self.move_space


    def reset_pos(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos

