from pygame.constants import APPACTIVE
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
        
        # castle

        propertys = self.is_castle_legal()

        if propertys[0]:
            if propertys[1]:
                possible_moves_filtered.append((self.x-2*tile_size, self.y))
            if propertys[2]:
                possible_moves_filtered.append((self.x+2*tile_size, self.y))


        iterator = filter(self.filter_method, possible_moves_filtered)

        possible_moves_filtered = list(iterator)

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

    def is_castle_legal(self):
        left_castle = True
        right_caste = True
        if not self.touched:
            for rook in Pieces.all_pieces_list:
                if 'Rook' in rook.name and rook.farbe == self.farbe and not rook.touched:
                    for enemy in Pieces.all_pieces_list:
                        if not enemy.farbe == self.farbe:
                            l = enemy.attacked_tiles()
                    
                            if 'L' in rook.name:
                                weak_side = (self.x-tile_size, self.y)
                            elif 'R' in rook.name:
                                weak_side = (self.x-tile_size, self.y)
                            
                            if weak_side in l:
                                return False, False, False
    
                    for piece in Pieces.all_pieces_list:
                        if 'L' in rook.name:
                            for i in range(1, 4):
                                if (piece.x, piece.y) == (self.x-i*tile_size, self.y):
                                    left_castle = False
                        elif 'R' in rook.name:
                            for i in range(1, 3):
                                b = (piece.x, piece.y) == (self.x+i*tile_size, self.y)
                                if b:
                                    right_caste = False
                    
            if left_castle or right_caste:
                return True, left_castle, right_caste
            else:
                return False, False, False
        else:
            return False, False, False