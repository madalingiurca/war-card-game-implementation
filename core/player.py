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
