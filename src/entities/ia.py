import random


class Ia:
    def __init__(self, identifier, color, disc, thinking_text):
        self._thinking_text = thinking_text
        self._disc = disc
        self._identifier = identifier
        self._color = color
        self._score = 0
        self._move = 0

    @property
    def move(self):
        return self._move

    @property
    def thinking_text(self):
        return self._thinking_text

    @property
    def disc(self):
        return self._disc

    @property
    def identifier(self):
        return self._identifier

    @move.setter
    def move(self, value):
        if -1 < value < 8:
            self._move = value
        else:
            raise ValueError("Move cannot be above 7 or under 0!")

    def do_random_move(self, grid, screen):
        # Verify move possibility
        random_col_value = random.randint(0, len(grid.matrix[0]))
        grid.add_disc(random_col_value, self, screen)

    def think(self, screen, pygame,grid):
        screen.blit(self.thinking_text, (715 if self.identifier == 1 else 35, 220))
        pygame.time.wait(2000)
        '''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
        '''