import sys

import pygame
from pygame.sprite import Group

from core.game_engine import Deck, GameState, update_game_start_text
from core.game_utils import get_starting_screen_card_backs_centered
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

    starting_UI_cards = Group(get_starting_screen_card_backs_centered(screen))

    while True:
        screen.fill(BACKGROUND_COLOR)
        if current_game_state == GameState.START:
            update_game_start_text(screen)
            starting_UI_cards.update()
            starting_UI_cards.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)
