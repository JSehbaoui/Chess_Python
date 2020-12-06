import pygame

round_int = 0
tile_size = 120

class Pieces:
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        self.x = tile_x*tile_size
        self.y = tile_y*tile_size
        self.possible_moves = []
        self.master = master
        self.name = name
        self.image = pygame.transform.scale(image, (tile_size-20, tile_size-20))
        if farbe == 'schwarz':
            self.farbe = (0,0,0)
        elif farbe == 'weiss':
            self.farbe = (255,255,255)
        Pieces.draw(self)

    @staticmethod
    def round_increment():
        global round_int
        round_int += 1

    def draw(self):
        #pygame.draw.rect(self.master, self.farbe, [self.x+10, self.y+10, 30, 30])
        self.master.blit(self.image, (self.x+10, self.y+10))

    
    def move(self, occupied_tiles, all_pieces_list):
    
        go = True
        ok = True
        while go:

            for tile in self.getPossible_Moves(all_pieces_list = all_pieces_list):
                pygame.draw.rect(self.master, (152, 186, 0), [tile[0], tile[1], tile_size, tile_size])

                fac1 = tile[0]/tile_size
                fac2 = tile[1]/tile_size  
                prod = fac1+fac2
                if prod % 2 == 0:
                    color = (245, 216, 188)
                else:
                    color = (176, 142, 109)

                pygame.draw.rect(self.master, color , [tile[0]+10, tile[1]+10, tile_size-20, tile_size-20])
            
            for pieces in all_pieces_list:
                pieces.draw()

            pygame.display.update()



            #checking for events
            for event in pygame.event.get():



                #Mouse-Inputs
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()

                    #if the clicked tile is a sqaure, where the pawn can go, move it
                    global round_int
                    
                    # create bool var
                    for possible_move in self.getPossible_Moves(all_pieces_list=all_pieces_list):
                        if mouse_pos[0] >= possible_move[0] and mouse_pos[1] >=possible_move[1]:
                            if mouse_pos[0] < possible_move[0]+tile_size and mouse_pos[1] < possible_move[1]+tile_size:
                                for piece in all_pieces_list:
                                    if mouse_pos[0] >= piece.x and mouse_pos[1] >= piece.y:
                                        if mouse_pos[0] < piece.x+tile_size and mouse_pos[1] < piece.y+tile_size:
                                            if self.farbe != piece.farbe:
                                                go = False
                                                ok = False
                                                print('TAKES')

                                                Pieces.round_increment()

                                                self.x = possible_move[0]
                                                self.y = possible_move[1]
                                                
                                                Pieces.draw(self)
                                                all_pieces_list.remove(piece)

                                                if 'Pawn-B' in self.name and self.y == 490 or 'Pawn-W' in self.name and self.y == 0:
                                                    self.promotion(all_pieces_list = all_pieces_list)



                                                return all_pieces_list
                                            else:
                                                ok = False 


                                                    
                                        else:
                                            pass
                                    else:
                                        pass
                                    
                                if ok: 
                                
                                    self.x = possible_move[0]
                                    self.y = possible_move[1]
                                    Pieces.draw(self)
                                    print('Moved')
                                    Pieces.round_increment()
                                    go = False

                                    if 'Pawn_B' in self.name and self.x == 350 or 'Pawn_W' in self.name and self.x == 0:
                                        self.promotion(all_pieces_list = all_pieces_list)
                            
                            else:
                                go = False
                        else:
                            go = False        
                    go = False
            
                
            



    def check_row_tiles(self, current_moves, step_x, step_y, all_pieces_list, attacking):
        free_bool = False
        go = True
        num = 0
        while go and num < 10:
            num += 1
            testing_move = (self.x+step_x*num, self.y+step_y*num)

            for piece in all_pieces_list:
                if testing_move[0] == piece.x and testing_move[1] == piece.y:
                    go = False
                    if attacking:
                        free_bool = True
                    else:
                        if self.farbe == piece.farbe:
                            free_bool = False
                        else:
                            free_bool = True
                        break
                else:
                    free_bool = True

            if free_bool:
                current_moves.append(testing_move)
                free_bool = False
        


        return current_moves

    def attacted_tiles(self, all_pieces_list):
        attacted_tiles = self.getPossible_Moves(all_pieces_list=all_pieces_list)

        return attacted_tiles



class BlackPawns(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)
    
    def getPossible_Moves(self, all_pieces_list):
             
        # the normal pawn move
        possible_moves = [(self.x, self.y+tile_size)]
        
        # if the pawn stands on its first square, the it can move two squares forward
        for piece in all_pieces_list:
            if self.y == tile_size and not (piece.x == self.x and piece.y == tile_size*3):
                possible_moves.append((self.x, self.y+tile_size*2))

        # if any piece stands directly in front of the pawn, it can't move forward in any way
        for piece in all_pieces_list:
            if self.x == piece.x and self.y+tile_size == piece.y:
                possible_moves.clear()
                break
        
        # if any enemy piece stands diagonaly in front of the pawn, it can move there and take it
        for piece in all_pieces_list:
            if self.x+tile_size == piece.x and self.y+tile_size == piece.y and self.farbe != piece.farbe:
                possible_moves.append((self.x+tile_size, self.y+tile_size))
                break
            if self.x-tile_size == piece.x and self.y+tile_size == piece.y and self.farbe != piece.farbe:
                possible_moves.append((self.x-tile_size, self.y+tile_size))
                break

        return possible_moves
        

    def promotion(self, all_pieces_list):
        
        queen = Queens(master = self.master, name = self.name + 'Promoted to Queen', tile_x = self.x/tile_size, tile_y = self.y/tile_size, farbe = 'schwarz', image = pygame.transform.scale(pygame.image.load(r'assets/black_queen.png'), (tile_size, tile_size)))
        all_pieces_list.append(queen)
        queen.draw()
        all_pieces_list.remove(self)

        return all_pieces_list



    def attacted_tiles(self, all_pieces_list):
        return [(self.x+tile_size, self.y+tile_size), (self.x-tile_size, self.y+tile_size)]

class WhitePawns(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)
    
    def getPossible_Moves(self, all_pieces_list):
        # the normal pawn move
        possible_moves = [(self.x, self.y-tile_size)]
        
        # if the pawn stands on its first square, the it can move two squares forward
        if self.y == 6*tile_size:
            possible_moves.append((self.x, self.y-tile_size*2))

        # if any piece stands directly in front of the pawn, it can't move forward in any way
        for piece in all_pieces_list:
            if self.x == piece.x and self.y-tile_size == piece.y:
                possible_moves.clear()
                break

        # if any enemy piece stands diagonaly in front of the pawn, it can move there and take it
        for piece in all_pieces_list:
            if self.x+tile_size == piece.x and self.y-tile_size == piece.y and self.farbe != piece.farbe:
                possible_moves.append((self.x+tile_size, self.y-tile_size))
                break
            if self.x-tile_size == piece.x and self.y-tile_size == piece.y and self.farbe != piece.farbe:
                possible_moves.append((self.x-tile_size, self.y-tile_size))
                break

        return possible_moves

    def attacted_tiles(self, all_pieces_list):
        return [(self.x+tile_size, self.y-tile_size), (self.x-tile_size, self.y-tile_size)]

    def promotion(self, all_pieces_list):

        all_pieces_list.append(Queens(master = self.master, name = self.name + 'Promoted to Queen', tile_x = self.x, tile_y = self.y, farbe = 'weiss', image = pygame.transform.scale(pygame.image.load(r'assets/white_queen.png'), (tile_size, tile_size))))
        all_pieces_list.remove(self)

        return all_pieces_list


class Rooks(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)

    def getPossible_Moves(self, all_pieces_list):
        possible_moves = []

        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = 0, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= tile_size*-1, step_y = 0, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = False)

        return possible_moves
    
    def attacted_tiles(self, all_pieces_list):
        possible_moves = []

        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = 0, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x= tile_size*-1, step_y = 0, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = True)

        return possible_moves
                    
class Bishops(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)
    
    def getPossible_Moves(self, all_pieces_list):
        possible_moves = []
        
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = False)

        return possible_moves

    def attacted_tiles(self, all_pieces_list):
        possible_moves = []
        
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = True)

        return possible_moves

class Knights(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)
    
    def getPossible_Moves(self, all_pieces_list):
        possible_moves = [(self.x-2*tile_size, self.y+tile_size),
                            (self.x-2*tile_size, self.y-tile_size),
                            (self.x-tile_size, self.y+2*tile_size),
                            (self.x-tile_size, self.y-2*tile_size),
                            (self.x+tile_size, self.y+2*tile_size),
                            (self.x+tile_size, self.y-2*tile_size),
                            (self.x+2*tile_size, self.y+tile_size),
                            (self.x+2*tile_size, self.y-tile_size)
                            ]

        index_list = []

        lenght_array = len(possible_moves)

        for i in range(lenght_array):
            for piece in all_pieces_list:
                bool1 = bool(possible_moves[i][0] == piece.x)
                bool2 = bool(possible_moves[i][1] == piece.y)
                bool3 = bool(self.farbe == piece.farbe)

                if bool1 and bool2 and bool3:
                    index_list.append(i)
                    break

        for del_index in index_list:
            possible_moves.pop(del_index)
            #nasty shit
            for i in range(len(index_list)):
                index_list[i] -= 1


        return possible_moves

class Queens(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)
    
    def getPossible_Moves(self, all_pieces_list):
        possible_moves = []

        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = 0, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= tile_size*-1, step_y = 0, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = False)
 
        return possible_moves

    def attacted_tiles(self, all_pieces_list):
        possible_moves = []
        
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = 0, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x= tile_size*-1, step_y = 0, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = True)

        return possible_moves

class Kings(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)
    
    def getPossible_Moves(self, all_pieces_list):
        possible_moves_unfiltered = [(self.x-tile_size, self.y+tile_size),
                                    (self.x-tile_size, self.y),
                                    (self.x-tile_size, self.y-tile_size),
                                    (self.x, self.y+tile_size),
                                    (self.x, self.y-tile_size),
                                    (self.x+tile_size, self.y+tile_size),
                                    (self.x+tile_size, self.y),
                                    (self.x+tile_size, self.y-tile_size)
                                    ]

        possible_moves_filtered = []

        # print('Raw: ', possible_moves)
        index_list = []
        possible = True

        for move in possible_moves_unfiltered:
            for piece in all_pieces_list:
                bool1 = bool(move[0] == piece.x)
                bool2 = bool(move[1] == piece.y)
                bool3 = bool(self.farbe == piece.farbe)

                if bool1 and bool2 and bool3:
                    possible = False
                    break

                else:
                    possible = True
                
            if possible:
                possible_moves_filtered.append(move)

        possible_moves_unfiltered = possible_moves_filtered

        possible_moves_filtered = []
        
        for move in possible_moves_unfiltered:
            for piece in all_pieces_list:
                if piece.farbe != self.farbe and not 'King' in piece.name:
                    piece_attacted_tiles_arr = piece.attacted_tiles(all_pieces_list = all_pieces_list)
                    bool4 = bool(move in piece_attacted_tiles_arr)
                    if bool4:
                        possible = False
                        break
                    else:
                        possible = True
            if possible:
                possible_moves_filtered.append(move)

        return possible_moves_filtered
