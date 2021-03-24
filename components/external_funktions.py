from components.board_cls import *

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
