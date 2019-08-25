class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def drawCards(self, deck):
        card = deck.popCard()
        self.hand.append(card)

    def playCard(self):
            return self.hand.pop()

    def hasCards(self):
        return self.hand.__len__() != 0
