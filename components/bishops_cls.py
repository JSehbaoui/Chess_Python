import pygame
import os
import json
from components.pieces_cls import Pieces
from components.kings_cls import Kings

json_file = open(os.getcwd()+r"\components\constants.json", "r")
json_content = json.load(json_file)

round_int = json_content["round_int"]
tile_size = json_content["tile_size"]

json_file.close()


class Bishops(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image, value):
        super().__init__(master, name, tile_x, tile_y, farbe, image, value)
    
    def getPossible_Moves(self):
        possible_moves = []
        
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size*-1,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size*-1,  attacking = False)

        iterator = filter(self.filter_method, possible_moves)

        possible_moves = list(iterator)

        possible_moves = self.foresight(possible_moves)


        return possible_moves#Pieces.check_limitation(possible_moves=possible_moves)

    def attacked_tiles(self):
        possible_moves = []
        
        self.check_row_tiles_wo_king(current_moves = possible_moves, step_x = tile_size, step_y = tile_size,  attacking = True)
        self.check_row_tiles_wo_king(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size,  attacking = True)
        self.check_row_tiles_wo_king(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size*-1,  attacking = True)
        self.check_row_tiles_wo_king(current_moves = possible_moves, step_x = tile_size, step_y = tile_size*-1,  attacking = True)

        # Have to that, so the other recognize that tile as an option to deny check
        possible_moves.append((self.x, self.y))

        return possible_moves
    
    # returns 1-4, rather which line is the attecked one
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


                        if newstep1 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size, step_y = tile_size, attacking = False)
                            return list_
                            break
                        
                        elif newstep2 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size, step_y = tile_size*-1, attacking = False)
                            return list_
                            break 
                        
                        elif newstep3 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size*-1, step_y = tile_size, attacking = False)
                            return list_
                            break

                        elif newstep4 == (blackKing.x, blackKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size*-1, step_y = tile_size*-1, attacking = False)
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

                        if newstep1 == (whiteKing.x, whiteKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size, step_y = tile_size, attacking = False)
                            return list_
                            break
                        
                        elif newstep2 == (whiteKing.x, whiteKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size, step_y = tile_size*-1, attacking = False)
                            return list_
                            break
                        
                        elif newstep3 == (whiteKing.x, whiteKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size*-1, step_y = tile_size, attacking = False)
                            return list_
                            break
                        
                        elif newstep4 == (whiteKing.x, whiteKing.y):
                            self.check_row_tiles(current_moves=list_, step_x = tile_size*-1, step_y = tile_size*-1, attacking = False)
                            return list_
                            break
