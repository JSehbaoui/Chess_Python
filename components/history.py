import pygame

class Hud(pygame.Surface):

    def __init__(self, size):
        super().__init__(size)

    def print(self, pos, label, font):
        self.blit(font.render(label, 1, (0,0,0)), pos)