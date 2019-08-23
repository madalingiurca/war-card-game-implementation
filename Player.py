class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def drawCards(self, deck):
        card = deck.popCard()
        self.hand.append(card)

    def playCard(self):
        try:
            card = self.hand.pop()
            return card
        except IndexError:
            return "{name} has no more cards".format(name=self.name)
