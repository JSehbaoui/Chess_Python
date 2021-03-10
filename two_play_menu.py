import pygame
import json 
import os
from main import main
from components.entry_boy import InputBox
from components.button import Button

def login(mode = 'STANDARD'):
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

    pygame.display.update()

    title_label = font.render(mode, True, BLACK)


    Player1_label = font.render("Player 1:", True, BLACK)
    Player2_label = font.render("Player 2:", True, BLACK)

    Player1 = InputBox(300, 200, 100, 32, (100, 100, 100), (10,10,10))
    Player2 = InputBox(300, 250, 100, 32, (100, 100, 100), (10,10,10))
    
    Accept_Button = Button(300, 300, 100, 50, (0,0,0), (200,200,200), lambda:[main(player1 = Player1.export(), player2= Player2.export() ,mode=mode)])
    
    boxes_arr = [Player1, Player2]



    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            for box in boxes_arr:
                box.checkActivation(event)

            Accept_Button.processEvent(event)

            screen.fill(WHITE)
            screen.blit(Player1_label, (150, 200))
            screen.blit(Player2_label, (150, 250))
            screen.blit(title_label, (pygame.display.get_window_size()[0]/2 - title_label.get_rect().w/2, 30))
            for box in boxes_arr:
                box.draw(screen)
            
            Accept_Button.draw(screen)

            pygame.display.flip()

            

if __name__ == "__main__":
    login()    