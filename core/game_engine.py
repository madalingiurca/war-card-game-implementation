import logging
from enum import Enum
from random import shuffle

import pygame
from pygame import Surface
from pygame.font import Font, get_default_font
from pygame.sprite import Group

from core.cards import Card
from core.game_constants import STARTING_SCREEN_TEXT, GAME_TITLE
from core.player import Player, ScoreBoard
from settings import BACKGROUND_COLOR

color_speed = 1
color = [26, 115, 50]
color_direction = [0, 1, 0]


def create_points_ui():
    points_ui_sprites_group = Group()
    player_score = ScoreBoard("Player 1", (1100, 650), Font(get_default_font(), 25))
    opponent_score = ScoreBoard("Eric Cartman", (100, 50), Font(get_default_font(), 25))

    points_ui_sprites_group.add(player_score)
    points_ui_sprites_group.add(opponent_score)
    return points_ui_sprites_group


def update_game_start_text(screen: Surface):
    start_game_message = Font(get_default_font(), 24).render(STARTING_SCREEN_TEXT, True, color)
    start_game_message_position = start_game_message.get_rect()
    start_game_message_position.center = screen.get_rect().center

    game_title = Font(get_default_font(), 28).render(GAME_TITLE, True, [26, 255, 50])
    game_title_position = game_title.get_rect()
    game_title_position.center = screen.get_rect().midtop
    game_title_position.y += 30

    screen.blit(start_game_message, start_game_message_position)
    screen.blit(game_title, game_title_position)

    color_update(color)


def handle_mouse_click_game_start(captured_event, start_group):
    if len(captured_event) == 1:
        [x, y] = captured_event[0].pos
        if start_group.sprites()[0].rect.collidepoint(x, y):
            player_deck_back = start_group.sprites()[0]
            opponent_deck_back = start_group.sprites()[0].duplicate()

        elif start_group.sprites()[1].rect.collidepoint(x, y):
            player_deck_back = start_group.sprites()[1]
            opponent_deck_back = start_group.sprites()[1].duplicate()

        else:
            return False

        player_deck_back.image = pygame.transform.scale(
            player_deck_back.image,
            (int(player_deck_back.image.get_size()[0] * 0.7), int(player_deck_back.image.get_size()[1] * 0.7))
        )
        opponent_deck_back.image = player_deck_back.image.copy()

        game_start_transition(player_deck_back, opponent_deck_back)

        start_group.empty()
        start_group.add(player_deck_back)
        start_group.add(opponent_deck_back)

        return True


def game_start_transition(player_deck: Card, opponent_deck: Card):
    screen = pygame.display.get_surface()

    player_deck_position = (screen.get_rect().bottomleft[0] + player_deck.rect.height // 2,
                            screen.get_rect().bottomleft[1] - player_deck.rect.width // 2)
    opponent_deck_position = (screen.get_rect().topright[0] - player_deck.rect.width // 2,
                              screen.get_rect().topright[1] + player_deck.rect.height // 2 + 30)

    while True:
        screen.fill(BACKGROUND_COLOR)
        screen.blit(player_deck.image, player_deck.rect)
        screen.blit(opponent_deck.image, opponent_deck.rect)
        pygame.display.update()

        move_card(player_deck, player_deck_position)
        move_card(opponent_deck, opponent_deck_position)

        if player_deck.rect.center == player_deck_position and opponent_deck.rect.center == opponent_deck_position:
            break


def move_card(card: Card, center):
    desired_x = center[0]
    desired_y = center[1]
    animation_step = 1

    x_speed = 1 if desired_x > card.rect.centerx else -1
    y_speed = 1 if desired_y > card.rect.centery else -1

    if card.rect.centerx != desired_x:
        card.rect.x += animation_step * x_speed
    if card.rect.centery != desired_y:
        card.rect.y += animation_step * y_speed


def color_update(color_to_update):
    for i in range(3):
        color_to_update[i] += color_speed * color_direction[i]
        if color_to_update[i] <= 115 or color_to_update[i] >= 255:
            color_direction[i] *= -1


def play_round(deck, clock):
    logging.info("Round started")
    screen = pygame.display.get_surface()

    player_card = deck.pop_card()
    player_card.rect.center = screen.get_rect().center
    player_card.move(-(player_card.rect.width // 2) - 25, 0)

    opponent_card = deck.pop_card()
    opponent_card.rect.center = screen.get_rect().center
    opponent_card.move((opponent_card.rect.width // 2) + 25, 0)

    pygame.display.get_surface().blit(player_card.image, player_card.rect)
    pygame.display.get_surface().blit(opponent_card.image, opponent_card.rect)

    result = player_card.compare_to(opponent_card)

    round_result_font = Font(get_default_font(), 24)

    if result == 0:
        round_result_text = round_result_font.render("WAR", True, pygame.Color("black"))
    else:
        round_result_text = round_result_font.render("You won!" if result > 0 else "You lost..", True,
                                                     pygame.Color("black"))

    round_result_text_position = list(screen.get_rect().center)
    round_result_text_position[0] -= round_result_text.get_rect().width // 2
    round_result_text_position[1] -= (player_card.rect.height // 2) + 120

    screen.blit(round_result_text, round_result_text_position)
    while True:
        logging.debug("waiting round result acknowledgement")

        events = pygame.event.get(pygame.MOUSEBUTTONUP)
        if len(events) == 1:
            break

        pygame.display.update()
        clock.tick(60)

    logging.info("Round finished")
    return result


class GameState(Enum):
    START = 0
    PLAY = 1
    WAR = 2
    ENDING = 3


class Deck:
    cards = []
    cardsType = ['heart', 'spade', 'clover', 'diamond']

    def __init__(self):
        for cardCol in self.cardsType:
            for i in range(2, 15):
                card = Card(i, cardCol)
                self.cards.append(card)

    def shuffle_deck(self):
        shuffle(self.cards)

    def pop_card(self) -> Card:
        return self.cards.pop()


def start_round(player1: Player, player2: Player, table: list):
    p1_card = player1.play_card()
    p2_card = player2.play_card()

    table += [p2_card, p1_card]
    if p1_card > p2_card:
        print("{} wins the round".format(player1.name))
        shuffle(table)
        player1.hand = table + player1.hand
        table.clear()
        return 0
    if p2_card > p1_card:
        print("{} wins the round".format(player2.name))
        shuffle(table)
        player2.hand = table + player2.hand
        table.clear()
        return 0
    start_round(player1, player2, table)
