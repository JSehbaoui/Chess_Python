import pygame
from .pieces_cls import Pieces

import json
import os

json_file = open(os.getcwd()+r"\components\constants.json", "r")
json_content = json.load(json_file)

round_int = json_content["round_int"]
tile_size = json_content["tile_size"]

json_file.close()

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
