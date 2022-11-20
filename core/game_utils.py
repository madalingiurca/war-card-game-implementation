import pygame
from pygame import SRCALPHA
from pygame.font import Font, get_default_font
from pygame.surface import Surface

from core.cards import Card
from settings import WHITE


class Button:
    def __init__(self, x, y, width, height, text='Button', color=pygame.Color("#ffffff"), on_click=None,
                 one_press=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.on_click = on_click
        self.one_press = one_press

        self.fill_colors = {
            'normal': color.correct_gamma(1),
            'hover': color.correct_gamma(0.3),
            'pressed': color.correct_gamma(1.2),
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = Font(get_default_font(), 25).render(text, True, (255, 255, 255))
        self.alreadyPressed = False

    def process(self):

        mouse_position = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fill_colors['normal'])
        if self.buttonRect.collidepoint(mouse_position):
            self.buttonSurface.fill(self.fill_colors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fill_colors['pressed'])

                if self.one_press:
                    self.on_click()
                elif not self.alreadyPressed:
                    self.on_click()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        pygame.display.get_surface().blit(self.buttonSurface, self.buttonRect)


def get_starting_screen_card_backs_centered(screen: Surface) -> tuple:
    card_back_1 = Card("back", 1)
    card_back_1.rect.center = screen.get_rect().center
    card_back_1.rect.x -= 1.5 * card_back_1.rect.width

    card_back_2 = Card("back", 2)
    card_back_2.rect.center = screen.get_rect().center
    card_back_2.rect.x += 1.5 * card_back_2.rect.width

    return card_back_1, card_back_2


def create_text2_surface(text1, text2):
    ending_text1 = Font(get_default_font(), 45).render(text1, True, WHITE)
    ending_text2 = Font(get_default_font(), 26).render(text2, True, WHITE)

    height = ending_text1.get_height()

    text_surface_width = max(ending_text1.get_rect().width, ending_text2.get_rect().width)
    text_surface_height = ending_text1.get_rect().height + ending_text1.get_rect().height

    text_surface = Surface((text_surface_width, text_surface_height), SRCALPHA)

    for y, txt_surf in enumerate([ending_text1, ending_text2]):
        text_surface.blit(txt_surf, ((text_surface_width - txt_surf.get_width()) // 2, y * height))

    return text_surface
