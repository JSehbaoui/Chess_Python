import pygame
from components.pieces_cls import Pieces

import json
import os

json_file = open(os.getcwd()+r"\components\constants.json", "r")
json_content = json.load(json_file)

round_int = json_content["round_int"]
tile_size = json_content["tile_size"]

json_file.close()

class Rooks(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)

    def getPossible_Moves(self):
        possible_moves = []
        finite_moves = []

        # getting the regular moves for the x+, x-, y+, y- Axis
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = 0,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= tile_size*-1, step_y = 0,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size,  attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size*-1,  attacking = False)

        # if white or black is checked look if you can move at an attacked square, from the attacking piece
        if Pieces.white_is_checked or Pieces.black_is_checked:
            enemy_moves = Pieces.checking_piece.attacted_tiles()
            for possible_move in possible_moves:
                for enemy_move in enemy_moves:
                    if enemy_move == possible_move:
                        finite_moves.append(possible_move)

        # else just pass the regular moves
        else:
            finite_moves = possible_moves


        return finite_moves
    
    def attacted_tiles(self):
        possible_moves = []

        self.check_row_tiles_wo_king(current_moves = possible_moves, step_x = tile_size, step_y = 0,  attacking = True)
        self.check_row_tiles_wo_king(current_moves = possible_moves, step_x= tile_size*-1, step_y = 0,  attacking = True)
        self.check_row_tiles_wo_king(current_moves = possible_moves, step_x= 0, step_y = tile_size,  attacking = True)
        self.check_row_tiles_wo_king(current_moves = possible_moves, step_x= 0, step_y = tile_size*-1,  attacking = True)

        possible_moves.append((self.x, self.y))

        return possible_moves
                    