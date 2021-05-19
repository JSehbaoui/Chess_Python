import pygame
from components.button import Button

pygame.init()

class Testmode_Button(Button):
    def __init__(self, x, y, w, h, color_b, color_in, color_t, command1, command2, text = 'Button', imaginary_x = 0, imaginary_y = 0, icon = None, deaf = False):
        super().__init__(x, y, w, h, color_b, color_in, color_t, command = None, text=text, imaginary_x=imaginary_x, imaginary_y=imaginary_y, icon=icon, deaf=deaf)
        self.state = True
        self.c1 = command1
        self.c2 = command2

    def processEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.active:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = mouse_pos[0]-self.x_, mouse_pos[1]-self.y_

            if self.button_rect.collidepoint(mouse_pos):
                if not self.state:
                    self.c1()
                else:
                    self.c2()

                self.state = not self.state
    