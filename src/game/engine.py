class Engine:
    def __init__(self, number_of_players, turn, turn_number=0):
        self._number_of_players = number_of_players
        self._turn = turn
        self._turn_number = turn_number

    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
            self.turn_number += 1
        elif self.turn == 2:
            self.turn = 1
            self.turn_number += 1
        else:
            raise ValueError("Player turn unidentified")

    @property
    def number_of_players(self):
        return self._number_of_players

    @property
    def turn(self):
        return self._turn

    @property
    def turn_number(self):
        return self._turn_number

    @turn.setter
    def turn(self, value):
        self._turn = value

    @turn_number.setter
    def turn_number(self, value):
        self._turn_number = value

    def refresh(self, bg, grid, screen, yellow_player, red_player):
        screen.fill([255, 255, 255])
        screen.blit(bg.image, bg.rect)
        for i in range(len(grid.matrix)):
            for j in range(len(grid.matrix[i])):
                if grid.matrix[i][j] == 1:
                    screen.blit(yellow_player.disc.image, (grid.screen_matrix[i][j][0], grid.screen_matrix[i][j][1]))
                elif grid.matrix[i][j] == 2:
                    screen.blit(red_player.disc.image, (grid.screen_matrix[i][j][0], grid.screen_matrix[i][j][1]))
