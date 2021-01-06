import pygame
from components.pieces_cls import Pieces
from components.kings_cls import Kings

import json
import os

json_file = open(os.getcwd()+r"\components\constants.json", "r")
json_content = json.load(json_file)

round_int = json_content["round_int"]
tile_size = json_content["tile_size"]

json_file.close()

class Queens(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)
    
    def getPossible_Moves(self):
        possible_moves = []
        finite_moves = []

        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size*-1,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size*-1,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = 0,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= tile_size*-1, step_y = 0,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size*-1,  attacking = False)
 
        if Pieces.white_is_checked or Pieces.black_is_checked:
            enemy_moves = Pieces.checking_piece.attacking_line()
            for possible_move in possible_moves:
                for enemy_move in enemy_moves:
                    if enemy_move == possible_move:
                        finite_moves.append(possible_move)

        else:
            finite_moves = possible_moves

        return finite_moves

    def attacted_tiles(self):
        possible_moves = []
        
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size,  attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size,  attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size*-1,  attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size*-1,  attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = 0,  attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x= tile_size*-1, step_y = 0,  attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size,  attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size*-1,  attacking = True)

        possible_moves.append((self.x, self.y))

        return possible_moves
    
    def attacking_line(self):
        
        if self.farbe == (0,0,0):
            list_ = []
            for blackKing in Pieces.all_pieces_list:
                bool1 = bool(isinstance(blackKing, Kings))
                bool2 = bool(blackKing.farbe == (255,255,255))
                if bool1 and bool2:

                    for i in range(8):
                        newstep1 = (self.x+tile_size*i, self.y+tile_size*i)
                        newstep2 = (self.x+tile_size*i, self.y-tile_size*i)
                        newstep3 = (self.x-tile_size*i, self.y+tile_size*i)
                        newstep4 = (self.x-tile_size*i, self.y-tile_size*i)
                        newstep5 = (self.x+tile_size*i, self.y)
                        newstep6 = (self.x-tile_size*i, self.y)
                        newstep7 = (self.x, self.y+tile_size*i)
                        newstep8 = (self.x, self.y-tile_size*i)


                        if newstep1 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size, step_y = tile_size, attacking = False)
                            return list_
                            break
                        
                        if newstep2 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size, step_y = tile_size*-1, attacking = False)
                            return list_
                            break 
                        
                        if newstep3 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size*-1, step_y = tile_size, attacking = False)
                            return list_
                            break

                        if newstep4 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size*-1, step_y = tile_size*-1, attacking = False)
                            return list_
                            break

                        if newstep5 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size, step_y = 0, attacking = False)
                            return list_
                            break
                        
                        if newstep6 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size*-1, step_y = 0, attacking = False)
                            return list_
                            break 
                        
                        if newstep7 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = 0, step_y = tile_size, attacking = False)
                            return list_
                            break

                        if newstep8 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = 0, step_y = tile_size*-1, attacking = False)
                            return list_
                            break
                        

        if self.farbe == (255,255,255):
            list_ = []
            for whiteKing in Pieces.all_pieces_list:
                if isinstance(whiteKing, Kings) and whiteKing.farbe == (0,0,0):

                    for i in range(8):
                        newstep1 = (self.x+tile_size*i, self.y+tile_size*i)
                        newstep2 = (self.x+tile_size*i, self.y-tile_size*i)
                        newstep3 = (self.x-tile_size*i, self.y+tile_size*i)
                        newstep4 = (self.x-tile_size*i, self.y-tile_size*i)
                        newstep5 = (self.x+tile_size*i, self.y)
                        newstep6 = (self.x-tile_size*i, self.y)
                        newstep7 = (self.x, self.y+tile_size*i)
                        newstep8 = (self.x, self.y-tile_size*i)

                        if newstep1 == (whiteKing.x, whiteKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size, step_y = tile_size, attacking = False)
                            return list_
                            break
                        
                        if newstep2 == (whiteKing.x, whiteKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size, step_y = tile_size*-1, attacking = False)
                            return list_
                            break
                        
                        if newstep3 == (whiteKing.x, whiteKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size*-1, step_y = tile_size, attacking = False)
                            return list_
                            break
                        
                        if newstep4 == (whiteKing.x, whiteKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size*-1, step_y = tile_size*-1, attacking = False)
                            return list_
                            break

                        if newstep5 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size, step_y = 0, attacking = False)
                            return list_
                            break
                        
                        if newstep6 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size*-1, step_y = 0, attacking = False)
                            return list_
                            break 
                        
                        if newstep7 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = 0, step_y = tile_size, attacking = False)
                            return list_
                            break

                        if newstep8 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = 0, step_y = tile_size*-1, attacking = False)
                            return list_
                            break
