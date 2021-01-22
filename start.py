import pygame
import json 
import os
from main import main
from components.button import Button
from login import login

def start():
    pygame.init()

    json_file = open(os.getcwd()+r"\components\constants.json", "r")
    json_content = json.load(json_file)
    round_int = json_content["round_int"]
    json_file.close()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    font = pygame.font.SysFont("DejaVu Sans", 30)
    # RED = (255, 0, 0), GREEN = (0, 255, 0), BLUE = (0, 0, 255)

    
    screen = pygame.display.set_mode((720, 480))
    screen.fill(WHITE)
    
    clock = pygame.time.Clock()

    choose_label = font.render("Choose a gamemode", 1, BLACK)

    screen.blit(choose_label, (200, 60))

    button_standard =   Button(screen, 100, 200, 200, 100, BLACK, WHITE, lambda:[login("STANDARD")], 'STANDARD')
    button_960 =        Button(screen, 400, 200, 200, 100, BLACK, WHITE, lambda:[login("CHESS 960")], 'CHESS 960')

    buttons = [button_standard, button_960]
    for button in buttons:
        button.draw()
    pygame.display.update()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            for button in buttons:
                button.checkClick(event)

            


if __name__ == "__main__":
    start()    