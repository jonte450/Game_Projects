import pygame

class block:

    cube_width = 500
    cube_rows = 20

    def __init__(self,begin,direct_x=1, direct_y=0,color=(255,0,0)):
            self.direct_x = 1
            self.direct_y = 0
            self.color = color
            self.pos = begin

    def draw_block(self,screen,draw_eyes):
       distance = self.cube_width // self.cube_rows
       x = self.pos[0]
       y = self.pos[1]

       pygame.draw.rect(screen,self.color,(x*distance+1,y*distance+1,distance -3,distance-3))
       if draw_eyes:
           entre = distance // 2
           rad = 3
           middle_circle = (x*distance+entre-rad,y*distance+7)
           middle_circle_2 = (x*distance+distance-rad*2,y*distance+7)
           pygame.draw.circle(screen,(0,0,0),middle_circle,rad)
           pygame.draw.circle(screen,(0,0,0),middle_circle_2,rad)

    def move_block(self,direct_x,direct_y):
        self.direct_x = direct_x
        self.direct_y = direct_y
        self.pos = (self.pos[0]+self.direct_x,self.pos[1]+direct_y)
