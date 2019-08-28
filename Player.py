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
        except IndexError as err:
            return err

    def hasCards(self):
        if self.hand.__len__() > 0:
            return True
        else:
            return False
