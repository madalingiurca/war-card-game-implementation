from random import shuffle


def cardFight(deck1, deck2):
    card1 = deck1.pop()
    card2 = deck2.pop()

    if card1 > card2:
        print("castiga p1")
        return 1
    elif card1 < card2:
        print("castiga p2")
        return 2
    else:
        print("+1 mana")
        return cardFight(deck1, deck2)


# def StartGame(p1, p2):


class Card:
    def __init__(self, no, cardType):
        self.number = no
        self.cardType = cardType

    def __lt__(self, other):
        if self.number < other.number:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.number >= other.number:
            return True
        else:
            return False


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
