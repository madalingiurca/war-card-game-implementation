from GameClasses import Deck, start_round
from Player import Player


def printHands(p1, p2):
    print(p1.name, ': ', end='')
    for card in p1.hand:
        print(card.number, end='| ')
    print('\n')
    print(p2.name, ': ', end='')
    for card in p2.hand:
        print(card.number, end='| ')
    print('\n')


deck = Deck()
deck.shuffleDeck()
# name = input("Player 1: Name?\n")
player1 = Player("Mirel")
# name = input("Player 2: Name?\n")
player2 = Player("Mihai")
while True:
    try:
        player1.drawCards(deck)
        player2.drawCards(deck)
    except IndexError:
        print("Cards has been split!\n")
        break

print("| {p1Name}: {p1CardsNO} cards | VS |".format(p1Name=player1.name, p1CardsNO=player1.hand.__len__()), end=" ")
print("{p2Name}: {p2CardsNO} cards|".format(p2Name=player2.name, p2CardsNO=player2.hand.__len__()))

# Inceputul jocului
# Acesta se termina cand unul din jucatori ramane fara carti
# Castigatorul se declara cel care inca are Cards in lista self.hand
table = list()
try:
    while True:
        start_round(player1, player2, table)
        print(player1, " | table cards:", len(table), " | ", player2)

except IndexError:
    if len(player1.hand) == 0:
        print("P2 Wins")
    if len(player2.hand) == 0:
        print("P1 Wins")