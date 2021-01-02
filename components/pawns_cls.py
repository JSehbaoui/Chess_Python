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
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)
    
    def getPossible_Moves(self):

        finite_moves = []     
        # the normal pawn move
        possible_moves = [(self.x, self.y+tile_size)]

        
        # if the pawn stands on its first square, the it can move two squares forward
        for piece in Pieces.all_pieces_list:
            if self.y == tile_size and not (piece.x == self.x and piece.y == tile_size*3):
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
        
        if Pieces.white_is_checked or Pieces.black_is_checked:
            enemy_moves = Pieces.checking_piece.attacted_tiles()
            for possible_move in possible_moves:
                for enemy_move in enemy_moves:
                    if enemy_move == possible_move:
                        finite_moves.append(possible_move)
        
        else:
            finite_moves = possible_moves 


        return finite_moves
        

    def promotion(self):
        
        queen = Queens(master = self.master, name = self.name + 'Promoted to Queen', tile_x = self.x/tile_size, tile_y = self.y/tile_size, farbe = 'schwarz', image = pygame.transform.scale(pygame.image.load(r'assets/black_queen.png'), (tile_size, tile_size)))
        Pieces.all_pieces_list.append(queen)
        queen.draw()
        Pieces.all_pieces_list.remove(self)





    def attacted_tiles(self):
        return [(self.x+tile_size, self.y+tile_size), (self.x-tile_size, self.y+tile_size)]

class WhitePawns(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)
    
    def getPossible_Moves(self):

        finite_moves = []
        # the normal pawn move
        possible_moves = [(self.x, self.y-tile_size)]
        
        # if the pawn stands on its first square, the it can move two squares forward
        if self.y == 6*tile_size:
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
                break
            if self.x-tile_size == piece.x and self.y-tile_size == piece.y and self.farbe != piece.farbe:
                possible_moves.append((self.x-tile_size, self.y-tile_size))
                break

        if Pieces.white_is_checked or Pieces.black_is_checked:
            enemy_moves = Pieces.checking_piece.attacted_tiles()
            for possible_move in possible_moves:
                for enemy_move in enemy_moves:
                    if enemy_move == possible_move:
                        finite_moves.append(possible_move)
        
        else:
            finite_moves = possible_moves 

        return finite_moves

    def attacted_tiles(self):
        return [(self.x+tile_size, self.y-tile_size), (self.x-tile_size, self.y-tile_size), (self.x, self.y)]

    def promotion(self):

        Pieces.all_pieces_list.append(Queens(master = self.master, name = self.name + 'Promoted to Queen', tile_x = self.x, tile_y = self.y, farbe = 'weiss', image = pygame.transform.scale(pygame.image.load(r'assets/white_queen.png'), (tile_size, tile_size))))
        Pieces.all_pieces_list.remove(self)

       