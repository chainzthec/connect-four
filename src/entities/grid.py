import numpy as np


class Grid:
    def __init__(self, screen_row_x, screen_row_y, width=7, height=6):
        self._screen_row_x = screen_row_x
        self._screen_row_y = screen_row_y
        self._screen_matrix = [[[i, j] for i in screen_row_x] for j in screen_row_y]
        self._width = width
        self._height = height
        self._matrix = np.zeros((height, width), dtype=int)

    @property
    def screen_matrix(self):
        return self._screen_matrix

    @property
    def screen_row_x(self):
        return self._screen_row_x

    @property
    def screen_row_y(self):
        return self._screen_row_y

    @property
    def matrix(self):
        return self._matrix

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        if value < 7:
            raise ValueError("Width of the board can't be under 7 units.")
        elif value > 20:
            raise ValueError("Width of the board can't be above 20 units.")
        self._width = value
        self._height = value - 1

    @height.setter
    def height(self, value):
        if value < 6:
            raise ValueError("Width of the board can't be under 7 units.")
        elif value > 19:
            raise ValueError("Width of the board can't be above 19 units.")
        self._width = value
        self._height = value

    def add_disc(self, value, player, screen):
        x = self.height - 1
        new_val = value - 1
        while self.matrix[x][new_val] != 0:
            x = x - 1
        self.matrix[x][new_val] = player.identifier
        screen.blit(player.disc.image, (self.screen_matrix[x][new_val][0], self.screen_matrix[x][new_val][1]))

    def possible_choice(self):
        #TODO finish this method
        print("FINISH IT")

