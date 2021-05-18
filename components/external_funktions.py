import random
from components.board_cls import *
from components.pieces_cls import *
from components.pieces_cls import Pieces
from components.pawns_cls import WhitePawns, BlackPawns
from components.bishops_cls import Bishops
from components.rooks_cls import Rooks
from components.knights_cls import Knights
from components.queens_cls import Queens
from components.kings_cls import Kings

def getTurn(round_int):
    if round_int%2 == 0:
        return 'White'
    else:
        return 'Black'

def decideWhoLost(round_int, board, screen):

    Board.resign = True

    if round_int % 2 == 0:
        board.end_screen(winner = 'BLACK', screen_ = screen)
    else:
        board.end_screen(winner = 'WHITE', screen_ = screen)

def takeback(board, screen, takeback_button):
    if len(Pieces.moves_done) > 0:
        taken_back = Pieces.moves_done[-1]

        move_to_do = taken_back[2:]+taken_back[:2]

        coordinates = Board.translate_to_coordinates(move_to_do[:2], tile_size=tile_size)

        Pieces.moves_done.pop(-1)

        for piece in Pieces.all_pieces_list:
            if (piece.x, piece.y) ==  (coordinates[0], coordinates[1]):
                piece.move_from_pos(move_to_do, board, screen, takeback_button, ignore_me = True)
                # Pieces.round_decrement()
        
def changebool(bool):
    bool = not bool

def build_board(mode, s, images):
    if mode == "CHESS 960":
        # CHESS 960
        ran_list =  random.sample([i for i in range(8)], 8)
        WhitePawns(master = s, name = 'A-Pawn-W', tile_x = 0, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'B-Pawn-W', tile_x = 1, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'C-Pawn-W', tile_x = 2, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'D-Pawn-W', tile_x = 3, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'E-Pawn-W', tile_x = 4, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'F-Pawn-W', tile_x = 5, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'G-Pawn-W', tile_x = 6, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'H-Pawn-W', tile_x = 7, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        Rooks(master = s, name = 'L-Rook-W', tile_x = ran_list[0], tile_y = 7, farbe = 'weiss', image = images["white_rook_img"], value = 5)
        Rooks(master = s, name = 'R-Rook-W', tile_x = ran_list[7], tile_y = 7, farbe = 'weiss', image = images["white_rook_img"], value = 5)
        Knights(master = s, name = 'L-Knight-W', tile_x = ran_list[6], tile_y = 7, farbe = 'weiss', image = images["white_knight_img"], value = 3.001)
        Knights(master = s, name = 'R-Knight-W', tile_x = ran_list[1], tile_y = 7, farbe = 'weiss', image = images["white_knight_img"], value = 3.001)
        Bishops(master = s, name = 'L-Bishop-W', tile_x = ran_list[2], tile_y = 7, farbe = 'weiss', image = images["white_bishop_img"], value = 3)
        Bishops(master = s, name = 'R-Bishop-W', tile_x = ran_list[5], tile_y = 7, farbe = 'weiss', image = images["white_bishop_img"], value = 3)
        Queens(master = s, name = '##Queen-W', tile_x = ran_list[3], tile_y = 7, farbe = 'weiss', image = images["white_queen_img"], value = 9)
        Kings(master = s, name = '##King-W', tile_x = ran_list[4], tile_y = 7, farbe = 'weiss', image = images["white_king_img"], value = 100)

        BlackPawns(master = s, name = 'A-Pawn-B', tile_x = 0, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'B-Pawn-B', tile_x = 1, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'C-Pawn-B', tile_x = 2, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'D-Pawn-B', tile_x = 3, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'E-Pawn-B', tile_x = 4, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'F-Pawn-B', tile_x = 5, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'G-Pawn-B', tile_x = 6, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'H-Pawn-B', tile_x = 7, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        Rooks(master = s, name = 'L-Rook-B', tile_x = ran_list[0], tile_y = 0, farbe = 'schwarz', image = images["black_rook_img"], value = 5)
        Rooks(master = s, name = 'R-Rook-B', tile_x = ran_list[7], tile_y = 0, farbe = 'schwarz', image = images["black_rook_img"], value = 5)
        Knights(master = s, name = 'L-Knight-B', tile_x = ran_list[1], tile_y = 0, farbe = 'schwarz', image = images["black_knight_img"], value = 3.001)
        Knights(master = s, name = 'R-Knight-B', tile_x = ran_list[6], tile_y = 0, farbe = 'schwarz', image = images["black_knight_img"], value = 3.001)
        Bishops(master = s, name = 'L-Bishop-B', tile_x = ran_list[2], tile_y = 0, farbe = 'schwarz', image = images["black_bishop_img"], value = 3)
        Bishops(master = s, name = 'R-Bishop-B', tile_x = ran_list[5], tile_y = 0, farbe = 'schwarz', image = images["black_bishop_img"], value = 3)
        Queens(master = s, name = '##Queen-B', tile_x = ran_list[3], tile_y = 0, farbe = 'schwarz', image = images["black_queen_img"], value = 9)
        Kings(master = s, name = '##King-B', tile_x = ran_list[4], tile_y = 0, farbe = 'schwarz', image = images["black_king_img"], value = 100)

    elif mode == "STANDARD":
        # STANDARD
        WhitePawns(master = s, name = 'A-Pawn-W', tile_x = 0, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'B-Pawn-W', tile_x = 1, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'C-Pawn-W', tile_x = 2, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'D-Pawn-W', tile_x = 3, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'E-Pawn-W', tile_x = 4, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'F-Pawn-W', tile_x = 5, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'G-Pawn-W', tile_x = 6, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'H-Pawn-W', tile_x = 7, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        Rooks(master = s, name = 'L-Rook-W', tile_x = 0, tile_y = 7, farbe = 'weiss', image = images["white_rook_img"], value = 5)
        Rooks(master = s, name = 'R-Rook-W', tile_x = 7, tile_y = 7, farbe = 'weiss', image = images["white_rook_img"], value = 5)
        Knights(master = s, name = 'L-Knight-W', tile_x = 6, tile_y = 7, farbe = 'weiss', image = images["white_knight_img"], value = 3.001)
        Knights(master = s, name = 'R-Knight-W', tile_x = 1, tile_y = 7, farbe = 'weiss', image = images["white_knight_img"], value = 3.001)
        Bishops(master = s, name = 'L-Bishop-W', tile_x = 2, tile_y = 7, farbe = 'weiss', image = images["white_bishop_img"], value = 3)
        Bishops(master = s, name = 'R-Bishop-W', tile_x = 5, tile_y = 7, farbe = 'weiss', image = images["white_bishop_img"], value = 3)
        Queens(master = s, name = '##Queen-W', tile_x = 3, tile_y = 7, farbe = 'weiss', image = images["white_queen_img"], value = 9)
        Kings(master = s, name = '##King-W', tile_x = 4, tile_y = 7, farbe = 'weiss', image = images["white_king_img"], value = 100)

        BlackPawns(master = s, name = 'A-Pawn-B', tile_x = 0, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'B-Pawn-B', tile_x = 1, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'C-Pawn-B', tile_x = 2, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'D-Pawn-B', tile_x = 3, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'E-Pawn-B', tile_x = 4, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'F-Pawn-B', tile_x = 5, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'G-Pawn-B', tile_x = 6, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'H-Pawn-B', tile_x = 7, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        Rooks(master = s, name = 'L-Rook-B', tile_x = 0, tile_y = 0, farbe = 'schwarz', image = images["black_rook_img"], value = 5)
        Rooks(master = s, name = 'R-Rook-B', tile_x = 7, tile_y = 0, farbe = 'schwarz', image = images["black_rook_img"], value = 5)
        Knights(master = s, name = 'L-Knight-B', tile_x = 1, tile_y = 0, farbe = 'schwarz', image = images["black_knight_img"], value = 3.001)
        Knights(master = s, name = 'R-Knight-B', tile_x = 6, tile_y = 0, farbe = 'schwarz', image = images["black_knight_img"], value = 3.001)
        Bishops(master = s, name = 'L-Bishop-B', tile_x = 2, tile_y = 0, farbe = 'schwarz', image = images["black_bishop_img"], value = 3)
        Bishops(master = s, name = 'R-Bishop-B', tile_x = 5, tile_y = 0, farbe = 'schwarz', image = images["black_bishop_img"], value = 3)
        Queens(master = s, name = '##Queen-B', tile_x = 3, tile_y = 0, farbe = 'schwarz', image = images["black_queen_img"], value = 9)
        Kings(master = s, name = '##King-B', tile_x = 4, tile_y = 0, farbe = 'schwarz', image = images["black_king_img"], value = 100)

    elif mode == "TESTING":
        #TESTING
        WhitePawns(master = s, name = 'A-Pawn-W', tile_x = 0, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'B-Pawn-W', tile_x = 1, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'C-Pawn-W', tile_x = 2, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'D-Pawn-W', tile_x = 3, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'E-Pawn-W', tile_x = 4, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'F-Pawn-W', tile_x = 5, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'G-Pawn-W', tile_x = 6, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        WhitePawns(master = s, name = 'H-Pawn-W', tile_x = 7, tile_y = 6, farbe = 'weiss', image = images["white_pawn_img"], value = 1)
        Kings(master = s, name = '##King-B', tile_x = 4, tile_y = 0, farbe = 'schwarz', image = images["black_king_img"], value = 100)
        Rooks(master = s, name = 'L-Rook-B', tile_x = 0, tile_y = 0, farbe = 'schwarz', image = images["black_rook_img"], value = 5)

        BlackPawns(master = s, name = 'A-Pawn-B', tile_x = 0, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'B-Pawn-B', tile_x = 1, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'C-Pawn-B', tile_x = 2, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        BlackPawns(master = s, name = 'D-Pawn-B', tile_x = 3, tile_y = 1, farbe = 'schwarz', image = images["black_pawn_img"], value = 1)
        Kings(master = s, name = '##King-W', tile_x = 4, tile_y = 7, farbe = 'weiss', image = images["white_king_img"], value = 100)
        
    