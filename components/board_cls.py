import pygame

class Board:
    def __init__(self, master, width, height, tile_size, color_a, color_b, border_color = (152, 186, 0)):
        self.master = master
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.color_a = color_a
        self.color_b = color_b
        self.borderColor = border_color

    def convert_Tile_to_X_and_Y(self, tile):
        x = 0

        for i in range(self.width):
            if tile[0] == chr(i+97):
                x = i

        y = int(tile[1]) - 1

        return x, y

    def draw_board(self):
        tile_dir_list = []

        for y in range(8):
            tile_dir_list.append([])
            for x in range(8):
                tile_dir_list[y].append((x*self.tile_size, y*self.tile_size))
                if y % 2 == 0:
                    if x % 2 == 0:
                        pygame.draw.rect(self.master, (245, 216, 188), [x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size])
                    else:
                        pygame.draw.rect(self.master, (176, 142, 109), [x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size])
                else:
                    if x % 2 == 0:
                        pygame.draw.rect(self.master, (176, 142, 109), [x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size])
                    else:
                        pygame.draw.rect(self.master, (245, 216, 188), [x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size])

    def changeTilecolor(self, tile, newColor):
        
        x = self.convert_Tile_to_X_and_Y(tile)[0]
        y = self.convert_Tile_to_X_and_Y(tile)[1]

        pygame.draw.rect(self.master, newColor, [self.tile_size*x, self.tile_size*y, self.tile_size*x+self.tile_size, self.tile_size*y+self.tile_size])

    def drawBorder(self, tile):
        
        x = tile[0]
        y = tile[1]

        pygame.draw.rect(self.master, self.borderColor, [x, y, self.tile_size, self.tile_size])

        fac1 = x/self.tile_size
        fac2 = y/self.tile_size  
        prod = fac1+fac2
        if prod % 2 == 0:
            color = self.color_a
        else:
            color = self.color_b

        pygame.draw.rect(self.master, color , [x+10, y+10, self.tile_size-20, self.tile_size-20])
