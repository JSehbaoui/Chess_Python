from numpy.lib.shape_base import tile
import pygame
import json
import os
from pygame import mixer
from components.board_cls import Board

json_file = open(os.getcwd()+r"\components\constants.json", "r")
json_content = json.load(json_file)

round_int = json_content["round_int"]
tile_size = json_content["tile_size"]
anchor_point = (json_content["anchor_point_s_x"]*tile_size, json_content["anchor_point_s_y"]*tile_size)

json_file.close()


class Pieces:

    all_pieces_list = []
    taken_pieces = []
    moves_done = []

    white_is_checked = False
    black_is_checked = False

    ignore_me_standard = False

    checking_piece = None

    round_safe = 0

    def __init__(self, master, name, tile_x, tile_y, farbe, image, value):
        self.touched = False
        self.x = tile_x*tile_size
        self.y = tile_y*tile_size
        self.possible_moves = []
        self.master = master
        self.value = value
        self.name = name
        self.image = pygame.transform.scale(image, (int(tile_size*0.7), int(tile_size*0.7)))
        if farbe == 'schwarz':
            self.farbe = (0,0,0)
        elif farbe == 'weiss':
            self.farbe = (255,255,255)
        # Pieces.draw(self)
        Pieces.all_pieces_list.append(self)

    @staticmethod
    def round_increment():

        json_file = open(os.getcwd()+r"\components\constants.json", "r")
        json_content = json.load(json_file)
        json_content["round_int"] += 1
        json_file.close()

        json_file = open(os.getcwd()+r"\components\constants.json", "w")
        json_file.writelines(json.dumps(json_content))
        json_file.close()
        # round_int = json_content["round_int"] 
    
    @staticmethod
    def round_decrement():
        json_file = open(os.getcwd()+r"\components\constants.json", "r")
        json_content = json.load(json_file)
        json_content["round_int"] -= 1
        json_file.close()

        json_file = open(os.getcwd()+r"\components\constants.json", "w")
        json_file.writelines(json.dumps(json_content))
        json_file.close()

    @staticmethod
    def set_round(round):
        json_file = open(os.getcwd()+r"\components\constants.json", "r")
        json_content = json.load(json_file)
        json_content["round_int"] = round
        json_file.close()

        json_file = open(os.getcwd()+r"\components\constants.json", "w")
        json_file.writelines(json.dumps(json_content))
        json_file.close()

    @staticmethod
    def safe_round():
        json_file = open(os.getcwd()+r"\components\constants.json", "r")
        json_content = json.load(json_file)
        Pieces.round_safe = json_content["round_int"]
        json_file.close()
        

    def animate(self, screen, start_pos_x, start_pos_y, stop_pos_x, stop_pos_y, time, board):
        newx = 0
        newy = 0
        counter = 0
        clocktick = 60
        time = time* clocktick

        clock = pygame.time.Clock()

        while counter <= time:

            clock.tick(clocktick)

            dis_vec_x = stop_pos_x-start_pos_x
            dis_vec_y = stop_pos_y-start_pos_y

            speed_x = dis_vec_x/time
            speed_y = dis_vec_y/time


            board.draw_board()
            for piece in Pieces.all_pieces_list:
                if piece != self:
                    piece.draw(screen)
            self.master.blit(self.image, (self.x+0.16*tile_size+newx, self.y+0.16*tile_size+newy))
            screen.blit(self.master, anchor_point)

            pygame.display.update()
            newx+= speed_x
            newy+= speed_y
            counter += 1

    def draw(self, screen):
        #pygame.draw.rect(self.master, self.farbe, [self.x+10, self.y+10, 30, 30])
        self.master.blit(self.image, (self.x+0.16*tile_size, self.y+0.16*tile_size))
        screen.blit(self.master, anchor_point)

    def do_move(move):
        move_start = Board.translate_to_coordinates(move[:2], tile_size) 
        move_end = Board.translate_to_coordinates(move[2:], tile_size) 
        for piece in Pieces.all_pieces_list:
            if piece.x == move_end[0] and piece.y == move_end[1]:
                Pieces.all_pieces_list.remove(piece)
                break
        for piece in Pieces.all_pieces_list:
            if piece.x == move_start[0] and piece.y == move_start[1]:
                piece.x = move_end[0]
                piece.y = move_end[1]
                break
        
        
    def move_from_pos(self, move, board, screen, takeback_button, ignore_me = False):
        if Board.getcurrentTile(self.x, self.y, tile_size) == move[:2]:
            newpos = Board.translate_to_coordinates(move[2:], tile_size)
            self.animate(screen=screen, start_pos_x=self.x, start_pos_y= self.y, stop_pos_x=newpos[0], stop_pos_y=newpos[1], time=0.3, board = board)
            
            old_pos = self.x, self.y

            self.x, self.y = newpos

            Pieces.round_increment()

            if not ignore_me:
                Pieces.moves_done.append(move)

            taken = ''

            if not ignore_me:
                takeback_button.active = True

            for piece in Pieces.all_pieces_list:
                if (piece.x, piece.y) == (self.x, self.y) and self != piece:
                    Pieces.append_taken_piece(piece)
                    taken = 'x'
                    takeback_button.active = False

            if 'King' in self.name:
                if old_pos[0] - self.x > tile_size or self.x - old_pos[0] > tile_size:
                    if self.touched == False:
                        if self.x > 4*tile_size:
                            for rook in Pieces.all_pieces_list:
                                if rook.farbe == self.farbe and 'R-Rook' in rook.name:
                                    move = Board.getcurrentTile(rook.x, rook.y, tile_size) + Board.getcurrentTile(rook.x-2*tile_size, rook.y, tile_size)
                                    rook.move_from_pos(move = move, board = board, screen = screen,takeback_button = takeback_button, ignore_me = True)
                                    Pieces.round_decrement()
                        else:
                            for rook in Pieces.all_pieces_list:
                                if rook.farbe == self.farbe and 'L-Rook' in rook.name:
                                    move = Board.getcurrentTile(rook.x, rook.y, tile_size) + Board.getcurrentTile(rook.x+3*tile_size, rook.y, tile_size)
                                    rook.move_from_pos(move = move, board = board, screen = screen,takeback_button = takeback_button, ignore_me = True)
                                    Pieces.round_decrement()

                    #only if taken back
                    else:
                        if old_pos[0] == 6*tile_size:
                            for rook in Pieces.all_pieces_list:
                                if rook.farbe == self.farbe and 'R-Rook' in rook.name:
                                    move = Board.getcurrentTile(rook.x, rook.y, tile_size) + Board.getcurrentTile(rook.x+2*tile_size, rook.y, tile_size)
                                    rook.move_from_pos(move = move, board = board, screen = screen,takeback_button = takeback_button, ignore_me = True)
                                    Pieces.round_decrement()
                                    self.touched = False
                        elif old_pos[0] == 2*tile_size:
                            for rook in Pieces.all_pieces_list:
                                if rook.farbe == self.farbe and 'L-Rook' in rook.name:
                                    move = Board.getcurrentTile(rook.x, rook.y, tile_size) + Board.getcurrentTile(rook.x-3*tile_size, rook.y, tile_size)
                                    rook.move_from_pos(move = move, board = board, screen = screen,takeback_button = takeback_button, ignore_me = True)
                                    Pieces.round_decrement()
                                    self.touched = False

            self.touched = True

            output = move, self.name, taken
            return output

    
    def move(self, board, screen, takeback_button, ignore_me = False):
    
        go = True
        ok = True
        move = ''


        while go:

            if not (self.getPossible_Moves() == None):
                for tile in self.getPossible_Moves():
                    board.drawBorder(tile, screen)
            
                for pieces in Pieces.all_pieces_list:
                    pieces.draw(screen)

                highlight_color = (0,0,0)

                #color_a = (245, 216, 188), color_b = (176, 142, 109)

                if self.y/tile_size % 2 == 0:
                    if self.x/tile_size % 2 == 0:
                        highlight_color = (189, 204, 157)
                    else:
                        highlight_color = (158, 173, 134)
                else:
                    if self.x/tile_size % 2 == 0:
                        highlight_color = (158, 173, 134)
                    else:
                        highlight_color = (189, 204, 157)
                
                board.changeTilecolor(tile = (self.x, self.y), newColor = highlight_color)

                pygame.display.update()

            taken = ''


            #checking for events
            for event in pygame.event.get():

                #Mouse-Inputs
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pos = (mouse_pos[0]-anchor_point[0], mouse_pos[1]-anchor_point[1])

                    #if the clicked tile is a sqaure, where the pawn can go, move it
                              
                    if not(self.getPossible_Moves() == None):
                        for possible_move in self.getPossible_Moves():
                            if mouse_pos[0] >= possible_move[0] and mouse_pos[1] >=possible_move[1]:
                                if mouse_pos[0] < possible_move[0]+tile_size and mouse_pos[1] < possible_move[1]+tile_size:
                                    for piece in Pieces.all_pieces_list:
                                        if mouse_pos[0] >= piece.x and mouse_pos[1] >= piece.y:
                                            if mouse_pos[0] < piece.x+tile_size and mouse_pos[1] < piece.y+tile_size:
                                                if self.farbe != piece.farbe:
                                                    go = False
                                                    ok = False

                                                    Pieces.round_increment()

                                                    old_pos = (self.x, self.y)

                                                    self.animate(screen = screen, start_pos_x = self.x, start_pos_y = self.y, stop_pos_x = possible_move[0], stop_pos_y = possible_move[1], time = 0.3, board = board)
                                                    self.x = possible_move[0]
                                                    self.y = possible_move[1]

                                                    
                                                    move = Board.getcurrentTile(old_pos[0], old_pos[1], tile_size) + Board.getcurrentTile(self.x, self.y, tile_size) 

                                                    self.touched = True

                                                    Pieces.draw(self, screen)
                                                    if not ignore_me:
                                                        Pieces.moves_done.append(move)

                                                    self.append_taken_piece(piece)

                                                    taken = 'x'

                                                    takeback_button.active = False

                                                    sound_take = mixer.Sound("./assets/sounds/piece-capture.mp3")
                                                    sound_take.play()

                                                    
                                                else:
                                                    ok = False 


                                        
                                    if ok: 

                                        sound_slide = mixer.Sound("./assets/sounds/piece-slide.mp3")
                                        sound_slide.play()
                                        
                                        self.animate(screen, self.x, self.y, possible_move[0], possible_move[1], 0.3, board = board)
                                    
                                        old_pos = (self.x, self.y)

                                        self.x = possible_move[0]
                                        self.y = possible_move[1]
                                        Pieces.draw(self, screen)
                                        Pieces.round_increment()
                                        go = False

                                        

                                        self.touched = True
                                        move = Board.getcurrentTile(old_pos[0], old_pos[1], tile_size) + Board.getcurrentTile(self.x, self.y, tile_size) 

                                        if not ignore_me:
                                            Pieces.moves_done.append(move)

                                        if 'King' in self.name:
                                            if old_pos[0] - self.x > tile_size or self.x - old_pos[0] > tile_size:
                                                if self.x > 4*tile_size:
                                                    for rook in Pieces.all_pieces_list:
                                                        if rook.farbe == self.farbe and 'R-Rook' in rook.name:
                                                            move = Board.getcurrentTile(rook.x, rook.y, tile_size) + Board.getcurrentTile(rook.x-2*tile_size, rook.y, tile_size)
                                                            rook.move_from_pos(move = move, board = board, screen = screen, takeback_button = takeback_button,ignore_me = True)
                                                            Pieces.round_decrement()
                                                else:
                                                    for rook in Pieces.all_pieces_list:
                                                        if rook.farbe == self.farbe and 'L-Rook' in rook.name:
                                                            move = Board.getcurrentTile(rook.x, rook.y, tile_size) + Board.getcurrentTile(rook.x+3*tile_size, rook.y, tile_size)
                                                            rook.move_from_pos(move = move, board = board, screen = screen, takeback_button = takeback_button,ignore_me = True)
                                                            Pieces.round_decrement()
                                                
                                        self.touched = True

                                        takeback_button.active = True

                                        # if 'Pawn_B' in self.name and self.x == 350 or 'Pawn_W' in self.name and self.x == 0:
                                        #     self.promotion()
                                
                                else:
                                    go = False
                            else:
                                go = False        
                    go = False     
        
        
        return move, self.name, taken

    @staticmethod
    def append_taken_piece(piece):
        Pieces.taken_pieces.append(piece)
        Pieces.all_pieces_list.remove(piece)
                
    def getPossible_Moves(self):
        return ''

    def promotion(self):
        pass

    def check_row_tiles(self, current_moves, step_x, step_y, attacking):
        free_bool = False
        go = True
        num = 0
        while go and num < 10:
            num += 1
            testing_move = (self.x+step_x*num, self.y+step_y*num)

            for piece in Pieces.all_pieces_list:
                if testing_move[0] == piece.x and testing_move[1] == piece.y:
                    go = False
                    if attacking:
                        free_bool = True
                    else:
                        if self.farbe == piece.farbe:
                            free_bool = False
                        else:
                            free_bool = True
                        break
                else:
                    free_bool = True

            if free_bool:
                current_moves.append(testing_move)
                free_bool = False
        
    def check_row_tiles_wo_king(self, current_moves, step_x, step_y, attacking):
        free_bool = False
        go = True
        num = 0
        while go and num < 10:
            num += 1
            testing_move = (self.x+step_x*num, self.y+step_y*num)

            for piece in Pieces.all_pieces_list:
                if not (piece.name == "King-B" or piece.name == "King-W"):
                    if testing_move[0] == piece.x and testing_move[1] == piece.y:
                        go = False
                        if attacking:
                            free_bool = True
                        else:
                            if self.farbe == piece.farbe:
                                free_bool = False
                            else:
                                free_bool = True
                            break
                    else:
                        free_bool = True

            if free_bool:
                current_moves.append(testing_move)
                free_bool = False
        


        return current_moves

    def attacked_tiles(self):
        attacted_tiles = self.getPossible_Moves()
        attacted_tiles.append((self.x, self.y))

        return attacted_tiles

    def attacking_line(self):
        pass

    @classmethod
    def check_limitation(cls, possible_moves):
        finite_moves = []
        if (Pieces.white_is_checked or Pieces.black_is_checked):
            if not ("King" in Pieces.checking_piece.name or "Pawn" in Pieces.checking_piece.name or "Knight" in Pieces.checking_piece.name):

                enemy_moves = Pieces.checking_piece.attacking_line()
                for possible_move in possible_moves:
                    for enemy_move in enemy_moves:
                        if enemy_move == possible_move or possible_move == (Pieces.checking_piece.x, Pieces.checking_piece.y):
                            finite_moves.append(possible_move)

                return finite_moves
            else:
                for move in possible_moves:
                    if (Pieces.checking_piece.x, Pieces.checking_piece.y) == move:
                        return [move]
        else:
            return possible_moves
    
    @staticmethod
    def detectingCheck(ignoring_piece = None):
        # if round_int % 2 == 0: #
        for white_king in Pieces.all_pieces_list:
            if 'King' in white_king.name and white_king.farbe == (255, 255, 255):
                for piece in Pieces.all_pieces_list:
                    if piece != white_king and piece.farbe != white_king.farbe and piece != ignoring_piece:
                        if (white_king.x, white_king.y) in piece.attacked_tiles():
                            Pieces.white_is_checked = True
                            Pieces.checking_piece = piece
                            break
                        else:
                            Pieces.white_is_checked = False
                if not Pieces.white_is_checked:
                    Pieces.checking_piece = None

        # detecting if the black king is checked #
        # else:
        for black_king in Pieces.all_pieces_list:
            if 'King' in black_king.name and black_king.farbe == (0, 0, 0):
                for piece in Pieces.all_pieces_list:
                    if piece != black_king and piece.farbe != black_king.farbe and piece != ignoring_piece:
                        if (black_king.x, black_king.y) in piece.attacked_tiles():
                            Pieces.black_is_checked = True
                            Pieces.checking_piece = piece
                            break
                        else:
                            Pieces.black_is_checked = False
                if not Pieces.black_is_checked:
                    Pieces.checking_piece = None


    def foresight(self, possible_moves):
        
        old_pos = self.x, self.y

        it = filter(self.filter_method_foresight, possible_moves)

        possible_moves = list(it)
            
        self.x, self.y = old_pos

        return possible_moves
    
    @staticmethod
    def filter_method(tuple):
        return tuple[0] >= 0 and tuple[1] >= 0 and tuple[0] <= 7*tile_size and tuple[1] <= 7*tile_size

    def filter_method_foresight(self, move):
        self.x, self.y = move #setting the position of the piece to the move, that you want to check
        ignoring_piece = None #currently no piece has to be ignored

        ### if you want to simulate to take a piece, 
        # without actually taking it, you can just 
        ### ignore it in the .detectingCheck method 
        for piece in Pieces.all_pieces_list:
            if (self.x, self.y) == (piece.x, piece.y) and not (piece == self):
                ignoring_piece = piece

        #checking if the king is checked, after the move
        Pieces.detectingCheck(ignoring_piece = ignoring_piece)

        white_check = bool(Pieces.white_is_checked)
        black_check = bool(Pieces.black_is_checked)
        white_bool = bool(self.farbe == (255,255,255))
        black_bool = bool(self.farbe == (0,0,0))

        #returning if the move is legal or not
        return (white_bool and not white_check) or (black_bool and not black_check)

    @staticmethod
    def detectGameOver(round_int):
        total_moves = []
        if round_int % 2 == 0:
            c = (255,255,255)
        elif round_int % 2 == 1:
            c = (0,0,0)
        
        for white_p in Pieces.all_pieces_list:
            if white_p.farbe == c:
                for x in white_p.getPossible_Moves():
                    total_moves.append(x)
                    
        
        if len(total_moves) == 0:
            return True
        else:
            return False

    @classmethod
    def change_ignore_me_standard(cls):
        cls.ignore_me_standard = not cls.ignore_me_standard

    @classmethod
    def kill_board(cls):
        cls.all_pieces_list = []

    def build_from_list(screen):
        for move in Pieces.moves_done:
            Pieces.do_move(move)
        for piece in Pieces.all_pieces_list:
            piece.draw(screen)

    def is_castle_legal(self):
        left_castle = True
        right_castle = True

        left_castle_p0 = False
        left_castle_p1 = True
        left_castle_p2 = True
        left_castle_p3 = True
        left_castle_p4 = True
        left_castle_p5 = True

        right_castle_p0 = False
        right_castle_p1 = True
        right_castle_p2 = True
        right_castle_p3 = True
        right_castle_p4 = True
        right_castle_p5 = True


        for rook in Pieces.all_pieces_list:
            #checking if left side castle is possible
            if "L-Rook" in rook.name and rook.farbe == self.farbe:
                
                left_castle_p0 = True
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

                #checking for property5: is the king checked
                Pieces.detectingCheck()
                if self.farbe == (0,0,0):
                    left_castle_p5 = not Pieces.black_is_checked
                else:
                    left_castle_p5 = not Pieces.white_is_checked

                
            

            #checking if right side castle is possible
            elif "R-Rook" in rook.name and rook.farbe == self.farbe:
                right_castle_p0 = True

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

                #checking for property5: is the king checked
                Pieces.detectingCheck()
                if self.farbe == (0,0,0):
                    right_castle_p5 = not Pieces.black_is_checked
                else:
                    right_castle_p5 = not Pieces.white_is_checked

        #asseble
        right_castle = right_castle_p0 and right_castle_p1 and right_castle_p2 and right_castle_p3 and right_castle_p4 and right_castle_p5
        left_castle = left_castle_p0 and left_castle_p1 and left_castle_p2 and left_castle_p3 and left_castle_p4 and left_castle_p5
        
        general = right_castle or left_castle

        return general, left_castle, right_castle

    @classmethod
    def give_FEN(cls):
        import numpy

        fen_output = ""

        #creating a helpful array to create fen
        board_arr = numpy.ndarray.tolist(numpy.zeros(shape = (8,8), dtype=numpy.int8))
        for piece in cls.all_pieces_list:
            if not "Knight" in piece.name:
                letter = piece.name[2] if piece.farbe == (255,255,255) else piece.name[2].lower()
            else:
                letter = "N" if piece.farbe == (255,255,255) else "n"
            
            x_ = int(piece.x //tile_size)
            y_ = int(piece.y //tile_size)

            board_arr[y_][x_] = letter

        #creating the first part of fen (board position)
        for line in board_arr:
            counter = 0
            for piece in line:
                if piece == 0:
                    counter += 1
                else:
                    if counter != 0:
                        fen_output = fen_output + str(counter)
                        counter = 0
                    fen_output = fen_output + piece
            if counter != 0:
                fen_output = fen_output + str(counter)
            fen_output = fen_output + "/"

        fen_output = fen_output[:-1] # removing the last "/"

        #creating the second part of fen (whos turn is it)
        json_file = open(os.getcwd()+r"\components\constants.json", "r")
        json_content = json.load(json_file)

        round_int = json_content["round_int"]

        json_file.close()
        
        turn = "w" if round_int % 2 == 0 else "b"
        fen_output = fen_output + " " + turn

        #creating the third part of fen (is castling possible)
        for king in cls.all_pieces_list:
            if "King-W" in king.name:
                o = list(king.is_castle_legal())
                K, Q = o[2], o[1]
            elif "King-B" in king.name:
                o = list(king.is_castle_legal())
                k, q = o[2], o[1]
            else:
                pass
        fen_output = fen_output+" "
        
        if K:
            fen_output = fen_output + "K"
        elif Q:
            fen_output = fen_output + "Q"
        elif k:
            fen_output = fen_output + "k"
        elif q:
            fen_output = fen_output + "q"
        else:
            fen_output = fen_output + "-"

        fen_output = fen_output + f" - 0 {round_int//2 +1}"

        return fen_output
        # for line in board_arr:
        #     print(line)


if __name__ == "__main__":
    pass