import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
# COLOR_INACTIVE = pygame.Color('lightskyblue3')
# COLOR_ACTIVE = pygame.Color('dodgerblue2')
# FONT = pygame.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, width, height, color_inactive, color_active, text=''):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color_act = color_active
        self.color_inact = color_inactive
        self.color_now = color_inactive
        self.text = text
        self.font = pygame.font.Font(None, self.height)
        self.txt_surface = self.font.render(text, True, self.color_now)
        self.active = False

    def checkActivation(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos):
                self.active = not self.active
            else:
                self.active = False

            self.color_now = self.color_act if self.active else self.color_inact

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # self.export()
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                
                self.txt_surface = self.font.render(self.text, True, self.color_inact)
                self.updateLength()

    def updateLength(self):
        width = max(self.width, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color_now, self.rect, 2)

    def export(self):
        return self.text


def main():
    clock = pygame.time.Clock()
    input_box1 = InputBox(100, 100, 140, 40, pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'))
    input_box2 = InputBox(100, 300, 140, 32, pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'))
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.checkActivation(event)


        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()