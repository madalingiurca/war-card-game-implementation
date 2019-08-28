from random import shuffle

from Player import Player


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
        if self.number > other.number:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.number == other.number:
            return True
        else:
            return False

    def __str__(self):
        return "{} {}".format(self.number, self.cardType)


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


def start_round(player1: Player, player2: Player, table: list):
    p1Card = player1.playCard()
    p2Card = player2.playCard()

    table += [p2Card, p1Card]
    if p1Card > p2Card:
        print("{} wins the round".format(player1.name))
        shuffle(table)
        player1.hand = table + player1.hand
        table.clear()
        return 0
    if p2Card > p1Card:
        print("{} wins the round".format(player2.name))
        shuffle(table)
        player2.hand = table + player2.hand
        table.clear()
        return 0
    start_round(player1, player2, table)
