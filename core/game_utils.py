from pygame.surface import Surface

from core.cards import Card


def get_starting_screen_card_backs_centered(screen: Surface) -> tuple:
    card_back_1 = Card("back", 1)
    card_back_1.rect.center = screen.get_rect().center
    card_back_1.rect.x -= 1.5 * card_back_1.rect.width

    card_back_2 = Card("back", 2)
    card_back_2.rect.center = screen.get_rect().center
    card_back_2.rect.x += 1.5 * card_back_2.rect.width

    return card_back_1, card_back_2
