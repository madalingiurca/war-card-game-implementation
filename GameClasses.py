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
        p1_card = player1.playCard()
        p2_card = player2.playCard()

        table = list()
        table.extend([p1_card, p2_card])

        if p1_card > p2_card:
            print("{} wins the round and the cards: {} {}".format(player1.name, p1_card, p2_card))
            player1.hand = table + player1.hand
        elif p1_card < p2_card:
            print("{} wins the round and the cards: {} {}".format(player2.name, p1_card, p2_card))
            player2.hand = table + player2.hand
        elif p1_card == p2_card:
            msg = "WAAAAAAAAAAARR"
            print(len(msg) * '_')
            print(msg)
            print(len(msg) * '_')
            if player1.hand.__len__() > 1 and player2.hand.__len__() > 1:
                # every player puts 1 face down card
                table.extend([player1.playCard(), player2.playCard()])
                # War cards played
                p1_warCard = player1.playCard()
                p2_warCard = player2.playCard()
                table.extend([p1_warCard, p2_warCard])

                if p1_warCard > p2_warCard:
                    print("{} wins the War and the cards: ".format(player1.name))
                    for card in table:
                        print(card)
                    print("\n")
                    player1.hand = table + player1.hand

                else:
                    print("{} wins the War and the cards:".format(player1.name))
                    for card in table:
                        print(card)
                    print("\n")
                    player1.hand = table + player1.hand

            else:

                if player1.hand.__len__() == 1:
                    print("Player {} has no more cards to fight at war".format(player1.name))
                    return 2
                else:
                    print("Player {} has no more cards to fight at war".format(player2.name))
                    return 1
    else:
        if not player1.hasCards():
            print("player 2 wins")
            return 2
        else:
            print("player 1 wins")
            return 1
