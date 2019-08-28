class Player:
    def __init__(self, name="test"):
        self.hand = []
        self.name = name

    def drawCards(self, deck):
        card = deck.popCard()
        self.hand.append(card)

    def playCard(self):
        card = self.hand.pop()
        return card

    def __str__(self):
        return "{} has {} cards left".format(self.name, len(self.hand))
