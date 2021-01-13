# import pygame
# import math

# pygame.init()

# screen_size = (800, 800)

# SCREEN = pygame.display.set_mode(screen_size)
# pygame.display.set_caption("Chess")

# clock = pygame.time.Clock()

# newx = 0
# speed = 3

# start_pos_x = 70
# start_pos_y = 70
# stop_pos_x = 120
# stop_pos_y = 120

# # how do I move a circle to this exact spot with a velocity that adapts to the distance traveled

# def animate(start_pos_x, start_pos_y, stop_pos_x, stop_pos_y, time):
#     newx = 0
#     newy = 0
#     counter = 0
#     clocktick = 30
#     time = time* clocktick

#     while counter <= time:

#         clock.tick(clocktick)

#         dis_vec_x = stop_pos_x-start_pos_x
#         dis_vec_y = stop_pos_y-start_pos_y

#         speed_x = dis_vec_x/time
#         speed_y = dis_vec_y/time  

#         pygame.draw.rect(SCREEN, (0,0,0), [0,0,800,800])
#         pygame.draw.circle(SCREEN, (255, 255, 255), (newx+start_pos_x, newy+start_pos_y), 30)
#         pygame.draw.circle(SCREEN, (255,0,0), (stop_pos_x, stop_pos_y), 30)
#         pygame.display.update()
#         newx+= speed_x
#         newy+= speed_y
#         counter += 1
    
# animate(40, 500, 40, 200, 2)

# print(chr('a'))

import pygame
import datetime
import time
import os

# pygame.init()

# screen_size = (800, 800)

# SCREEN = pygame.display.set_mode(screen_size)
# pygame.display.set_caption("Chess")

# clock = pygame.time.Clock()
# while True:
# print(datetime.time(5,30,50))

# for minutes in range(5):
#     for seconds in range(59):
#         print(str(datetime.time(0,4-minutes, 59-seconds))[3:])
#         time.sleep(1)
#         os.system('cls')

print(str(datetime.datetime.now())[11:19])

