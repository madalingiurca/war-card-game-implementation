import sys

from pygame import Color

from core.game_constants import *
from core.game_engine import *
from core.game_utils import get_starting_screen_card_backs_centered, Button, create_text2_surface
from settings import *

current_game_state = GameState.START

if __name__ == '__main__':

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Cards War')
    clock = pygame.time.Clock()
    logging.basicConfig(level=LOGGING_LEVEL)

    sc_x = screen.get_rect().center[0]
    sc_y = screen.get_rect().center[1]

    win_screen_surface = create_text2_surface(ENDING_CONGRATS, ENDING_MESSAGE_WIN)
    lose_screen_surface = create_text2_surface(ENDING_LOSE, ENDING_MESSAGE_LOST)

    deck = Deck()
    deck.shuffle_deck()

    card_deck_backs = Group(get_starting_screen_card_backs_centered(screen))
    points_ui = create_points_ui()


    def start_over():
        global current_game_state, deck, points_ui
        current_game_state = GameState.START
        deck = Deck()
        deck.shuffle_deck()
        points_ui = create_points_ui()


    def quit_game():
        pygame.quit()
        sys.exit()


    play_again_b = Button(sc_x - (220 // 2) - 250, sc_y, 220, 80, "Play again", Color("#31AA06"), on_click=start_over)
    quit_b = Button(sc_x - (220 // 2) + 250, sc_y, 220, 80, "Quit", Color("#D11D1D"), on_click=quit_game)

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
            play_instruction = Font(get_default_font(), 20).render("Play card", True, pygame.Color("black"))

            screen.blit(play_instruction, player_deck_ui.rect.center)
            if len(events) == 1 and player_deck_ui.rect.collidepoint(events[0].pos[0], events[0].pos[1]):
                round_result = play_round(deck, clock)
                if round_result > 0:
                    points_ui.sprites()[0].score += 1
                elif round_result < 0:
                    points_ui.sprites()[1].score += 1

                if len(deck.cards) < 2:
                    current_game_state = GameState.ENDING

        if current_game_state == GameState.ENDING:
            text = win_screen_surface \
                if points_ui.sprites()[0].score > points_ui.sprites()[1].score \
                else lose_screen_surface

            text_rect = text.get_rect()
            text_rect.center = screen.get_rect().center

            score_text = Font(get_default_font(), 26).render("Your score is: " + str(points_ui.sprites()[0].score),
                                                             True, WHITE)
            score_rect = score_text.get_rect()
            score_rect.center = screen.get_rect().center

            screen.blit(text, text_rect.move(0, -200))
            screen.blit(score_text, score_rect.move(0, 250))

            play_again_b.process()
            quit_b.process()
            logging.info("Game ended")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        pygame.display.update()
        clock.tick(60)
