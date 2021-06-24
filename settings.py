# Author: Colin Francis
# Date: 5/29/2021
# Description: This file contains any game settings / constant values used in Kuba.

# dimensions:
GAME_SCREEN = (750, 825)  # (WIDTH, HEIGHT)
GAME_BOARD = (25, 100, 700, 700)

# colors:
SCREEN_COLOR = (0, 0, 255)
BLACK = (0, 0, 0)
GREY = (190, 190, 190)
LIGHT_GREY = (230, 230, 230)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# marble positioning / size
MARBLE_RADIUS = 40

# TODO: Is there a better way to do this?
MARBLE_POSITIONS = [[],
                    [],
                    [],
                    [],
                    [],
                    [],
                    []]
x_coord, y_coord = (GAME_BOARD[0] + 50, GAME_BOARD[1] + 50)
for row_index, row in enumerate(MARBLE_POSITIONS):
    for column in range(7):
        MARBLE_POSITIONS[row_index].append((x_coord, y_coord))
        x_coord += 100
    x_coord = GAME_BOARD[0] + 50
    y_coord += 100

BOARD_POSITIONS = [[],
                   [],
                   [],
                   [],
                   [],
                   [],
                   []]
x_coord, y_coord = (GAME_BOARD[0], GAME_BOARD[1])
for row_index, row in enumerate(BOARD_POSITIONS):
    for column in range(7):
        BOARD_POSITIONS[row_index].append((x_coord, y_coord))
        x_coord += 100
    x_coord = GAME_BOARD[0]
    y_coord += 100
