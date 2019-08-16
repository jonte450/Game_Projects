import pygame
import math
import sys

sys.path.append("../Snake_class")
from Block import block

class Snake:
     direction = dict()
     snake_body = []

     def __init__(self,color,pos):
         self.color = color
         self.start = block(pos)
         self.snake_body.append(self.start)
         self.direct_y = 1
         self.direct_x = 0

     def snake_move(self):
         counter = 0
         body_len = len(self.snake_body)
         for action in pygame.event.get():
           if action.type == pygame.QUIT:
               pygame.quit()

           commands = pygame.key.get_pressed()




           if commands[pygame.K_a]:
               self.direct_x = -1
               self.direct_y = 0
               self.direction[tuple(self.start.pos[:])] = [self.direct_x, self.direct_y]

           elif commands[pygame.K_s]:
               self.direct_x = 1
               self.direct_y = 0
               self.direction[tuple(self.start.pos[:])] = [self.direct_x, self.direct_y]

           elif commands[pygame.K_w]:
               self.direct_x = 0
               self.direct_y = -1
               self.direction[tuple(self.start.pos[:])] = [self.direct_x, self.direct_y]

           elif commands[pygame.K_z]:
               self.direct_x = 0
               self.direct_y = 1
               self.direction[tuple(self.start.pos[:])] = [self.direct_x, self.direct_y]




           counter = 0
           while counter < body_len:
               check_block = self.snake_body[counter].pos[:]
               if tuple(check_block) in self.direction:
                   dir = self.direction[tuple(check_block)]
                   self.snake_body[counter].move_block(dir[0],dir[1])
                   if counter == body_len -1:
                       self.direction.pop(tuple(check_block))
               else:
                   if self.snake_body[counter].direct_x == -1 and self.snake_body[counter].pos[0] <= 0:
                       self.snake_body[counter].pos = [self.snake_body[counter].cube_rows-1,self.snake_body[counter].pos[1]]
                   elif self.snake_body[counter].direct_x == 1 and self.snake_body[counter].pos[0] >= (self.snake_body[counter].cube_rows-1):
                       self.snake_body[counter].pos = [0,self.snake_body[counter].pos[1]]
                   elif self.snake_body[counter].direct_y == 1 and self.snake_body[counter].pos[1] >= (self.snake_body[counter].cube_rows-1):
                       self.snake_body[counter].pos = [self.snake_body[counter].pos[0],0]
                   elif self.snake_body[counter].direct_y == -1 and self.snake_body[counter].pos[1] <= 0:
                       self.snake_body[counter].pos = [self.snake_body[counter].pos[0],self.snake_body[counter].cube_rows-1]
                   else:
                       self.snake_body[counter].move_block(self.snake_body[counter].direct_x,self.snake_body[counter].direct_y)
               counter += 1

     def draw_snake(self,screen):
              counter = 0
              while counter < len(self.snake_body):
                  check_block = self.snake_body[counter]
                  if counter == 0:
                      check_block.draw_block(screen,True)
                  else:
                      check_block.draw_block(screen,False)
                  counter += 1

     def build_snake(self):
         last_part = self.snake_body[-1]
         last_x = last_part.direct_x
         last_y = last_part.direct_y

         if last_x == 1 and last_y == 0:
             self.snake_body.append(block((last_part.pos[0]-1,last_part.pos[1])))
         elif last_x == -1 and last_y == 0:
             self.snake_body.append(block((last_part.pos[0]+1,last_part.pos[1])))
         elif last_x == 0 and last_y == 1:
             self.snake_body.append(block((last_part.pos[0],last_part.pos[1]-1)))
         elif last_x == 0 and last_y == -1:
             self.snake_body.append(block((last_part.pos[0],last_part.pos[1]+1)))

         self.snake_body[-1].direct_x = last_x
         self.snake_body[-1].direct_y = last_y

     def reset_snake(self,pos):
         self.start = block(pos)
         self.snake_body = []
         self.snake_body.append(self.start)
         self.direct_x = 1
         self.direct_y = 0
         self.direction = dict()
