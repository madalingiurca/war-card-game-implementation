import pygame
import sys

from GameEngine import Deck, GameState, draw_starting_screen
from settings import *

if __name__ == '__main__':

    current_game_state = GameState.START

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Cards War')
    clock = pygame.time.Clock()

    pygame.display.set_caption("Let it be WAR")

    deck = Deck()
    deck.shuffleDeck()
    screen.fill(BACKGROUND_COLOR)

    while True:

        if current_game_state == GameState.START:
            draw_starting_screen(screen)

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # drawing logic
        pygame.display.update()
        clock.tick(60)
