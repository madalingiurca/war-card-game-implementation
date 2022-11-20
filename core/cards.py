from __future__ import annotations

import logging
import os
from typing import Any

import pygame
from pygame.sprite import Sprite


class Card(Sprite):
    def __init__(self, no, card_type):
        Sprite.__init__(self)
        self.number = no
        self.type = card_type
        # noinspection PyCompatibility
        self.image = pygame.image.load(f"{os.getcwd()}/assets/cards/{self.number}_{self.type}.png").convert()
        self.default_size = self.image.get_size()
        self.rect = self.image.get_rect()

    def update(self, *args: Any, **kwargs: Any) -> None:
        zoom_factor = kwargs.get("zoom_factor") if "zoom_factor" in kwargs else 1.05
        max_width = kwargs.get("max_width") if "max_width" in kwargs else 195
        persistent_width = kwargs.get("persistent_width") if "persistent_width" in kwargs else 179
        if self.rect.collidepoint(pygame.mouse.get_pos()) and self.image.get_rect().width < max_width:
            self.zoom(zoom_factor)
        elif not self.rect.collidepoint(pygame.mouse.get_pos()) and self.image.get_rect().width >= persistent_width:
            self.zoom(2 - zoom_factor)

    def compare_to(self, other: Card) -> int:
        if self.number == other.number:
            return 0
        else:
            return 1 if self.number > other.number else -1

    def zoom(self, zoom_factor):
        # noinspection PyCompatibility
        logging.debug(f"Zooming with zoom factor: {zoom_factor}, current width: {self.rect.width}")
        current_size = self.image.get_size()
        self.image = pygame.transform.scale(
            self.image,
            (int(current_size[0] * zoom_factor), int(current_size[1] * zoom_factor))
        )
        self.rect.width = self.image.get_rect().width
        self.rect.height = self.image.get_rect().height

    def move(self, x_offset: int, y_offset: int):
        self.rect.x += x_offset
        self.rect.y += y_offset

    def duplicate(self):
        duplicate = Card(self.number, self.type)
        duplicate.image, duplicate.rect = self.image.copy(), self.rect.copy()

        return duplicate
