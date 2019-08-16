import pygame
import sys
import math
import tkinter as box
from tkinter import messagebox
from Snake_class import Snake as sn

from Block import block as bl

from Random_Snack import create_snack_pos




def update_screen(screen):
   global food,ss,screen_w,screen_r
   screen.fill((0,0,0))
   ss.draw_snake(screen)
   food.draw_block(screen,False)
   draw_screen(screen)
   pygame.display.update()

def draw_screen(screen):
     screen_size = screen_w // screen_r
     x_pos = 0
     y_pos = 0
     counter = 0
     while counter < screen_r:
         x_pos += screen_size
         y_pos += screen_size
         pygame.draw.line(screen,(250,250,250),(x_pos,0),(x_pos,screen_w))
         pygame.draw.line(screen,(250,250,250),(0,y_pos),(screen_w,y_pos))
         counter += 1


def send_message(send_to,to_say):
    begin = box.Tk()
    begin.attributes("-topmost",True)
    begin.withdraw()
    messagebox.showinfo(send_to,to_say)
    try:
        begin.destroy()
    except:
        pass

def check_collide(index,body_part,body_list):
    while index < len(body_list):
        check = body_list[index]
        if body_part.pos == check.pos:
            return True
        index += 1
    return False

def main():
    global food,ss,screen_w,screen_r
    screen_w = 500
    screen_r = 20
    ss = sn((255,0,0),(10,10))
    position = create_snack_pos(ss)
    food = bl(position,color = (0,0,255))
    win = pygame.display.set_mode((screen_w,screen_w))
    game_continue = True
    time = pygame.time.Clock()

    while game_continue:
        pygame.time.delay(50)
        time.tick(10)
        ss.snake_move()
        if ss.snake_body[0].pos == food.pos:
            ss.build_snake()
            food = bl(create_snack_pos(ss),color = (0,0,255))
        counter = 0
        while counter < len(ss.snake_body):
            if check_collide(counter+1,ss.snake_body[counter],ss.snake_body):
                print("Your score: ")
                print(len(ss.snake_body))
                send_message("Sorry you lost!" , "You can play again...")
                ss.reset_snake((10,10))
                break
            counter += 1

        update_screen(win)


    pass
main()
