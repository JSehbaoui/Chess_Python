from components.pieces_cls import Pieces
# from components.board_cls import Board

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