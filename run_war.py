import sys

from core.game_engine import *
from core.game_utils import get_starting_screen_card_backs_centered
from settings import *

if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Cards War')
    clock = pygame.time.Clock()
    logging.basicConfig(level=LOGGING_LEVEL)

    deck = Deck()
    deck.shuffle_deck()
    deck.pop_card()
    # current_game_state = GameState.START
    current_game_state = GameState.START

    card_deck_backs: Group = Group(get_starting_screen_card_backs_centered(screen))
    points_ui: Group = create_points_ui()

    while True:
        screen.fill(BACKGROUND_COLOR)
        if current_game_state == GameState.START:
            update_game_start_text(screen)
            card_deck_backs.update()
            card_deck_backs.draw(screen)

            event = pygame.event.get(pygame.MOUSEBUTTONUP)
            if handle_mouse_click_game_start(event, card_deck_backs):
                current_game_state = GameState.PLAY

        if current_game_state == GameState.PLAY:
            points_ui.update(screen)
            points_ui.draw(screen)

            player_deck_ui = card_deck_backs.sprites()[0]
            player_deck_ui.update(screen, max_width=140, persistent_width=136)
            card_deck_backs.draw(screen)

            events = pygame.event.get(pygame.MOUSEBUTTONUP)
            if len(events) == 1 and player_deck_ui.rect.collidepoint(events[0].pos[0], events[0].pos[1]):
                play_round(deck, clock)
                if len(deck.cards) < 2:
                    current_game_state = GameState.ENDING

        if current_game_state == GameState.ENDING:
            logging.info("Game ended")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)
