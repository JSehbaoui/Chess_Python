import pygame
from pieces_cls import Pieces

class Queens(Pieces):
    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        super().__init__(master, name, tile_x, tile_y, farbe, image)
    
    def getPossible_Moves(self, all_pieces_list):
        possible_moves = []

        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = 0, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= tile_size*-1, step_y = 0, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = False)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = False)
 
        return possible_moves

    def attacted_tiles(self, all_pieces_list):
        possible_moves = []
        
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size*-1, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x = tile_size, step_y = 0, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x= tile_size*-1, step_y = 0, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size, all_pieces_list = all_pieces_list, attacking = True)
        self.check_row_tiles(current_moves = possible_moves, step_x= 0, step_y = tile_size*-1, all_pieces_list = all_pieces_list, attacking = True)

        return possible_moves