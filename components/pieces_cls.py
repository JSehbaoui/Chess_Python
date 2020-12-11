import pygame
import json
import os

json_file = open(os.getcwd()+r"\constants.json", "r")
json_content = json.load(json_file)

round_int = json_content["round_int"]
print(round_int)
tile_size = 120

class Pieces:
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
        Pieces.draw(self)

    @staticmethod
    def round_increment():
        global round_int
        round_int += 1

    def draw(self):
        #pygame.draw.rect(self.master, self.farbe, [self.x+10, self.y+10, 30, 30])
        self.master.blit(self.image, (self.x+10, self.y+10))

    
    def move(self, occupied_tiles, all_pieces_list):
    
        go = True
        ok = True
        while go:

            for tile in self.getPossible_Moves(all_pieces_list = all_pieces_list):
                pygame.draw.rect(self.master, (152, 186, 0), [tile[0], tile[1], tile_size, tile_size])

                fac1 = tile[0]/tile_size
                fac2 = tile[1]/tile_size  
                prod = fac1+fac2
                if prod % 2 == 0:
                    color = (245, 216, 188)
                else:
                    color = (176, 142, 109)

                pygame.draw.rect(self.master, color , [tile[0]+10, tile[1]+10, tile_size-20, tile_size-20])
            
            for pieces in all_pieces_list:
                pieces.draw()

            pygame.display.update()



            #checking for events
            for event in pygame.event.get():



                #Mouse-Inputs
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()

                    #if the clicked tile is a sqaure, where the pawn can go, move it
                    global round_int
                    
                    # create bool var
                    for possible_move in self.getPossible_Moves(all_pieces_list=all_pieces_list):
                        if mouse_pos[0] >= possible_move[0] and mouse_pos[1] >=possible_move[1]:
                            if mouse_pos[0] < possible_move[0]+tile_size and mouse_pos[1] < possible_move[1]+tile_size:
                                for piece in all_pieces_list:
                                    if mouse_pos[0] >= piece.x and mouse_pos[1] >= piece.y:
                                        if mouse_pos[0] < piece.x+tile_size and mouse_pos[1] < piece.y+tile_size:
                                            if self.farbe != piece.farbe:
                                                go = False
                                                ok = False
                                                print('TAKES')

                                                Pieces.round_increment()

                                                self.x = possible_move[0]
                                                self.y = possible_move[1]
                                                
                                                Pieces.draw(self)
                                                all_pieces_list.remove(piece)

                                                if 'Pawn-B' in self.name and self.y == 490 or 'Pawn-W' in self.name and self.y == 0:
                                                    self.promotion(all_pieces_list = all_pieces_list)



                                                return all_pieces_list
                                            else:
                                                ok = False 


                                                    
                                        else:
                                            pass
                                    else:
                                        pass
                                    
                                if ok: 
                                
                                    self.x = possible_move[0]
                                    self.y = possible_move[1]
                                    Pieces.draw(self)
                                    print('Moved')
                                    Pieces.round_increment()
                                    go = False

                                    if 'Pawn_B' in self.name and self.x == 350 or 'Pawn_W' in self.name and self.x == 0:
                                        self.promotion(all_pieces_list = all_pieces_list)
                            
                            else:
                                go = False
                        else:
                            go = False        
                    go = False
            
                
            



    def check_row_tiles(self, current_moves, step_x, step_y, all_pieces_list, attacking):
        free_bool = False
        go = True
        num = 0
        while go and num < 10:
            num += 1
            testing_move = (self.x+step_x*num, self.y+step_y*num)

            for piece in all_pieces_list:
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

    def attacted_tiles(self, all_pieces_list):
        attacted_tiles = self.getPossible_Moves(all_pieces_list=all_pieces_list)

        return attacted_tiles





