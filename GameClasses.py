from random import shuffle


class Card:
    def __init__(self, no, cardType):
        self.number = no
        self.cardType = cardType


class Deck:
    cards = []
    cardsType = ['heart', 'spades', 'clubs', 'diamond']

    def __init__(self):
        for cardCol in self.cardsType:
            for i in range(2, 15):
                card = Card(i, cardCol)
                self.cards.append(card)

    def shuffleDeck(self):
        shuffle(self.cards)

    def popCard(self):

        popped = self.cards.pop()
        return popped
