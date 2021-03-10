import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

class TickBox:
    def __init__(self, posx, posy, size):
        self.x = posx
        self.y = posy
        self.size = size
        self.rect_border = pygame.Rect(self.x, self.y, self.size, self.size)
        self.rect_inner = pygame.Rect(self.x+5, self.y+5, self.size-10, self.size-10)
        self.ticked = False
        self.color_unticked = (200, 200, 200)
        self.color_ticked = (20, 200, 20)
        self.color_now = self.color_unticked
        self.color_border = (255,255,255)

    def processEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousepos = pygame.mouse.get_pos()
            if self.rect_border.collidepoint(mousepos):
                self.ticked = not self.ticked
                if self.ticked:
                    self.color_now = self.color_ticked
                else:
                    self.color_now = self.color_unticked
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color_border, self.rect_border)
        pygame.draw.rect(screen, self.color_now, self.rect_inner)
    
    def getStatus(self):
        return self.ticked

def main():
    clock = pygame.time.Clock()
    box = TickBox(posx = 50, posy = 50, size = 50)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            box.processEvent(event)


        screen.fill((30, 30, 30))
        box.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
