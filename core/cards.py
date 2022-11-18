import math
import os
from typing import Any

import pygame
from pygame.sprite import Sprite

MAX_IMAGE_SIZE = 50_000
ZOOM_FACTOR = 1.05


class Card(Sprite):
    def __init__(self, no, card_type):
        Sprite.__init__(self)
        self.number = no
        self.type = card_type
        self.image = pygame.image.load(f"{os.getcwd()}/assets/cards/{self.number}_{self.type}.png").convert()
        self.default_size = self.image.get_size()
        self.rect = self.image.get_rect()

    def update(self, *args: Any, **kwargs: Any) -> None:
        if self.rect.collidepoint(pygame.mouse.get_pos()) and self.image.get_rect().width < 195:
            print(f"Zooming in: {self.rect.width}")
            current_size = self.image.get_size()
            self.image = pygame.transform.scale(
                self.image,
                (int(current_size[0] * ZOOM_FACTOR), int(current_size[1] * ZOOM_FACTOR))
            )

        elif not self.rect.collidepoint(pygame.mouse.get_pos()) and self.image.get_rect().width >= 179:
            print(f"Zooming out: {self.rect.width}")
            current_size = self.image.get_size()
            self.image = pygame.transform.scale(
                self.image,
                (int(current_size[0] * (2 - ZOOM_FACTOR)), int(current_size[1] * (2 - ZOOM_FACTOR)))
            )
