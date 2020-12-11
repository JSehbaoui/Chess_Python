import pygame
from .pieces_cls import Pieces

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
