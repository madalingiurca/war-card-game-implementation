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


def cardFight(card1, card2):
    if card1 > card2:
        return 1
    elif card2 > card1:
        return 2
    elif card1 == card2:
        return 0


def start_round(player1: Player, player2: Player):

    if player1.hasCards() and player2.hasCards():

        table = []

        p1_card = player1.playCard()
        p2_card = player2.playCard()

        table.extend([p1_card, p2_card])

        if p1_card == p2_card:
            try:
                p1_wcard = player1.playCard()
            except IndexError:
                p1_wcard = Card(0, None)
            try:
                p2_wcard = player2.playCard()
            except IndexError:
                p2_wcard = Card(0, None)

        # continue with War, cards have been drawn

        elif p1_card < p2_card:
            print("{} wins the round!".format(player2.name))
            player2.hand = table + player2.hand

        elif p1_card > p2_card:
            print("{} wins the round!".format(player1.name))
            player1.hand = table + player1.hand
