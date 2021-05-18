import pygame
pygame.init()

class Button:
    
    def __init__(self, x, y, w, h, color_b, color_in, color_t, command, text = 'Button', imaginary_x = 0, imaginary_y = 0, icon = None, deaf = True):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.button_rect = pygame.Rect(x, y, w, h)
        self.color_b = color_b
        self.color_in = color_in
        self.color_t = color_t
        self.text = text
        self.font = pygame.font.Font(None, self.h//3)
        self.command = command
        self.x_ = imaginary_x
        self.y_ = imaginary_y
        self.icon = icon
        self.active = True
        self.deaf = deaf


    def draw(self, screen):
        if self.active:
            color = self.color_b
        else:
            color = self.color_in

        pygame.draw.rect(screen, color , self.button_rect)
        if self.icon != None:
            icon = pygame.transform.scale(self.icon, (self.w-10, self.h-10))
            screen.blit(icon, (self.x+5,self.y+5))
        else:
            label = self.font.render(self.text, True, self.color_t)
            label_rect = label.get_rect()
            screen.blit(label, (self.x + self.w/2 - label_rect.w/2, self.y + self.h/2 - label_rect.h/2))

    def processEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.active:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = mouse_pos[0]-self.x_, mouse_pos[1]-self.y_

            if self.button_rect.collidepoint(mouse_pos):
                if self.deaf:
                    self.active = False
                self.command()
            
def printHello():
    print("hello")

def main():
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    Button1 = Button(100, 100, 300, 200, (0,0,0), (100, 100, 100), printHello)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            Button1.processEvent(event)
        

        screen.fill((255, 255, 255))

        Button1.draw(screen)


        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()