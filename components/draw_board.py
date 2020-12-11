import pygame

def draw_board(screen, tile_size):
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