from .pieces_cls import Pieces

import json
import os

json_file = open(os.getcwd()+r"\components\constants.json", "r")
json_content = json.load(json_file)

round_int = json_content["round_int"]
tile_size = json_content["tile_size"]

json_file.close()

class Kings(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image, value):
        super().__init__(master, name, tile_x, tile_y, farbe, image, value)
    
    def getPossible_Moves(self):
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

        # Filters the tiles, where allied pieces stand on
        for move in possible_moves_unfiltered:
            for piece in Pieces.all_pieces_list:
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

        # reset the lists for the next filter
        possible_moves_unfiltered = list(possible_moves_filtered)
        possible_moves_filtered = []
        
        # filters the tiles, that are currently attacked by the enemy
        for move in possible_moves_unfiltered:
            for piece in Pieces.all_pieces_list:
                if piece.farbe != self.farbe:
                    piece_attacted_tiles_arr = piece.attacked_tiles()
                    if move in piece_attacted_tiles_arr and not move == (piece.x, piece.y):
                        possible = False
                        break
                    else:
                        possible = True
            if possible:
                possible_moves_filtered.append(move)

        possible_moves_filtered = self.foresight(possible_moves_filtered)

        return possible_moves_filtered

    def attacked_tiles(self):
        possible_moves_unfiltered = [(self.x-tile_size, self.y+tile_size),
                                    (self.x-tile_size, self.y),
                                    (self.x-tile_size, self.y-tile_size),
                                    (self.x, self.y+tile_size),
                                    (self.x, self.y-tile_size),
                                    (self.x+tile_size, self.y+tile_size),
                                    (self.x+tile_size, self.y),
                                    (self.x+tile_size, self.y-tile_size)
                                    ]
        return possible_moves_unfiltered
