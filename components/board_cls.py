import pygame

class Board:

    game_draws = []
    game_over = False
    resign = False
    test_mode = False

    def __init__(self, master, width, height, tile_size, color_a, color_b, color_t1, color_t2, anchor_point, border_color = (152, 186, 0)):
        self.master = master
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.color_a = color_a
        self.color_b = color_b
        self.color_t1 = color_t1
        self.color_t2 = color_t2
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
        font = pygame.font.Font(None, 20)

        if Board.test_mode:
            color = (self.color_t1, self.color_t2)
        else:
            color = (self.color_a, self.color_b)

        for y in range(8):
            tile_dir_list.append([])
            for x in range(8):
                tile_dir_list[y].append((x*self.tile_size, y*self.tile_size))
                if y % 2 == 0:
                    if x % 2 == 0:
                        pygame.draw.rect(self.master, color[0], [x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size])
                    else:
                        pygame.draw.rect(self.master, color[1], [x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size])
                else:
                    if x % 2 == 0:
                        pygame.draw.rect(self.master, color[1], [x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size])
                    else:
                        pygame.draw.rect(self.master, color[0], [x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size])

        for x in range(8):
            if x%2 == 0:
                color_l = color[0]
            else:
                color_l = color[1]
            
            label = font.render(chr(97+x), True, color_l)
            self.master.blit(label, (x*self.tile_size+5, 8*self.tile_size-15))

        for y in range(8):
            if y%2 == 0:
                color_l = color[0]
            else:
                color_l = color[1]
            
            label = font.render(str(8-y), True, color_l)
            self.master.blit(label, (8*self.tile_size-15, y*self.tile_size+5))


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

        if Board.test_mode:
            color_set = [self.color_t1, self.color_t2]
        else:
            color_set = [self.color_a, self.color_b]

        if prod % 2 == 0:
            color = color_set[0]
        else:
            color = color_set[1]

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
    
    def end_screen(self, winner, screen_):
        
        f = pygame.font.SysFont('Arial', self.tile_size)
        s = pygame.Surface((8*self.tile_size,8*self.tile_size))  # the size of your rect
        s.set_alpha(128)                # alpha level
        s.fill((255,255,255))           # this fills the entire surface
        if winner == 'STALEMATE':
            label = f.render('STALEMATE', True, (0,0,0))
        else:
            label = f.render(winner+' WON', True, (0,0,0))
        screen_.blit(label, (s.get_width()/2 - label.get_width()/2,s.get_height()/2-label.get_height()/2))
        screen_.blit(s, (0,0))    # (0,0) are the top-left coordinates
        Board.game_over = True

    @classmethod
    def change_testmode(cls):
        cls.test_mode = not cls.test_mode