from enum import Enum
from random import shuffle

import pygame
from pygame import Surface
from pygame.font import Font, get_default_font

from core.cards import Card
from core.game_constants import STARTING_SCREEN_TEXT, GAME_TITLE
from core.player import Player
from settings import BACKGROUND_COLOR

color_speed = 1
color = [26, 115, 50]
color_direction = [0, 1, 0]


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


def game_start_transition(selected_deck_theme: Card, screen: Surface):
    animation_in_progress = True
    animation_limits = screen.get_rect().bottomleft

    selected_deck_theme.image = pygame.transform.scale(
        selected_deck_theme.image,
        (int(selected_deck_theme.image.get_size()[0] * 0.7), int(selected_deck_theme.image.get_size()[1] * 0.7))
    )

    while animation_in_progress:
        screen.fill(BACKGROUND_COLOR)
        screen.blit(selected_deck_theme.image, selected_deck_theme.rect)
        pygame.display.update()
        previous_center = selected_deck_theme.rect.center
        if selected_deck_theme.rect.bottomleft[0] > animation_limits[0]:
            selected_deck_theme.rect.x -= 2
        if not selected_deck_theme.rect.bottomleft[1] > animation_limits[1]:
            selected_deck_theme.rect.y += 2

        if previous_center == selected_deck_theme.rect.center:
            animation_in_progress = False


def color_update(color_to_update):
    for i in range(3):
        color_to_update[i] += color_speed * color_direction[i]
        if color_to_update[i] <= 115 or color_to_update[i] >= 255:
            color_direction[i] *= -1


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
        popped = self.cards.pop()
        return popped


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
