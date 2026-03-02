import pygame
import setup

tile = pygame.image.load("imgs/fishing_tile.png")

class Tile:
    tile_width: int
    tile_height: int

def render_tiles():
    for tile_pos_x in range(0, setup.WIDTH):
        for tile_pos_y in range(0, setup.HEIGHT):
            if tile_pos_x % 32 == 0:
                if tile_pos_y % 32 == 0:
                    tile.blit()
        
