# Author: Colin Francis
# Date: 6/3/2021

import pygame
from settings import *
import copy


class KubaGame(object):
    """"""
    def __init__(self) -> None:
        """Initializes pygame modules and creates a KubaGame object with board, running, and selected attributes. The
        board attribute initializes the game Board. The running attribute is True while the game is running and False
        when the user exits. The selected attribute is set to True if the user selects a cell on the game board,
        otherwise this is False."""
        pygame.init()
        pygame.mixer.init()
        self._board = Board()
        self._running = True
        self._selected = False
        self._turn = None
        self._winner = None
        self._player_1 = Player(WHITE, "White")
        self._player_2 = Player(BLACK, "Black")

    def play(self) -> None:
        """Start playing Kuba."""
        while self._running:
            self._board.update_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (255 <= pygame.mouse.get_pos()[0] <= 355 and 65 <= pygame.mouse.get_pos()[1] <= 95) and \
                            self._mode_selected is False:
                        self._mode_selected = True
                    elif (400 <= pygame.mouse.get_pos()[0] <= 500 and 65 <= pygame.mouse.get_pos()[1] <= 95) and \
                            self._mode_selected is False:
                        self._mode_selected = True
                    # row 1
                    if (BOARD_POSITIONS[0][0][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][1][0]) and \
                            (BOARD_POSITIONS[0][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[1][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][0][0])
                        self._board.set_top(BOARD_POSITIONS[0][0][1])
                    elif (BOARD_POSITIONS[0][1][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][2][0]) and \
                            (BOARD_POSITIONS[0][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[1][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][1][0])
                        self._board.set_top(BOARD_POSITIONS[0][0][1])
                    elif (BOARD_POSITIONS[0][2][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][3][0]) and \
                            (BOARD_POSITIONS[0][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[1][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][2][0])
                        self._board.set_top(BOARD_POSITIONS[0][0][1])
                    elif (BOARD_POSITIONS[0][3][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][4][0]) and \
                            (BOARD_POSITIONS[0][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[1][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][3][0])
                        self._board.set_top(BOARD_POSITIONS[0][0][1])
                    elif (BOARD_POSITIONS[0][4][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][5][0]) and \
                            (BOARD_POSITIONS[0][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[1][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][4][0])
                        self._board.set_top(BOARD_POSITIONS[0][0][1])
                    elif (BOARD_POSITIONS[0][5][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) and \
                            (BOARD_POSITIONS[0][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[1][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][5][0])
                        self._board.set_top(BOARD_POSITIONS[0][0][1])
                    elif (BOARD_POSITIONS[0][6][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0] + 100) and \
                            (BOARD_POSITIONS[0][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[1][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][6][0])
                        self._board.set_top(BOARD_POSITIONS[0][0][1])
                    # row 2
                    elif (BOARD_POSITIONS[0][0][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][1][0]) and \
                         (BOARD_POSITIONS[1][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[2][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][0][0])
                        self._board.set_top(BOARD_POSITIONS[1][0][1])
                    elif (BOARD_POSITIONS[0][1][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][2][0]) and \
                         (BOARD_POSITIONS[1][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[2][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][1][0])
                        self._board.set_top(BOARD_POSITIONS[1][0][1])
                    elif (BOARD_POSITIONS[0][2][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][3][0]) and \
                         (BOARD_POSITIONS[1][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[2][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][2][0])
                        self._board.set_top(BOARD_POSITIONS[1][0][1])
                    elif (BOARD_POSITIONS[0][3][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][4][0]) and \
                         (BOARD_POSITIONS[1][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[2][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][3][0])
                        self._board.set_top(BOARD_POSITIONS[1][0][1])
                    elif (BOARD_POSITIONS[0][4][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][5][0]) and \
                         (BOARD_POSITIONS[1][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[2][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][4][0])
                        self._board.set_top(BOARD_POSITIONS[1][0][1])
                    elif (BOARD_POSITIONS[0][5][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) and \
                         (BOARD_POSITIONS[1][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[2][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][5][0])
                        self._board.set_top(BOARD_POSITIONS[1][0][1])
                    elif (BOARD_POSITIONS[0][6][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) + 100 and \
                         (BOARD_POSITIONS[1][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[2][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][6][0])
                        self._board.set_top(BOARD_POSITIONS[1][0][1])
                    # row 3
                    elif (BOARD_POSITIONS[0][0][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][1][0]) and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][0][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    elif (BOARD_POSITIONS[0][1][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][2][0]) and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][1][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    elif (BOARD_POSITIONS[0][2][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][3][0]) and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][2][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    elif (BOARD_POSITIONS[0][3][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][4][0]) and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][3][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    elif (BOARD_POSITIONS[0][4][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][5][0]) and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][4][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    elif (BOARD_POSITIONS[0][5][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][5][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    elif (BOARD_POSITIONS[0][6][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) + 100 and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][6][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    # row 4
                    elif (BOARD_POSITIONS[0][0][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][1][0]) and \
                            (BOARD_POSITIONS[3][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[4][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][0][0])
                        self._board.set_top(BOARD_POSITIONS[3][0][1])
                    elif (BOARD_POSITIONS[0][1][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][2][0]) and \
                            (BOARD_POSITIONS[3][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[4][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][1][0])
                        self._board.set_top(BOARD_POSITIONS[3][0][1])
                    elif (BOARD_POSITIONS[0][2][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][3][0]) and \
                            (BOARD_POSITIONS[3][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[4][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][2][0])
                        self._board.set_top(BOARD_POSITIONS[3][0][1])
                    elif (BOARD_POSITIONS[0][3][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][4][0]) and \
                            (BOARD_POSITIONS[3][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[4][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][3][0])
                        self._board.set_top(BOARD_POSITIONS[3][0][1])
                    elif (BOARD_POSITIONS[0][4][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][5][0]) and \
                            (BOARD_POSITIONS[3][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[4][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][4][0])
                        self._board.set_top(BOARD_POSITIONS[3][0][1])
                    elif (BOARD_POSITIONS[0][5][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) and \
                            (BOARD_POSITIONS[3][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[4][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][5][0])
                        self._board.set_top(BOARD_POSITIONS[3][0][1])
                    elif (BOARD_POSITIONS[0][6][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) + 100 and \
                            (BOARD_POSITIONS[3][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[4][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][6][0])
                        self._board.set_top(BOARD_POSITIONS[3][0][1])
                    # row 3
                    elif (BOARD_POSITIONS[0][0][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][1][0]) and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][0][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    elif (BOARD_POSITIONS[0][1][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][2][0]) and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][1][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    elif (BOARD_POSITIONS[0][2][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][3][0]) and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][2][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    elif (BOARD_POSITIONS[0][3][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][4][0]) and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][3][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    elif (BOARD_POSITIONS[0][4][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][5][0]) and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][4][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    elif (BOARD_POSITIONS[0][5][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][5][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    elif (BOARD_POSITIONS[0][6][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) + 100 and \
                            (BOARD_POSITIONS[2][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[3][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][6][0])
                        self._board.set_top(BOARD_POSITIONS[2][0][1])
                    # row 5
                    elif (BOARD_POSITIONS[0][0][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][1][0]) and \
                            (BOARD_POSITIONS[4][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[5][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][0][0])
                        self._board.set_top(BOARD_POSITIONS[4][0][1])
                    elif (BOARD_POSITIONS[0][1][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][2][0]) and \
                            (BOARD_POSITIONS[4][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[5][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][1][0])
                        self._board.set_top(BOARD_POSITIONS[4][0][1])
                    elif (BOARD_POSITIONS[0][2][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][3][0]) and \
                            (BOARD_POSITIONS[4][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[5][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][2][0])
                        self._board.set_top(BOARD_POSITIONS[4][0][1])
                    elif (BOARD_POSITIONS[0][3][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][4][0]) and \
                            (BOARD_POSITIONS[4][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[5][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][3][0])
                        self._board.set_top(BOARD_POSITIONS[4][0][1])
                    elif (BOARD_POSITIONS[0][4][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][5][0]) and \
                            (BOARD_POSITIONS[4][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[5][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][4][0])
                        self._board.set_top(BOARD_POSITIONS[4][0][1])
                    elif (BOARD_POSITIONS[0][5][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) and \
                            (BOARD_POSITIONS[4][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[5][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][5][0])
                        self._board.set_top(BOARD_POSITIONS[4][0][1])
                    elif (BOARD_POSITIONS[0][6][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) + 100 and \
                            (BOARD_POSITIONS[4][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[5][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][6][0])
                        self._board.set_top(BOARD_POSITIONS[4][0][1])
                    # row 6
                    elif (BOARD_POSITIONS[0][0][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][1][0]) and \
                            (BOARD_POSITIONS[5][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][0][0])
                        self._board.set_top(BOARD_POSITIONS[5][0][1])
                    elif (BOARD_POSITIONS[0][1][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][2][0]) and \
                            (BOARD_POSITIONS[5][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][1][0])
                        self._board.set_top(BOARD_POSITIONS[5][0][1])
                    elif (BOARD_POSITIONS[0][2][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][3][0]) and \
                            (BOARD_POSITIONS[5][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][2][0])
                        self._board.set_top(BOARD_POSITIONS[5][0][1])
                    elif (BOARD_POSITIONS[0][3][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][4][0]) and \
                            (BOARD_POSITIONS[5][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][3][0])
                        self._board.set_top(BOARD_POSITIONS[5][0][1])
                    elif (BOARD_POSITIONS[0][4][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][5][0]) and \
                            (BOARD_POSITIONS[5][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][4][0])
                        self._board.set_top(BOARD_POSITIONS[5][0][1])
                    elif (BOARD_POSITIONS[0][5][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) and \
                            (BOARD_POSITIONS[5][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][5][0])
                        self._board.set_top(BOARD_POSITIONS[5][0][1])
                    elif (BOARD_POSITIONS[0][6][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) + 100 and \
                            (BOARD_POSITIONS[5][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1]):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][6][0])
                        self._board.set_top(BOARD_POSITIONS[5][0][1])
                    # row 7
                    elif (BOARD_POSITIONS[0][0][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][1][0]) and \
                            (BOARD_POSITIONS[6][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1] + 100):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][0][0])
                        self._board.set_top(BOARD_POSITIONS[6][0][1])
                    elif (BOARD_POSITIONS[0][1][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][2][0]) and \
                            (BOARD_POSITIONS[6][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1]) + 100:
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][1][0])
                        self._board.set_top(BOARD_POSITIONS[6][0][1])
                    elif (BOARD_POSITIONS[0][2][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][3][0]) and \
                            (BOARD_POSITIONS[6][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1] + 100):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][2][0])
                        self._board.set_top(BOARD_POSITIONS[6][0][1])
                    elif (BOARD_POSITIONS[0][3][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][4][0]) and \
                            (BOARD_POSITIONS[6][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1] + 100):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][3][0])
                        self._board.set_top(BOARD_POSITIONS[6][0][1])
                    elif (BOARD_POSITIONS[0][4][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][5][0]) and \
                            (BOARD_POSITIONS[6][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1] + 100):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][4][0])
                        self._board.set_top(BOARD_POSITIONS[6][0][1])
                    elif (BOARD_POSITIONS[0][5][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) and \
                            (BOARD_POSITIONS[6][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1] + 100):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][5][0])
                        self._board.set_top(BOARD_POSITIONS[6][0][1])
                    elif (BOARD_POSITIONS[0][6][0] <= pygame.mouse.get_pos()[0] < BOARD_POSITIONS[0][6][0]) + 100 and \
                            (BOARD_POSITIONS[6][0][1] <= pygame.mouse.get_pos()[1] < BOARD_POSITIONS[6][0][1] + 100):
                        self._selected = True
                        self._board.set_cell_selected(True)
                        self._board.set_left(BOARD_POSITIONS[0][6][0])
                        self._board.set_top(BOARD_POSITIONS[6][0][1])
                    else:
                        self._board.set_cell_selected(False)

                if self._selected is True:
                    if self._marble_in_cell() and self._board.get_marble().get_color() != RED:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                self._make_move('L')
                            elif event.key == pygame.K_RIGHT:
                                self._make_move('R')
                            elif event.key == pygame.K_UP:
                                self._make_move('F')
                            elif event.key == pygame.K_DOWN:
                                self._make_move('B')

            self._board.get_screen().blit(self._display_white_captures(), (25, 60))
            self._board.get_screen().blit(self._display_black_captures(), (510, 60))

            if self._turn is not None and self._winner is None:
                self._board.get_screen().blit(self._display_turn(), (295, 10))

            if self._winner is not None:
                self._board.get_screen().blit(self._display_winner(), (295, 10))

            pygame.display.update()

    def set_turn(self, player: object) -> None:
        """Sets turn to the Player whose turn it is."""
        self._turn = player

    def _make_move(self, direction: str) -> None:
        """Makes a move on the Board by shifting marble positions based on the selected Marble and the specified push
        direction."""
        if self._board.get_marble().get_color() == self._player_1.get_color():
            player = self._player_1
            other_player = self._player_2
        else:
            player = self._player_2
            other_player = self._player_1

        if (self._turn is None or self._turn.get_color() == self._board.get_marble().get_color()) and \
                self._winner is None:
            if self._is_valid(direction):
                if self._is_valid_push(direction, self._board.get_marble().get_color()):
                    # get marble counts before move:
                    white_count_before, black_count_before, red_count_before = self._marble_count()

                    # make move:
                    self._push_marbles(direction)

                    # get marble counts after move:
                    white_count_after, black_count_after, red_count_after = self._marble_count()

                    # make sure move isn't undoing a previous move leading to exact same board state:
                    if player.get_previous_configuration() is not None and self._undone(player):
                        self._board.restore_previous_configuration()
                    else:
                        self.play_slide_sound()
                        self._board.set_cell_selected(False)

                        # check for red marble captures and set winner if 7 red marbles have been captured:
                        if red_count_after < red_count_before:
                            player.capture()
                            if player.get_captures() == 7:
                                self._winner = player.get_color_text()

                        # check if all of one player's marbles have been removed and set winner accordingly:
                        if white_count_after == 0:
                            self._winner = self._player_2.get_color_text()
                        elif black_count_after == 0:
                            self._winner = self._player_1.get_color_text()

                        self.set_turn(other_player)
                        self._board.set_previous_configuration(player)
                        self._board.set_previous_configuration()

    def _undone(self, player) -> bool:
        """Returns True if the move being made is going to undo the other Player's previous move and return the Board
        back to the exact same state."""
        for marble_index, marble in enumerate(self._board.get_marbles_on_board()):
            if marble.get_center() != player.get_previous_configuration()[marble_index].get_center():
                return False
        else:
            return True

    def _is_valid(self, direction: str) -> bool:
        """Returns True if the attempted move is valid, otherwise returns False. In order for an attempted move to
        be valid, there must be an empty space or edge on the side the push is occurring from."""
        if direction == 'L':
            if self._board.get_selected_left() + 100 >= 725 or \
                    not self._marble_in_cell(left=self._board.get_selected_left() + 100,
                                             top=self._board.get_selected_top()):
                return True
            else:
                return False
        elif direction == 'R':
            if self._board.get_selected_left() - 100 < 25 or \
                    not self._marble_in_cell(left=self._board.get_selected_left() - 100,
                                             top=self._board.get_selected_top()):
                return True
            else:
                return False
        elif direction == 'F':
            if self._board.get_selected_top() + 100 > 800 or \
                    not self._marble_in_cell(left=self._board.get_selected_left(),
                                             top=self._board.get_selected_top() + 100):
                return True
            else:
                return False
        else:  # direction == 'B'
            if self._board.get_selected_top() - 100 < 100 or \
                    not self._marble_in_cell(left=self._board.get_selected_left(),
                                             top=self._board.get_selected_top() - 100):
                return True
            else:
                return False

    def _is_valid_push(self, direction: str, color: tuple, left=None, top=None, curr_marble=None) -> bool:
        """Recursively searches for the last marble in the chain of marbles being pushed to confirm that the Player is
        not pushing their own Marble of the Board."""
        if left is None:
            left = self._board.get_selected_left()
            top = self._board.get_selected_top()
            curr_marble = self._board.get_marble()

        if direction == 'R':
            if not self._marble_in_cell(left=left + 100, top=top):
                if left + 100 >= 725 and curr_marble.get_color() == color:
                    return False
                else:
                    return True
            else:
                next_marble = self._board.get_marble(left=left + 100, top=top)
                return self._is_valid_push(direction, color, left=left + 100, top=top, curr_marble=next_marble)
        elif direction == 'L':
            if not self._marble_in_cell(left=left - 100, top=top):
                if left - 100 < 25 and curr_marble.get_color() == color:
                    return False
                else:
                    return True
            else:
                next_marble = self._board.get_marble(left=left - 100, top=top)
                return self._is_valid_push(direction, color, left=left - 100, top=top, curr_marble=next_marble)
        elif direction == 'F':
            if not self._marble_in_cell(left=left, top=top - 100):
                if top - 100 < 100 and curr_marble.get_color() == color:
                    return False
                else:
                    return True
            else:
                next_marble = self._board.get_marble(left=left, top=top - 100)
                return self._is_valid_push(direction, color, left=left, top=top - 100, curr_marble=next_marble)
        else:
            if not self._marble_in_cell(left=left, top=top + 100):
                if top + 100 >= 800 and curr_marble.get_color() == color:
                    return False
                else:
                    return True
            else:
                next_marble = self._board.get_marble(left=left, top=top + 100)
                return self._is_valid_push(direction, color, left=left, top=top + 100, curr_marble=next_marble)

    def _marble_in_cell(self, left=None, top=None) -> bool:
        """Returns true if the selected cell has a marble in it, otherwise False is returned. By default, this method
        will use the current selected cell to define left and top. Default arguments `left` and `top` can be changed
        to specify a different left or top position."""
        if left is None:
            left = self._board.get_selected_left()
            top = self._board.get_selected_top()
        for marble in self._board.get_marbles_on_board():
            if (left <= marble.get_center()[0] < left + 100) and (top <= marble.get_center()[1] < top + 100):
                return True
        return False

    def _push_marbles(self, direction: str, left=None, top=None, curr_marble=None) -> None:
        """Recursively moves each Marble in the chain of Marbles being pushed one square over in the direction of the
        push. If a valid Marble is knocked off the Board, it will be removed from play."""
        if left is None:
            left = self._board.get_selected_left()
            top = self._board.get_selected_top()
            curr_marble = self._board.get_marble()

        if direction == 'R':
            if not self._marble_in_cell(left=left + 100, top=top):
                curr_marble.push_right()
                if curr_marble.get_center()[0] > 725:
                    self.play_capture_sound()
                    del self._board.get_marbles_on_board()[self._board.get_marbles_on_board().index(curr_marble)]
                return
            else:
                next_marble = self._board.get_marble(left=left + 100, top=top)
                curr_marble.push_right()
                return self._push_marbles(direction, left=left + 100, top=top, curr_marble=next_marble)
        elif direction == 'L':
            if not self._marble_in_cell(left=left - 100, top=top):
                curr_marble.push_left()
                if curr_marble.get_center()[0] < 25:
                    self.play_capture_sound()
                    del self._board.get_marbles_on_board()[self._board.get_marbles_on_board().index(curr_marble)]
                return
            else:
                next_marble = self._board.get_marble(left=left - 100, top=top)
                curr_marble.push_left()
                return self._push_marbles(direction, left=left - 100, top=top, curr_marble=next_marble)
        elif direction == 'F':
            if not self._marble_in_cell(left=left, top=top - 100):
                curr_marble.push_up()
                if curr_marble.get_center()[1] < 100:
                    self.play_capture_sound()
                    del self._board.get_marbles_on_board()[self._board.get_marbles_on_board().index(curr_marble)]
                return
            else:
                next_marble = self._board.get_marble(left=left, top=top - 100)
                curr_marble.push_up()
                return self._push_marbles(direction, left=left, top=top - 100, curr_marble=next_marble)
        else:
            if not self._marble_in_cell(left=left, top=top + 100):
                curr_marble.push_down()
                if curr_marble.get_center()[1] > 800:
                    self.play_capture_sound()
                    del self._board.get_marbles_on_board()[self._board.get_marbles_on_board().index(curr_marble)]
                return
            else:
                next_marble = self._board.get_marble(left=left, top=top + 100)
                curr_marble.push_down()
                return self._push_marbles(direction, left=left, top=top + 100, curr_marble=next_marble)

    def _marble_count(self) -> tuple:
        """Counts the number of white, black, and red Marbles that remain in play and returns a tuple containing the
        counts of the Marbles in that order."""
        white_count = 0
        black_count = 0
        red_count = 0
        for marble in self._board.get_marbles_on_board():
            if marble.get_color() == WHITE:
                white_count += 1
            elif marble.get_color() == BLACK:
                black_count += 1
            else:
                red_count += 1
        return white_count, black_count, red_count

    def _display_white_captures(self):
        """Displays the number of red marbles captured by the Player using the white marbles."""
        font = pygame.font.SysFont("Times New Roman", 30)
        return font.render("White Captures: {}".format(self._player_1.get_captures()), True, WHITE)

    def _display_black_captures(self):
        """Displays the number of red marbles captured by the Player using the Black marbles."""
        font = pygame.font.SysFont("Times New Roman", 30)
        return font.render("Black Captures: {}".format(self._player_2.get_captures()), True, WHITE)

    def _display_turn(self):
        """Displays the color of the Player whose turn it is."""
        font = pygame.font.SysFont("Times New Roman", 30)
        return font.render("{}'s Turn".format(self._turn.get_color_text()), True, WHITE)

    def _display_winner(self):
        """Displays the color of the winning Player"""
        font = pygame.font.SysFont("Times New Roman", 30)
        return font.render("{} Wins!".format(self._winner), True, WHITE)

    @staticmethod
    def play_capture_sound():
        """A sound used when a Marble is knocked off the board."""
        pygame.mixer.Sound('marble_capture.mp3').play()

    @staticmethod
    def play_slide_sound():
        """A sound used when Marbles are pushed on the game Board."""
        pygame.mixer.Sound('marble_slide.mp3').play().set_volume(0.15)


class Board(object):
    """Represents a Board to play the game Kuba on."""
    def __init__(self) -> None:
        """"""
        pygame.display.set_caption("Kuba")
        self._screen = pygame.display.set_mode(GAME_SCREEN)
        self._marbles_on_board = [Marble(WHITE, MARBLE_POSITIONS[0][0]), Marble(WHITE, MARBLE_POSITIONS[0][1]),
                                  Marble(BLACK, MARBLE_POSITIONS[0][5]), Marble(BLACK, MARBLE_POSITIONS[0][6]),
                                  Marble(WHITE, MARBLE_POSITIONS[1][0]), Marble(WHITE, MARBLE_POSITIONS[1][1]),
                                  Marble(BLACK, MARBLE_POSITIONS[1][5]), Marble(BLACK, MARBLE_POSITIONS[1][6]),
                                  Marble(RED, MARBLE_POSITIONS[1][3]), Marble(RED, MARBLE_POSITIONS[2][2]),
                                  Marble(RED, MARBLE_POSITIONS[2][3]), Marble(RED, MARBLE_POSITIONS[2][4]),
                                  Marble(RED, MARBLE_POSITIONS[3][1]), Marble(RED, MARBLE_POSITIONS[3][2]),
                                  Marble(RED, MARBLE_POSITIONS[3][3]), Marble(RED, MARBLE_POSITIONS[3][4]),
                                  Marble(RED, MARBLE_POSITIONS[3][5]), Marble(RED, MARBLE_POSITIONS[4][2]),
                                  Marble(RED, MARBLE_POSITIONS[4][3]), Marble(RED, MARBLE_POSITIONS[4][4]),
                                  Marble(RED, MARBLE_POSITIONS[5][3]), Marble(BLACK, MARBLE_POSITIONS[5][0]),
                                  Marble(BLACK, MARBLE_POSITIONS[5][1]), Marble(WHITE, MARBLE_POSITIONS[5][5]),
                                  Marble(WHITE, MARBLE_POSITIONS[5][6]), Marble(BLACK, MARBLE_POSITIONS[6][0]),
                                  Marble(BLACK, MARBLE_POSITIONS[6][1]), Marble(WHITE, MARBLE_POSITIONS[6][5]),
                                  Marble(WHITE, MARBLE_POSITIONS[6][6])]
        self._previous_configuration = copy.deepcopy(self._marbles_on_board)
        self._selected_top = None
        self._selected_left = None
        self._cell_selected = False

    def get_screen(self):
        """Returns the screen that Kuba is being played on."""
        return self._screen

    def get_selected_top(self) -> float:
        """Returns the top position of the current selected cell."""
        return self._selected_top

    def get_selected_left(self) -> float:
        """Returns the left position of the current selected cell."""
        return self._selected_left

    def get_marbles_on_board(self) -> list:
        """Returns a list of Marble objects that are current on the Board."""
        return self._marbles_on_board

    def get_marble(self, left=None, top=None):
        """Returns the Marble object contained in the currently selected cell. Default arguments 'left' and 'top' can
        be used in order to get a Marble in a different cell than the one currently selected."""
        if left is None:
            left = self._selected_left
            top = self._selected_top
        for marble in self._marbles_on_board:
            if (left <= marble.get_center()[0] < left + 100) and (top <= marble.get_center()[1] < top + 100):
                return marble

    def set_previous_configuration(self, player=None):
        """Sets the previous board configuration prior to the player's most recent move."""
        previous_configuration = []
        if player is None:
            for marble in self._marbles_on_board:
                previous_configuration.append(marble)
            self._previous_configuration = copy.deepcopy(previous_configuration)
        else:
            for marble in self._marbles_on_board:
                previous_configuration.append(marble)
            player.set_previous_configuration(copy.deepcopy(previous_configuration))

    def set_cell_selected(self, state: bool) -> None:
        """Set the _shade_cell attribute to True if a cell is selected and should be shaded. Otherwise, this attribute
        should be set to False."""
        self._cell_selected = state

    def set_top(self, top: float) -> None:
        """Sets the top position corresponding to the current selected cell."""
        self._selected_top = top

    def set_left(self, left: float) -> None:
        """Sets the left position corresponding to the current selected cell."""
        self._selected_left = left

    def update_board(self):
        """Responsible for updating thew board."""
        self._draw_board()
        if self._cell_selected is True:
            self._shade_cell(self._selected_left + 4, self._selected_top + 4)
        self._draw_grid()
        self._place_marbles()

    def restore_previous_configuration(self):
        """Restores the previous configuration of the board."""
        self._marbles_on_board = copy.deepcopy(self._previous_configuration)

    def _draw_board(self):
        """Draws the rectangle that will act as the game Board."""
        self._screen.fill(SCREEN_COLOR)
        pygame.draw.rect(self._screen, GREY, pygame.Rect(25, 100, 700, 700))
        pygame.draw.rect(self._screen, BLACK, pygame.Rect(25, 100, 700, 700), width=5)

    def _draw_grid(self):
        """Draws the grid lines on the game Board that the Marbles will moved into."""
        x_pos, y_pos = 25 + 100, 100 + 100
        for loop_count in range(7):
            pygame.draw.line(self._screen, BLACK, (x_pos, 100), (x_pos, 800), width=5)
            pygame.draw.line(self._screen, BLACK, (25, y_pos), (725, y_pos), width=5)
            x_pos += 100
            y_pos += 100

    def _shade_cell(self, left, top):
        """Shades a cell that has been selected."""
        pygame.draw.rect(self._screen, LIGHT_GREY, pygame.Rect(left, top, 95, 95))

    def _place_marbles(self):
        """Places Marble objects on the game board."""
        for marble in self._marbles_on_board:
            pygame.draw.circle(self._screen, marble.get_color(), marble.get_center(), MARBLE_RADIUS)


class Marble(object):
    """Represents a Marble used to play Kuba with."""
    def __init__(self, color: tuple, center: tuple) -> None:
        """Creates a Marble object with color and center attributes. The center represents the position on the Board
        where the center of the Marble will be placed."""
        self._color = color
        self._center = center

    def get_center(self) -> tuple:
        """Returns the coordinates where the center of the Marble currently is on the Board. The first coordinate is the
        x-coordinate, the second coordinate is the y-coordinate."""
        return self._center

    def get_color(self) -> tuple:
        """Returns the RGB tuple representing the Marble's color."""
        return self._color

    def set_center(self, center: tuple) -> None:
        """Repositions the center of the Marble on the Board."""
        self._center = center

    def push_right(self) -> None:
        """Pushes a Marble one square in the right-hand direction."""
        self._center = (self._center[0] + 100, self._center[1])

    def push_left(self) -> None:
        """Pushes a Marble one square in the left-hand direction."""
        self._center = (self._center[0] - 100, self._center[1])

    def push_up(self) -> None:
        """Pushes a Marble one square in the upwards direction."""
        self._center = (self._center[0], self._center[1] - 100)

    def push_down(self) -> None:
        """Pushes a Marble one square in the downwards direction."""
        self._center = (self._center[0], self._center[1] + 100)


class Player(object):
    def __init__(self, color: tuple, color_text: str) -> None:
        self._color = color
        self._color_text = color_text
        self._captures = 0
        self._previous_configuration = None

    def get_color(self):
        """Returns the Marble color that the Player is using."""
        return self._color

    def get_color_text(self):
        """Returns the string with the name of the Marble color that the Player is using."""
        return self._color_text

    def get_captures(self):
        """Returns the number of red marbles captures by the Player."""
        return self._captures

    def get_previous_configuration(self):
        return self._previous_configuration

    def set_previous_configuration(self, previous_configuration):
        self._previous_configuration = previous_configuration

    def capture(self):
        """Increments the number of red marbles captured by the Player by 1."""
        self._captures += 1


if __name__ == "__main__":
    kuba = KubaGame()
    kuba.play()
