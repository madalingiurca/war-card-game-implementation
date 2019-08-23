from random import shuffle

from Player import Player


def cardFight(card1, card2):
    if card1 > card2:
        return 1
    elif card2 > card1:
        return 2
    else:
        return 0


def startGame(p1: Player, p2: Player):
    card1 = p1.hand.pop()
    card2 = p2.hand.pop()
    res = cardFight(card1, card2)
    if res == 1:
        print("!!!P1 won cards {},{}".format(card1.number, card2.number))
        p1.hand.insert(0, card1)
        p1.hand.insert(0, card2)
        # print("player 1 won the hand")
    elif res == 2:
        print("!!!P2 won cards {},{}".format(card1.number, card2.number))
        p2.hand.insert(0, card1)
        p2.hand.insert(0, card2)
        # print("player 2 won the hand")
    else:
        startGame(p1, p2)


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
