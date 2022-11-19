import sys

import pygame
from pygame.sprite import Group

from core.game_engine import Deck, GameState, update_game_start_text, game_start_transition
from core.game_utils import get_starting_screen_card_backs_centered
from settings import *


def handle_mouse_click_game_start(captured_event, start_group):
    global current_game_state

    if len(captured_event) == 1:
        [x, y] = captured_event[0].pos
        if starting_UI_cards.sprites()[0].rect.collidepoint(x, y):
            selected_deck_cover = start_group.sprites()[0]
            game_start_transition(start_group.sprites()[0], screen)
            starting_UI_cards.empty()
            starting_UI_cards.add(selected_deck_cover)
        elif starting_UI_cards.sprites()[1].rect.collidepoint(x, y):
            selected_deck_cover = start_group.sprites()[1]
            game_start_transition(start_group.sprites()[1], screen)
            starting_UI_cards.empty()
            starting_UI_cards.add(selected_deck_cover)
        else:
            return False

        current_game_state = GameState.PLAY
        return True


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Cards War')
    clock = pygame.time.Clock()

    deck = Deck()
    deck.shuffle_deck()
    current_game_state = GameState.START

    starting_UI_cards: Group = Group(get_starting_screen_card_backs_centered(screen))

    while True:
        screen.fill(BACKGROUND_COLOR)
        if current_game_state == GameState.START:
            update_game_start_text(screen)
            starting_UI_cards.update()
            starting_UI_cards.draw(screen)

            event = pygame.event.get(pygame.MOUSEBUTTONUP)
            handle_mouse_click_game_start(event, starting_UI_cards)

        if current_game_state == GameState.PLAY:
            starting_UI_cards.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)
