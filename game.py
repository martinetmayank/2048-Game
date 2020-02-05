import pygame
import sys
import time

# Imports from another module
from pygame.locals import *
from random import random

# Imports form another file
from colors import *


def main(default=False):

    if not default:
        place_random_tile()
    print_matrix()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if check_if_can_go() == True:
                if event.type == KEYDOWN:
                    if is_arrow(event.key):
                        rotations = get_rotations(event.key)
                        add_to_undo()
                        for i in range(0, rotations):
                            rotate_matrix_clockwise()

                        if can_move():
                            move_tiles()
                            merge_tiles()
                            place_random_tile()

                        for j in range(0, (4 - rotations) % 4):
                            rotate_matrix_clockwise()

                        print_matrix()
            else:
                print_game_over()

            if event.type == KEYDOWN:
                global BOARD_SIZE

                if event.key == pygame.K_r:
                    reset()

                if 50 < event.key and 56 > event.key:
                    BOARD_SIZE = event.key - 48
                    reset()

        pygame.display.update()


def can_move():
    for i in range(0, BOARD_SIZE):
        for j in range(1, BOARD_SIZE):
            if tile_matrix[i][j-1] == 0 and tile_matrix[i][j] > 0:
                return True
            elif (tile_matrix[i][j-1] == tile_matrix[i][j]) and tile_matrix[i][j-1] != 0:
                return True
    return False


def move_tiles():
    for i in range(0, BOARD_SIZE):
        for j in range(0, BOARD_SIZE - 1):

            while tile_matrix[i][j] == 0 and sum(tile_matrix[i][j:]) > 0:
                for k in range(j, BOARD_SIZE - 1):
                    tile_matrix[i][k] = tile_matrix[i][k + 1]
                tile_matrix[i][BOARD_SIZE - 1] = 0


def merge_tiles():
    global TOTAL_POINTS

    for i in range(0, BOARD_SIZE):
        for j in range(0, BOARD_SIZE-1):
            if tile_matrix[i][j] == tile_matrix[i][j + 1] and tile_matrix[i][j] != 0:
                tile_matrix[i][j] = tile_matrix[i][j]*2
                tile_matrix[i][j + 1] = 0
                TOTAL_POINTS += tile_matrix[i][j]

                move_tiles()


def place_random_tile():
    # c = 0
    # for i in range(0, BOARD_SIZE):
    #     for j in range(0, BOARD_SIZE):
    #         if tile_matrix[i][j] == 0:
    #             c += 1

    key = floor_function(random() * BOARD_SIZE * BOARD_SIZE)
    print("click")

    while tile_matrix[floor_function(key / BOARD_SIZE)][key % BOARD_SIZE] != 0:
        key = floor_function(random() * BOARD_SIZE * BOARD_SIZE)

    tile_matrix[floor_function(key / BOARD_SIZE)][key % BOARD_SIZE] = 2


def floor_function(number):
    return int(number - (number % 1))


def print_matrix():
    surface.fill(black)
    global BOARD_SIZE
    global TOTAL_POINTS

    for i in range(0, BOARD_SIZE):
        for j in range(0, BOARD_SIZE):
            pygame.draw.rect(
                surface,
                getColor(
                    tile_matrix[i][j]),
                (
                    i * (400 / BOARD_SIZE),
                    j * (400 / BOARD_SIZE) + 100,
                    400 / BOARD_SIZE,
                    400 / BOARD_SIZE)
            )

            label = default_font.render(
                str(tile_matrix[i][j]),
                1,
                (255, 255, 255)
            )

            label2 = score_font.render(
                "YourScore: " + str(TOTAL_POINTS),
                1,
                (255, 255, 255)
            )

            surface.blit(label,
                         (i * (400 / BOARD_SIZE) +
                          30, j * (400 / BOARD_SIZE) + 130)
                         )

            surface.blit(label2, (10, 20))


def check_if_can_go():
    for i in range(0, BOARD_SIZE ** 2):
        if tile_matrix[floor_function(i / BOARD_SIZE)][i % BOARD_SIZE] == 0:
            return True

    for i in range(0, BOARD_SIZE):
        for j in range(0, BOARD_SIZE - 1):

            if tile_matrix[i][j] == tile_matrix[i][j + 1]:
                return True

            elif tile_matrix[j][i] == tile_matrix[j + 1][i]:
                return True

    return False


def convert_to_linear_matrix():

    matrix = []
    for i in range(0, BOARD_SIZE ** 2):
        matrix.append(
            tile_matrix[floor_function(
                i / BOARD_SIZE)][i % BOARD_SIZE]
        )

    matrix.append(TOTAL_POINTS)
    return matrix


def add_to_undo():
    reset_matrix.append(convert_to_linear_matrix())


def rotate_matrix_clockwise():
    for i in range(0, int(BOARD_SIZE / 2)):
        for j in range(i, BOARD_SIZE - i - 1):

            temp1 = tile_matrix[i][j]
            temp2 = tile_matrix[BOARD_SIZE - 1 - j][i]
            temp3 = tile_matrix[BOARD_SIZE - 1 - i][BOARD_SIZE - 1 - j]
            temp4 = tile_matrix[j][BOARD_SIZE - 1 - i]

            tile_matrix[BOARD_SIZE - 1 - j][i] = temp1
            tile_matrix[BOARD_SIZE - 1 - i][BOARD_SIZE - 1 - j] = temp2
            tile_matrix[j][BOARD_SIZE - 1 - i] = temp3
            tile_matrix[i][j] = temp4


def print_game_over():
    global TOTAL_POINTS

    surface.fill(black)

    gameover_label = score_font.render(
        "GameOver!",
        1,
        (255, 255, 255)
    )

    score_label = score_font.render(
        "Score : " + str(TOTAL_POINTS),
        1,
        (255, 255, 255)
    )

    restart_game = default_font.render(
        "press 'R' to play again!! ",
        1,
        (255, 255, 255)
    )

    surface.blit(gameover_label, (50, 100))
    surface.blit(score_label, (50, 200))
    surface.blit(restart_game, (50, 300))


def reset():
    global TOTAL_POINTS
    global tile_matrix

    TOTAL_POINTS = 0
    surface.fill(black)
    tile_matrix = [
        [
            0 for i in range(0, BOARD_SIZE)
        ]
        for j in range(0, BOARD_SIZE)

    ]
    main()


def is_arrow(key):
    """
    This help you find the which arrow is clicked by the user
    """
    return (key == pygame.K_UP or key == pygame.K_DOWN or key == pygame.K_LEFT or key == pygame.K_RIGHT)


def get_rotations(key):
    if key == pygame.K_UP:
        return 0

    elif key == pygame.K_DOWN:
        return 2

    elif key == pygame.K_LEFT:
        return 1

    elif key == pygame.K_RIGHT:
        return 3


if __name__ == "__main__":
    BOARD_SIZE = 4
    TOTAL_POINTS = 0
    DEFAULT_SCORE = 2

    pygame.init()

    surface = pygame.display.set_mode((400, 500), 0, 32)
    pygame.display.set_caption("game")

    default_font = pygame.font.SysFont("monospace", 40)
    score_font = pygame.font.SysFont("monospace", 30)

    tile_matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    reset_matrix = []

    main()