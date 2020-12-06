import pygame
from components.pieces_cls import *

tile_size = 120
round_int = 0


def main():
    pygame.init()

    screen_size = (8*tile_size, 8*tile_size)

    go = True
    white_is_checked = False
    black_is_checked = False    

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Chess")

    clock = pygame.time.Clock()

    brown = pygame.Color(179,140,94)

    #creating the board
    tile_dir_list = []
    for y in range(8):
        tile_dir_list.append([])
        for x in range(8):
            tile_dir_list[y].append((x*tile_size, y*tile_size))
            if y % 2 == 0:
                if x % 2 == 0:
                    pygame.draw.rect(screen, (245, 216, 188), [x*tile_size, y*tile_size, tile_size, tile_size])
                else:
                    pygame.draw.rect(screen, (176, 142, 109), [x*tile_size, y*tile_size, tile_size, tile_size])
            else:
                if x % 2 == 0:
                    pygame.draw.rect(screen, (176, 142, 109), [x*tile_size, y*tile_size, tile_size, tile_size])
                else:
                    pygame.draw.rect(screen, (245, 216, 188), [x*tile_size, y*tile_size, tile_size, tile_size])


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
    A_Pawn_white =      WhitePawns(master = screen, name = 'A-Pawn-W', tile_x = 0, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    B_Pawn_white =      WhitePawns(master = screen, name = 'B-Pawn-W', tile_x = 1, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    C_Pawn_white =      WhitePawns(master = screen, name = 'C-Pawn-W', tile_x = 2, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    D_Pawn_white =      WhitePawns(master = screen, name = 'D-Pawn-W', tile_x = 3, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    E_Pawn_white =      WhitePawns(master = screen, name = 'E-Pawn-W', tile_x = 4, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    F_Pawn_white =      WhitePawns(master = screen, name = 'F-Pawn-W', tile_x = 5, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    G_Pawn_white =      WhitePawns(master = screen, name = 'G-Pawn-W', tile_x = 6, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    H_Pawn_white =      WhitePawns(master = screen, name = 'H-Pawn-W', tile_x = 7, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    L_Rook_white =      Rooks(master = screen, name = 'L-Rook-W', tile_x = 0, tile_y = 7, farbe = 'weiss', image = white_rook_img)
    R_Rook_white =      Rooks(master = screen, name = 'R-Rook-W', tile_x = 7, tile_y = 7, farbe = 'weiss', image = white_rook_img)
    L_Knight_white =    Knights(master = screen, name = 'L-Knight-W', tile_x = 6, tile_y = 7, farbe = 'weiss', image = white_knight_img)
    R_Knight_white =    Knights(master = screen, name = 'R-Knight-W', tile_x = 1, tile_y = 7, farbe = 'weiss', image = white_knight_img)
    L_Bishop_white =   Bishops(master = screen, name = 'L-Bishop-W', tile_x = 2, tile_y = 7, farbe = 'weiss', image = white_bishop_img)
    R_Bishop_white =   Bishops(master = screen, name = 'R-Bishop-W', tile_x = 5, tile_y = 7, farbe = 'weiss', image = white_bishop_img)
    Queen_white =       Queens(master = screen, name = 'Queen-W', tile_x = 3, tile_y = 7, farbe = 'weiss', image = white_queen_img)
    King_white =        Kings(master = screen, name = 'King-W', tile_x = 4, tile_y = 7, farbe = 'weiss', image = white_king_img)
    
    

    A_Pawn_black =      BlackPawns(master = screen, name = 'A-Pawn-B', tile_x = 0, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    B_Pawn_black =      BlackPawns(master = screen, name = 'B-Pawn-B', tile_x = 1, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    C_Pawn_black =      BlackPawns(master = screen, name = 'C-Pawn-B', tile_x = 2, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    D_Pawn_black =      BlackPawns(master = screen, name = 'D-Pawn-B', tile_x = 3, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    E_Pawn_black =      BlackPawns(master = screen, name = 'E-Pawn-B', tile_x = 4, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    F_Pawn_black =      BlackPawns(master = screen, name = 'F-Pawn-B', tile_x = 5, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    G_Pawn_black =      BlackPawns(master = screen, name = 'G-Pawn-B', tile_x = 6, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    H_Pawn_black =      BlackPawns(master = screen, name = 'H-Pawn-B', tile_x = 7, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    L_Rook_black =      Rooks(master = screen, name = 'L-Rook-B', tile_x = 0, tile_y = 0, farbe = 'schwarz', image = black_rook_img)
    R_Rook_black =      Rooks(master = screen, name = 'R-Rook-B', tile_x = 7, tile_y = 0, farbe = 'schwarz', image = black_rook_img)
    L_Knight_black =    Knights(master = screen, name = 'L-Knight-B', tile_x = 1, tile_y = 0, farbe = 'schwarz', image = black_knight_img)
    R_Knight_black =    Knights(master = screen, name = 'R-Knight-B', tile_x = 6, tile_y = 0, farbe = 'schwarz', image = black_knight_img)
    L_Bishop_black =   Bishops(master = screen, name = 'L-Bishop-B', tile_x = 2, tile_y = 0, farbe = 'schwarz', image = black_bishop_img)
    R_Bishop_black =   Bishops(master = screen, name = 'R-Bishop-B', tile_x = 5, tile_y = 0, farbe = 'schwarz', image = black_bishop_img)
    Queen_black =       Queens(master = screen, name = 'Queen-B', tile_x = 3, tile_y = 0, farbe = 'schwarz', image = black_queen_img)
    King_black =        Kings(master = screen, name = 'King-B', tile_x = 4, tile_y = 0, farbe = 'schwarz', image = black_king_img)
    
    

    all_pieces_list =[
                        A_Pawn_white, B_Pawn_white, C_Pawn_white, D_Pawn_white,
                        E_Pawn_white, F_Pawn_white, G_Pawn_white, H_Pawn_white,
                        L_Rook_white, R_Rook_white, L_Knight_white, R_Knight_white,
                        L_Bishop_white, R_Bishop_white, Queen_white, King_white,
                        A_Pawn_black, B_Pawn_black, C_Pawn_black, D_Pawn_black,
                        E_Pawn_black, F_Pawn_black, G_Pawn_black, H_Pawn_black,
                        L_Rook_black, R_Rook_black, L_Knight_black, R_Knight_black,
                        L_Bishop_black, R_Bishop_black, Queen_black, King_black                        
                     ]

    occupied_tiles = []

    # DOENST WORK QUIET YET !!!!!!!!!!! 



    # round_int = 0 

    while go:

        #Frames
        clock.tick(30)

        occupied_tiles.clear()

        for piece in all_pieces_list:
            occupied_tiles.append((piece.x, piece.y))

        #creating the board
        for y in range(8):
            for x in range(8):
                if y % 2 == 0:
                    if x % 2 == 0:
                        pygame.draw.rect(screen, (245, 216, 188), [x*tile_size, y*tile_size, tile_size, tile_size])
                    else:
                        pygame.draw.rect(screen, (176, 142, 109), [x*tile_size, y*tile_size, tile_size, tile_size])
                else:
                    if x % 2 == 0:
                        pygame.draw.rect(screen, (176, 142, 109), [x*tile_size, y*tile_size, tile_size, tile_size])
                    else:
                        pygame.draw.rect(screen, (245, 216, 188), [x*tile_size, y*tile_size, tile_size, tile_size])


        if white_is_checked:
            pygame.draw.rect(screen, (247, 87, 87), [King_white.x, King_white.y, tile_size, tile_size])
    
        elif black_is_checked:
            pygame.draw.rect(screen, (247, 87, 87), [King_black.x, King_black.y, tile_size, tile_size])

        #draw all the pieces
        for pieces in all_pieces_list:
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
                    print(type(King_black))
            #Mouse-Inputs
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

                #checking if a Piece stands on the clicked tile
                for piece in all_pieces_list:
                    if mouse_pos[0] >= piece.x and mouse_pos[1] >=piece.y:
                        if mouse_pos[0] < piece.x+tile_size and mouse_pos[1] < piece.y+tile_size:
                            from components.pieces_cls import round_int
                            if round_int % 2 == 1 and piece.farbe == (0,0,0) or round_int % 2 == 0 and piece.farbe == (255, 255, 255):

                                if (white_is_checked or black_is_checked) and str(type(piece)) == "<class 'components.pieces_cls.Kings'>":
                                    piece.move(occupied_tiles=occupied_tiles, all_pieces_list = all_pieces_list)

                                elif (white_is_checked or black_is_checked) and str(type(piece)) != "<class 'components.pieces_cls.Kings'>":
                                    print('You have to deny check')

                                else:
                                    piece.move(occupied_tiles=occupied_tiles, all_pieces_list = all_pieces_list)


                                for white_king in all_pieces_list:
                                    if str(type(white_king)) == "<class 'components.pieces_cls.Kings'>" and white_king.farbe == (255, 255, 255):
                                        for piece in all_pieces_list:
                                            if piece != white_king and piece.farbe != white_king.farbe:
                                                if (white_king.x, white_king.y) in piece.attacted_tiles(all_pieces_list = all_pieces_list):
                                                    white_is_checked = True
                                                    checking_piece = piece
                                                    break
                                                else:
                                                    white_is_checked = False
                                                    checking_piece = None

                                for black_king in all_pieces_list:
                                    if str(type(black_king)) == "<class 'components.pieces_cls.Kings'>" and black_king.farbe == (0, 0, 0):
                                        for piece in all_pieces_list:
                                            if piece != black_king and piece.farbe != black_king.farbe:
                                                if (black_king.x, black_king.y) in piece.attacted_tiles(all_pieces_list = all_pieces_list):
                                                    black_is_checked = True
                                                    checking_piece = piece
                                                    break
                                                else:
                                                    black_is_checked = False
                                                    checking_piece = None

                                if white_is_checked or black_is_checked:
                                    print('Someone is checked')


if __name__ == '__main__':

    main()

