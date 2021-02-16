import pygame

class Board:

    game_draws = []

    def __init__(self, master, width, height, tile_size, color_a, color_b, anchor_point, border_color = (152, 186, 0)):
        self.master = master
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.color_a = color_a
        self.color_b = color_b
        self.borderColor = border_color
        self.anchor_point = anchor_point

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
        
        x = tile[0]
        y = tile[1]

        pygame.draw.rect(self.master, newColor, [x, y, self.tile_size, self.tile_size])

    def drawBorder(self, tile, screen):
        
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
        screen.blit(self.master, self.anchor_point)

    def check(self, king_pos):
        self.changeTilecolor(tile = king_pos, newColor = (247, 87, 87))

    @staticmethod
    def getcurrentTile(x_, y_, tile_size):
        posx = 0
        posy = 0

        for x in range(8):
            if x_ >= x*tile_size and x_ < x*tile_size+tile_size:
                posx = chr(x+97)
        
        for y in range(8):
            if y_ >= y*tile_size and y_ < y*tile_size+tile_size:
                posy = 9-y-1
        
        return str(posx)+str(posy)

    @staticmethod
    def translate_to_coordinates(tile, tile_size):
        return (int(ord(tile[0])-97)*tile_size, (8-int(tile[1]))*tile_size)
    
    def end_screen(self, winner, screen):
        
        f = pygame.font.SysFont('Arial', self.tile_size)
        s = pygame.Surface((8*self.tile_size,8*self.tile_size))  # the size of your rect
        s.set_alpha(128)                # alpha level
        s.fill((255,255,255))           # this fills the entire surface
        if winner == 'STALEMATE':
            label = f.render('STALEMATE', True, (0,0,0))
        else:
            label = f.render(winner+' WON', True, (0,0,0))
        screen.blit(label, (s.get_width()/2 - label.get_width()/2,s.get_height()/2-label.get_height()/2))
        screen.blit(s, (0,0))    # (0,0) are the top-left coordinates


        
print(Board.translate_to_coordinates('e2', 70))
# b = Board(None, None, None, 120, None, None, None, None)

# print(Board.getcurrentTile(356, 270))