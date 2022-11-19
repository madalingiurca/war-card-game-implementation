from typing import Any

from pygame import Surface, SRCALPHA, Color, Rect
from pygame.sprite import Sprite


class ScoreBoard(Sprite):
    def __init__(self, player_name, position, font):
        self.font = font
        self.name = player_name
        self.position = position
        Sprite.__init__(self)
        self.score = 0
        self.update()

    def update(self, *args: Any, **kwargs: Any):
        height = self.font.get_height()
        text_surfaces = []

        for txt in (self.name, f'score {self.score}'):
            text_surfaces.append(self.font.render(txt, True, Color("black")))

        width = max(txt_surf.get_width() for txt_surf in text_surfaces)

        self.image = Surface((width, height * 2), SRCALPHA)
        self.image.get_rect().center = self.position

        for y, txt_surf in enumerate(text_surfaces):
            self.image.blit(txt_surf, (0, y * height))

        self.rect = self.image.get_rect()
        self.rect.center = self.position


class Player:
    def __init__(self, name="test"):
        self.hand = []
        self.name = name

    def draw_cards(self, deck):
        card = deck.popCard()
        self.hand.append(card)

    def play_card(self):
        card = self.hand.pop()
        return card

    def __str__(self):
        return "{} has {} cards left".format(self.name, len(self.hand))
