import pygame
import json
import os

json_file = open(os.getcwd()+r"\components\constants.json", "r")
json_content = json.load(json_file)

round_int = json_content["round_int"]
tile_size = json_content["tile_size"]
anchor_point = (json_content["anchor_point_s_x"]*tile_size, json_content["anchor_point_s_y"]*tile_size)

json_file.close()


class Pieces:

    all_pieces_list = []

    white_is_checked = False
    black_is_checked = False

    checking_piece = None

    def __init__(self, master, name, tile_x, tile_y, farbe, image):
        self.x = tile_x*tile_size
        self.y = tile_y*tile_size
        self.possible_moves = []
        self.master = master
        self.name = name
        self.image = pygame.transform.scale(image, (tile_size-20, tile_size-20))
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
            self.master.blit(self.image, (self.x+10+newx, self.y+10+newy))
            screen.blit(self.master, anchor_point)

            pygame.display.update()
            newx+= speed_x
            newy+= speed_y
            counter += 1

    def draw(self, screen):
        #pygame.draw.rect(self.master, self.farbe, [self.x+10, self.y+10, 30, 30])
        self.master.blit(self.image, (self.x+10, self.y+10))
        screen.blit(self.master, anchor_point)
    
    def move(self, occupied_tiles, board, screen):
    
        go = True
        ok = True


        while go:

            for tile in self.getPossible_Moves():
                board.drawBorder(tile, screen)
                
            
            for pieces in Pieces.all_pieces_list:
                pieces.draw(screen)

            pygame.display.update()



            #checking for events
            for event in pygame.event.get():



                #Mouse-Inputs
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pos = (mouse_pos[0]-anchor_point[0], mouse_pos[1]-anchor_point[1])

                    #if the clicked tile is a sqaure, where the pawn can go, move it
                    
                    
                    # create bool var
                    for possible_move in self.getPossible_Moves():
                        if mouse_pos[0] >= possible_move[0] and mouse_pos[1] >=possible_move[1]:
                            if mouse_pos[0] < possible_move[0]+tile_size and mouse_pos[1] < possible_move[1]+tile_size:
                                for piece in Pieces.all_pieces_list:
                                    if mouse_pos[0] >= piece.x and mouse_pos[1] >= piece.y:
                                        if mouse_pos[0] < piece.x+tile_size and mouse_pos[1] < piece.y+tile_size:
                                            if self.farbe != piece.farbe:
                                                go = False
                                                ok = False
                                                print('TAKES')

                                                Pieces.round_increment()

                                                self.animate(screen = screen, start_pos_x = self.x, start_pos_y = self.y, stop_pos_x = possible_move[0], stop_pos_y = possible_move[1], time = 0.2, board = board)
                                                self.x = possible_move[0]
                                                self.y = possible_move[1]
                                                
                                                Pieces.draw(self, screen)
                                                Pieces.all_pieces_list.remove(piece)

                                                if 'Pawn-B' in self.name and self.y == 490 or 'Pawn-W' in self.name and self.y == 0:
                                                    self.promotion()



                                                
                                            else:
                                                ok = False 


                                                    
                                        else:
                                            pass
                                    else:
                                        pass
                                    
                                if ok: 

                                    self.animate(screen, self.x, self.y, possible_move[0], possible_move[1], 0.2, board = board)
                                
                                    self.x = possible_move[0]
                                    self.y = possible_move[1]
                                    Pieces.draw(self, screen)
                                    print('Moved')
                                    Pieces.round_increment()
                                    go = False

                                    if 'Pawn_B' in self.name and self.x == 350 or 'Pawn_W' in self.name and self.x == 0:
                                        self.promotion()
                            
                            else:
                                go = False
                        else:
                            go = False        
                    go = False     
                
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

    def attacted_tiles(self):
        attacted_tiles = self.getPossible_Moves()
        attacted_tiles.append((self.x, self.y))

        return attacted_tiles
