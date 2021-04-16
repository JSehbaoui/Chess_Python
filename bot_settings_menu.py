import pygame
import json 
import os
from pygame_widgets import Slider
from main import main
from components.entry_boy import InputBox
from components.button import Button


def settings(mode = 'STANDARD'):
    pygame.init()

    json_file = open(os.getcwd()+r"\components\constants.json", "r")
    json_content = json.load(json_file)
    round_int = json_content["round_int"]
    json_file.close()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (100, 100, 100)
    BROWN = (138, 79, 28)
    font = pygame.font.SysFont("DejaVu Sans", 30)
    # RED = (255, 0, 0), GREEN = (0, 255, 0), BLUE = (0, 0, 255)

    
    screen = pygame.display.set_mode((720, 480))
    screen.fill(BROWN)
    
    clock = pygame.time.Clock()

    pygame.display.update()

    title_label = font.render(mode, True, BLACK)


    Player1_label = font.render("Player 1:", True, BLACK)
    Player2_label = font.render("AI Difficuly:", True, BLACK)

    Player1 = InputBox(345, 200, 120, 32, WHITE, GREY)
    bot_diff = Slider(screen, 350, 260, 120, 15, min=1, max=20, step=1, initial= 6)

    
    Accept_Button = Button(x = 300,
                           y = 300,
                           w = 100,
                           h = 50,
                           color_b = BLACK,
                           color_in = WHITE,
                           color_t = WHITE, 
                           command = lambda:[main(player1 = Player1.export(), player2= 'Computer', mode=mode, bot_bool = True, bot_difficulty=bot_diff.getValue())],
                           text = 'Start Game'
                           )
  
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            
            Player1.checkActivation(event)
            bot_diff.listen(event)

            Accept_Button.processEvent(event)

            screen.fill(BROWN)
            screen.blit(Player1_label, (150, 200))
            screen.blit(Player2_label, (150, 250))
            screen.blit(title_label, (pygame.display.get_window_size()[0]/2 - title_label.get_rect().w/2, 30))
            Player1.draw(screen)
            bot_diff.draw()
            
            Accept_Button.draw(screen)

            pygame.display.flip()

            

if __name__ == "__main__":
    settings()    