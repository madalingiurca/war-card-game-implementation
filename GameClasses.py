from random import shuffle

from Player import Player


def WarGame():
    pass


def startRound(player1: Player, player2: Player):
    table = list()

    Player1Card = player1.playCard()
    #   print("{} played {} card".format(player1.name, Player1Card.number))
    Player2Card = player2.playCard()
    #   print("{} played {} card".format(player2.name, Player2Card.number))

    table.append(Player1Card)
    table.append(Player2Card)

    if Player1Card > Player2Card:
        #      print("{} wins the round!".format(player1.name))
        player1.hand = table + player1.hand
    elif Player2Card > Player1Card:
        #      print("{} wins the round!".format(player2.name))
        player2.hand = table + player2.hand
    else:                   # War TIME
        msg = 'War Starts'
        print('-' * len(msg))
        print(msg)
        print('-' * len(msg))
        if player2.hand.__len__() == 1 or player1.hand.__len__() == 1:
            print("weak players")
            return 1
        for i in range(3):
            table.extend([player1.playCard(), player2.playCard()])
        warCardP1 = player1.playCard()
        warCardP2 = player2.playCard()
#
        table = [warCardP1, warCardP2] + table
        if warCardP1 > warCardP2:
            #            print("{} wins the war!".format(player1.name))
            player1.hand = table + player1.hand
        elif warCardP2 > warCardP1:
            #            print("{} wins the war!".format(player2.name))
            player2.hand = table + player2.hand


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
