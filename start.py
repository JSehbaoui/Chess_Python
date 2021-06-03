import pygame
import json 
import os

from pygame import display
from main import main
from components.button import Button
from intermediary import intermediary
from components.switch import TickBox

def start():
    pygame.init()

    json_file = open(os.getcwd()+r"\components\constants.json", "r")
    json_content = json.load(json_file)
    round_int = json_content["round_int"]
    json_file.close()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BROWN = (138, 79, 28)
    font_large = pygame.font.SysFont("DejaVu Sans", 30)
    font_small = pygame.font.SysFont("DejaVu Sans", 22)
    
    screen = pygame.display.set_mode((720, 480))
    screen.fill(BROWN)
    
    clock = pygame.time.Clock()

    choose_label = font_large.render("Choose a gamemode", 1, BLACK)
    screen.blit(choose_label, (200, 60))

    bot_box = TickBox(posx = 320, posy = 350, size = 30)
    button_standard =   Button(x = 100,
                               y = 200,
                               w = 200,
                               h = 100, 
                               color_b = BLACK,
                               color_in = WHITE,
                               color_t = WHITE,
                               command = lambda: [intermediary(bot = bot_box.getStatus(), mode = "STANDARD")],
                               text = 'STANDARD'
                               )

    button_960 =        Button(x = 400,
                               y = 200,
                               w= 200,
                               h= 100,
                               color_b = BLACK,
                               color_in = WHITE,
                               color_t = WHITE,
                               command = lambda:[intermediary(bot = bot_box.getStatus(), mode = "CHESS 960")],
                               text = 'CHESS 960'
                               )
    

    bot_label = font_small.render("Play against AI", 1, BLACK)
    screen.blit(bot_label, (120, 350))

    items = [button_standard, button_960, bot_box]
    for item in items:
        item.draw(screen = screen)
    pygame.display.update()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            for item in items:
                item.processEvent(event)

            bot_box.draw(screen)
        
        pygame.display.flip()


if __name__ == "__main__":
    start()    