import sys
import time
import random

# Importing another pyhton file.
import colors

# Modules you need to install.
import pygame
from pygame.locals import *


BOARD_SIZE = 4
TOTAL_POINTS = 0
DEFAULT_SCORE = 2


def init_pygame():
    pygame.init()
    clock = pygame.time.Clock()
    screen_height = 500
    screen_width = 400
    surface = pygame.display.set_mode(size=(screen_width, screen_height))
    pygame.display.set_caption("2048")

    default_font = pygame.font.SysFont("cosmicsansms", 40)
    score_font = pygame.font.SysFont("cosmicsansms", 25)
    tile_matrxi = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    reset_matrix = []


def main():
    loaded = False

    if not loaded:
        pass


def place_random_tile()
    pass


if __name__ == "__main__":
    init_pygame()
    main()
