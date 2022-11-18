import os
from enum import Enum
from random import shuffle

import pygame.image
from pygame import Surface
from pygame.font import Font, get_default_font
from pygame.sprite import Sprite

from GameConstants import STARTING_SCREEN_TEXT
from Player import Player

color_speed = 1
color = [26, 115, 50]
color_direction = [0, 1, 0]


def draw_starting_screen(screen: Surface):
    card_back_1 = Card("back", 1)
    card_back_1.rect.center = screen.get_rect().center
    card_back_1.rect.x -= 1.5 * card_back_1.rect.width

    card_back_2 = Card("back", 2)
    card_back_2.rect.center = screen.get_rect().center
    card_back_2.rect.x += 1.5 * card_back_2.rect.width

    font = Font(get_default_font(), 24)

    screen.blit(card_back_1.image, card_back_1.rect)
    screen.blit(card_back_2.image, card_back_2.rect)
    screen.blit(
        font.render(STARTING_SCREEN_TEXT, True, color),
        (screen.get_rect().height // 2, screen.get_rect().width // 2)
    )

    color_update(color)


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


class Card(Sprite):
    def __init__(self, no, card_type):
        super().__init__()
        self.number = no
        self.type = card_type
        self.image = pygame.image.load(f"{os.getcwd()}/assets/cards/{self.number}_{self.type}.png").convert()

        self.rect = self.image.get_rect()

    def __lt__(self, other):
        if self.number < other.number:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.number > other.number:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.number == other.number:
            return True
        else:
            return False

    def __str__(self):
        return "{} {}".format(self.number, self.type)


class Deck:
    cards = []
    cardsType = ['heart', 'spade', 'clover', 'diamond']

    def __init__(self):
        for cardCol in self.cardsType:
            for i in range(2, 15):
                card = Card(i, cardCol)
                self.cards.append(card)

    def shuffleDeck(self):
        shuffle(self.cards)

    def popCard(self) -> Card:
        popped = self.cards.pop()
        return popped


def start_round(player1: Player, player2: Player, table: list):
    p1Card = player1.playCard()
    p2Card = player2.playCard()

    table += [p2Card, p1Card]
    if p1Card > p2Card:
        print("{} wins the round".format(player1.name))
        shuffle(table)
        player1.hand = table + player1.hand
        table.clear()
        return 0
    if p2Card > p1Card:
        print("{} wins the round".format(player2.name))
        shuffle(table)
        player2.hand = table + player2.hand
        table.clear()
        return 0
    start_round(player1, player2, table)
