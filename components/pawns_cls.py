import pygame
from components.pieces_cls import Pieces
from components.queens_cls import Queens

import json
import os

json_file = open(os.getcwd()+r"\components\constants.json", "r")
json_content = json.load(json_file)

round_int = json_content["round_int"]
tile_size = json_content["tile_size"]

json_file.close()

class BlackPawns(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image, value):
        super().__init__(master, name, tile_x, tile_y, farbe, image, value)
    
    def getPossible_Moves(self):

        finite_moves = []     
        # the normal pawn move
        possible_moves = [(self.x, self.y+tile_size)]

        
        # if the pawn stands on its first square, the it can move two squares forward
        deny = False
        if self.y == tile_size:
            for piece in Pieces.all_pieces_list:
                if (self.x, self.y+tile_size*2) == (piece.x, piece.y):
                    deny = True
                    break
        if not deny and self.y == tile_size:
            possible_moves.append((self.x, self.y+tile_size*2))

        # if any piece stands directly in front of the pawn, it can't move forward in any way
        for piece in Pieces.all_pieces_list:
            if self.x == piece.x and self.y+tile_size == piece.y:
                possible_moves.clear()
                break
        
        # if any enemy piece stands diagonaly in front of the pawn, it can move there and take it
        for piece in Pieces.all_pieces_list:
            if self.x+tile_size == piece.x and self.y+tile_size == piece.y and self.farbe != piece.farbe:
                possible_moves.append((self.x+tile_size, self.y+tile_size))
                
            if self.x-tile_size == piece.x and self.y+tile_size == piece.y and self.farbe != piece.farbe:
                possible_moves.append((self.x-tile_size, self.y+tile_size))

        possible_moves = self.foresight(possible_moves)

        return possible_moves #Pieces.check_limitation(possible_moves=possible_moves)

    def promotion(self):
        Pieces.all_pieces_list.remove(self)
        Queens(master = self.master, name = self.name + 'Promoted to Queen', tile_x = self.x/tile_size, tile_y = self.y/tile_size, farbe = 'schwarz', image = pygame.transform.scale(pygame.image.load(r'assets/black_queen.png'), (tile_size, tile_size)), value = 9)
        
        
        

    def attacked_tiles(self):
        return [(self.x+tile_size, self.y+tile_size), (self.x-tile_size, self.y+tile_size)]


class WhitePawns(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image, value):
        super().__init__(master, name, tile_x, tile_y, farbe, image, value)
    
    def getPossible_Moves(self):


        # the normal pawn move
        possible_moves = [(self.x, self.y-tile_size)]
        
        # if the pawn stands on its first square, the it can move two squares forward
        deny = False
        if self.y == 6*tile_size:
            for piece in Pieces.all_pieces_list:
                if (self.x, self.y-tile_size*2) == (piece.x, piece.y):
                    deny = True
                    break
        if not deny and self.y == 6* tile_size:
            possible_moves.append((self.x, self.y-tile_size*2))

        # if any piece stands directly in front of the pawn, it can't move forward in any way
        for piece in Pieces.all_pieces_list:
            if self.x == piece.x and self.y-tile_size == piece.y:
                possible_moves.clear()
                break

        # if any enemy piece stands diagonaly in front of the pawn, it can move there and take it
        for piece in Pieces.all_pieces_list:
            if self.x+tile_size == piece.x and self.y-tile_size == piece.y and self.farbe != piece.farbe:
                possible_moves.append((self.x+tile_size, self.y-tile_size))
                
            if self.x-tile_size == piece.x and self.y-tile_size == piece.y and self.farbe != piece.farbe:
                possible_moves.append((self.x-tile_size, self.y-tile_size))

        possible_moves = self.foresight(possible_moves)

        return possible_moves #Pieces.check_limitation(possible_moves= possible_moves)

    def attacked_tiles(self):
        return [(self.x+tile_size, self.y-tile_size), (self.x-tile_size, self.y-tile_size), (self.x, self.y)]

    def promotion(self):
        Pieces.all_pieces_list.remove(self)
        Queens(master = self.master, name = self.name + 'Promoted to Queen', tile_x = self.x/tile_size, tile_y = self.y/tile_size, farbe = 'weiss', image = pygame.transform.scale(pygame.image.load(r'assets/white_queen.png'), (tile_size, tile_size)), value = 9)
        
        
        


       