import random


def check_body(x_pos,y_pos,body_list):
    counter = 0
    create_list = []
    create_list.append(x_pos)
    create_list.append(y_pos)
    target = tuple(create_list)
    for check in body_list:
        if check.pos == target:
            counter += 1
    return counter

def create_snack_pos(Snake):
    body_parts = Snake.snake_body
    while 1:
        x_pos = random.randrange(20)
        y_pos = random.randrange(20)
        occur = check_body(x_pos,y_pos,body_parts)
        if occur > 0:
            continue
        else:
            break
    return (x_pos,y_pos)
