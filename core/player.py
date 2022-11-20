from typing import Any

from pygame import Surface, SRCALPHA, Color
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

        # noinspection PyCompatibility
        for txt in (self.name, f'score {self.score}'):
            text_surfaces.append(self.font.render(txt, True, Color("black")))

        width = max(txt_surf.get_width() for txt_surf in text_surfaces)

        self.image = Surface((width, height * 2), SRCALPHA)
        self.image.get_rect().center = self.position

        for y, txt_surf in enumerate(text_surfaces):
            self.image.blit(txt_surf, (0, y * height))

        self.rect = self.image.get_rect()
        self.rect.center = self.position
