import random
import sys
import pygame
from src.entities.grid import Grid
from src.entities.ia import Ia
from src.entities.sprite import Sprite
from src.game.engine import Engine

SCREEN_GRID_ROW_X = [147, 223, 298, 372, 445, 518, 592]
SCREEN_GRID_ROW_Y = [61, 134, 205, 276, 348, 420]

# Pygame init
engine = Engine(2, random.randint(1, 2))  # random.randint(1, 2) to know if player one or player two plays first

pygame.init()
clock = pygame.time.Clock()

# Init screen
screen = pygame.display.set_mode((800, 600))

# Set screen name
pygame.display.set_caption("Connect Four")

# Init background
bg = Sprite('img/bg.png', [0, 0])
screen.fill([255, 255, 255])
screen.blit(bg.image, bg.rect)

# Pygame text init
pygame.font.init()
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 12)

# To create text block containing `Thinking`
yellow_player_thinking_text = font_renderer.render("Thinking...", 1, (255, 87, 87))
red_player_thinking_text = font_renderer.render("Thinking...", 1, (255, 222, 89))

# Init grid
grid = Grid(SCREEN_GRID_ROW_X, SCREEN_GRID_ROW_Y)

ia_one = Ia(1, "yellow", Sprite('img/yellow_disc.png', [0, 0]), yellow_player_thinking_text)
ia_two = Ia(2, "red", Sprite('img/red_disc.png', [0, 0]), red_player_thinking_text)

while True:
    clock.tick(50)

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Refresh the screen
    engine.refresh(bg, grid, screen, ia_one, ia_two)

    '''
    # Verify grid status
    if engine.player_won(grid) == (1 or 2):
        engine.display_victory
    '''

    # Player one actions
    if engine.turn == 1:
        print("Player ONE turn !")
        ia_one.think(screen, pygame,grid)
        ia_one.do_random_move(grid, screen)
    # Player two actions
    else:
        print("Player TWO turn !")
        ia_two.think(screen, pygame,grid)
        ia_two.do_random_move(grid, screen)

    print(grid.matrix)

    engine.turn = 1 if engine.turn == 2 else 2
    engine.turn_number += 1

    # Update the screen
    pygame.display.flip()
