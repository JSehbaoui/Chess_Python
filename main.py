import pygame
import json
import os
from components.pieces_cls import Pieces
from components.pawns_cls import WhitePawns, BlackPawns
from components.bishops_cls import Bishops
from components.rooks_cls import Rooks
from components.knights_cls import Knights
from components.queens_cls import Queens
from components.kings_cls import Kings
from components.draw_board import draw_board

json_file = open(r'components\constants.json', 'r')
json_content = json.load(json_file)
json_content["round_int"] = 0
json_file.close()

json_file = open(r'components\constants.json', 'w')
json_file.writelines(json.dumps(json_content))
json_file.close()


def main():
    pygame.init()

    json_file = open(os.getcwd()+r"\components\constants.json", "r")
    json_content = json.load(json_file)

    round_int = json_content["round_int"]
    tile_size = json_content["tile_size"]

    json_file.close()

    screen_size = (8*tile_size, 8*tile_size)

    go = True
    Pieces.white_is_checked = False
    Pieces.black_is_checked = False    

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Chess")

    clock = pygame.time.Clock()

    #creating the board
    



    draw_board(screen = screen, tile_size = tile_size)
    #summoning the Pieces

    white_pawn_img = pygame.image.load(r'assets/white_pawn.png')
    white_rook_img = pygame.image.load(r'assets/white_rook.png')
    white_knight_img = pygame.image.load(r'assets/white_knight.png')
    white_bishop_img = pygame.image.load(r'assets/white_bishop.png')
    white_queen_img = pygame.image.load(r'assets/white_queen.png')
    white_king_img = pygame.image.load(r'assets/white_king.png')

    black_pawn_img = pygame.image.load(r'assets/black_pawn.png')
    black_rook_img = pygame.image.load(r'assets/black_rook.png')
    black_knight_img = pygame.image.load(r'assets/black_knight.png')
    black_bishop_img = pygame.image.load(r'assets/black_bishop.png')
    black_queen_img = pygame.image.load(r'assets/black_queen.png')
    black_king_img = pygame.image.load(r'assets/black_king.png')


    white_pawn_img = pygame.transform.scale(white_pawn_img, (tile_size, tile_size))
    white_rook_img = pygame.transform.scale(white_rook_img, (tile_size, tile_size))
    white_knight_img = pygame.transform.scale(white_knight_img, (tile_size, tile_size))
    white_bishop_img = pygame.transform.scale(white_bishop_img, (tile_size, tile_size))
    white_queen_img = pygame.transform.scale(white_queen_img, (tile_size, tile_size))
    white_king_img = pygame.transform.scale(white_king_img, (tile_size, tile_size))

    black_pawn_img = pygame.transform.scale(black_pawn_img, (tile_size, tile_size))
    black_rook_img = pygame.transform.scale(black_rook_img, (tile_size, tile_size))
    black_knight_img = pygame.transform.scale(black_knight_img, (tile_size, tile_size))
    black_bishop_img = pygame.transform.scale(black_bishop_img, (tile_size, tile_size))
    black_queen_img = pygame.transform.scale(black_queen_img, (tile_size, tile_size))
    black_king_img = pygame.transform.scale(black_king_img, (tile_size, tile_size))


    # Keine magicnumbers (num_7 = 7)
    WhitePawns(master = screen, name = 'A-Pawn-W', tile_x = 0, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = screen, name = 'B-Pawn-W', tile_x = 1, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = screen, name = 'C-Pawn-W', tile_x = 2, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = screen, name = 'D-Pawn-W', tile_x = 3, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = screen, name = 'E-Pawn-W', tile_x = 4, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = screen, name = 'F-Pawn-W', tile_x = 5, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = screen, name = 'G-Pawn-W', tile_x = 6, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = screen, name = 'H-Pawn-W', tile_x = 7, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    Rooks(master = screen, name = 'L-Rook-W', tile_x = 0, tile_y = 7, farbe = 'weiss', image = white_rook_img)
    Rooks(master = screen, name = 'R-Rook-W', tile_x = 7, tile_y = 7, farbe = 'weiss', image = white_rook_img)
    Knights(master = screen, name = 'L-Knight-W', tile_x = 6, tile_y = 7, farbe = 'weiss', image = white_knight_img)
    Knights(master = screen, name = 'R-Knight-W', tile_x = 1, tile_y = 7, farbe = 'weiss', image = white_knight_img)
    Bishops(master = screen, name = 'L-Bishop-W', tile_x = 2, tile_y = 7, farbe = 'weiss', image = white_bishop_img)
    Bishops(master = screen, name = 'R-Bishop-W', tile_x = 5, tile_y = 7, farbe = 'weiss', image = white_bishop_img)
    Queens(master = screen, name = 'Queen-W', tile_x = 3, tile_y = 7, farbe = 'weiss', image = white_queen_img)
    Kings(master = screen, name = 'King-W', tile_x = 4, tile_y = 7, farbe = 'weiss', image = white_king_img)
    BlackPawns(master = screen, name = 'A-Pawn-B', tile_x = 0, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = screen, name = 'B-Pawn-B', tile_x = 1, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = screen, name = 'C-Pawn-B', tile_x = 2, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = screen, name = 'D-Pawn-B', tile_x = 3, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = screen, name = 'E-Pawn-B', tile_x = 4, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = screen, name = 'F-Pawn-B', tile_x = 5, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = screen, name = 'G-Pawn-B', tile_x = 6, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = screen, name = 'H-Pawn-B', tile_x = 7, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    Rooks(master = screen, name = 'L-Rook-B', tile_x = 0, tile_y = 0, farbe = 'schwarz', image = black_rook_img)
    Rooks(master = screen, name = 'R-Rook-B', tile_x = 7, tile_y = 0, farbe = 'schwarz', image = black_rook_img)
    Knights(master = screen, name = 'L-Knight-B', tile_x = 1, tile_y = 0, farbe = 'schwarz', image = black_knight_img)
    Knights(master = screen, name = 'R-Knight-B', tile_x = 6, tile_y = 0, farbe = 'schwarz', image = black_knight_img)
    Bishops(master = screen, name = 'L-Bishop-B', tile_x = 2, tile_y = 0, farbe = 'schwarz', image = black_bishop_img)
    Bishops(master = screen, name = 'R-Bishop-B', tile_x = 5, tile_y = 0, farbe = 'schwarz', image = black_bishop_img)
    Queens(master = screen, name = 'Queen-B', tile_x = 3, tile_y = 0, farbe = 'schwarz', image = black_queen_img)
    Kings(master = screen, name = 'King-B', tile_x = 4, tile_y = 0, farbe = 'schwarz', image = black_king_img)
    


    occupied_tiles = [] 

    while go:

        #Frames
        clock.tick(60)

        occupied_tiles.clear()

        for piece in Pieces.all_pieces_list:
            occupied_tiles.append((piece.x, piece.y))

        json_file = open(os.getcwd()+r"\components\constants.json", "r")
        json_content = json.load(json_file)

        round_int = json_content["round_int"]
        tile_size = json_content["tile_size"]

        json_file.close()

        #creating the board
        draw_board(screen = screen, tile_size = tile_size)


        if Pieces.white_is_checked:
            for king in Pieces.all_pieces_list:
                if isinstance(king, Kings):
                    pygame.draw.rect(screen, (247, 87, 87), [king.x, king.y, tile_size, tile_size])
    
        elif Pieces.black_is_checked:
            for king in Pieces.all_pieces_list:
                if isinstance(king, Kings):
                    pygame.draw.rect(screen, (247, 87, 87), [King_black.x, King_black.y, tile_size, tile_size])

        #draw all the pieces
        for pieces in Pieces.all_pieces_list:
            pieces.draw()

        pygame.display.update()

        #checking for events
        for event in pygame.event.get():

            #closing the screen by clicking the X
            if event.type == pygame.QUIT:
                go = False
 
            #Keyboard-Inputs
            if event.type == pygame.KEYDOWN:
                #kill window if ESC is pressed
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                if event.key == pygame.K_DOWN:
                    pass
            #Mouse-Inputs
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

                #checking if a Piece stands on the clicked tile
                for piece in Pieces.all_pieces_list:
                    if mouse_pos[0] >= piece.x and mouse_pos[1] >=piece.y:
                        if mouse_pos[0] < piece.x+tile_size and mouse_pos[1] < piece.y+tile_size:

                            if round_int % 2 == 1 and piece.farbe == (0,0,0) or round_int % 2 == 0 and piece.farbe == (255, 255, 255):

                                piece.move(occupied_tiles = occupied_tiles)


                                for white_king in Pieces.all_pieces_list:
                                    if isinstance(white_king, Kings) and white_king.farbe == (255, 255, 255):
                                        for piece in Pieces.all_pieces_list:
                                            if piece != white_king and piece.farbe != white_king.farbe:
                                                if (white_king.x, white_king.y) in piece.attacted_tiles():
                                                    Pieces.white_is_checked = True
                                                    Pieces.checking_piece = piece
                                                    break
                                                else:
                                                    Pieces.white_is_checked = False
                                                    Pieces.checking_piece = None

                                for black_king in Pieces.all_pieces_list:
                                    if type(black_king) == type(Kings) and black_king.farbe == (0, 0, 0):
                                        for piece in Pieces.all_pieces_list:
                                            if piece != black_king and piece.farbe != black_king.farbe:
                                                if (black_king.x, black_king.y) in piece.attacted_tiles():
                                                    Pieces.black_is_checked = True
                                                    Pieces.checking_piece = piece
                                                    break
                                                else:
                                                    Pieces.black_is_checked = False
                                                    Pieces.checking_piece = None

                                if Pieces.white_is_checked or Pieces.black_is_checked:
                                    print('Someone is checked')
    
    json_file = open(r'components\constants.json', 'r')
    json_content = json.load(json_file)
    json_content["round_int"] = 0
    json_file.close()

    json_file = open(r'components\constants.json', 'w')
    json_file.writelines(json.dumps(json_content))
    json_file.close()


if __name__ == '__main__':

    main()

