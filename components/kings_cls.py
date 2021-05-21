from components.board_cls import Board
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
        right_castle = True

        left_castle_p1 = True
        left_castle_p2 = True
        left_castle_p3 = True
        left_castle_p4 = True

        right_castle_p1 = True
        right_castle_p2 = True
        right_castle_p3 = True
        right_castle_p4 = True


        for rook in Pieces.all_pieces_list:
            #checking if left side castle is possible
            if "L-Rook" in rook.name and rook.farbe == self.farbe:

                #checking for property1: is a tile between the castles attacked
                left_square = (self.x-tile_size, self.y)
                for enemy in Pieces.all_pieces_list:
                    #"defining" enemy
                    if enemy.farbe != self.farbe:
                        att = enemy.attacked_tiles()
                        if left_square in att:
                            left_castle_p1 = False

                #checking for property2: is a piece between the castles
                tiles_in_between = [(self.x-tile_size*x, self.y) for x in range(1, 4)]
                for any_piece in Pieces.all_pieces_list:
                    any_piece_pos = (any_piece.x, any_piece.y)
                    if any_piece_pos in tiles_in_between:
                        left_castle_p2 = False
                
                #checking for property3 and property4: is any of the pieces touched

                left_castle_p3 = not self.touched
                left_castle_p4 = not rook.touched

                #asseble
                left_castle = left_castle_p1 and left_castle_p2 and left_castle_p3 and left_castle_p4
            

            #checking if right side castle is possible
            elif "R-Rook" in rook.name and rook.farbe == self.farbe:

                #checking for property1: is a tile between the castles attacked
                right_square = (self.x+tile_size, self.y)
                for enemy in Pieces.all_pieces_list:
                    #"defining" enemy
                    if enemy.farbe != self.farbe:
                        att = enemy.attacked_tiles()
                        if right_square in att:
                            right_castle_p1 = False

                #checking for property2: is a piece between the castles
                tiles_in_between = [(self.x+tile_size*x, self.y) for x in range(1, 3)]
                for any_piece in Pieces.all_pieces_list:
                    any_piece_pos = (any_piece.x, any_piece.y)
                    if any_piece_pos in tiles_in_between:
                        right_castle_p2 = False
                
                #checking for property3 and property4: is any of the pieces touched

                right_castle_p3 = not self.touched
                right_castle_p4 = not rook.touched

                #asseble
                right_castle = right_castle_p1 and right_castle_p2 and right_castle_p3 and right_castle_p4
        
        general = right_castle or left_castle

        return general, left_castle, right_castle