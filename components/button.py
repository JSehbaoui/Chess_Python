import pygame
pygame.init()

class Button:
    
    def __init__(self, master, x, y, w, h, color_b, color_t, command, text = 'Button'):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.master = master
        self.button_rect = pygame.Rect(x, y, w, h)
        self.color_b = color_b
        self.color_t = color_t
        self.text = text
        self.font = pygame.font.Font(None, self.h//3)
        self.command = command

    def draw(self):
        pygame.draw.rect(self.master, self.color_b, self.button_rect)
        label = self.font.render(self.text, True, self.color_t)
        label_rect = label.get_rect()
        self.master.blit(label, (self.x + self.w/2 - label_rect.w/2, self.y + self.h/2 - label_rect.h/2))

    def checkClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.button_rect.collidepoint(mouse_pos):
                self.command()
            
def printHello():
    print("hello")

def main():
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    Button1 = Button(screen, 100, 100, 300, 200, (0,0,0), (100, 100, 100), printHello)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        Button1.checkClick(event)
        

        screen.fill((255, 255, 255))

        Button1.draw()


        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()