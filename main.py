from GameClasses import Deck, startRound
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

noRounds = 0
#printHands(player1, player2)
while player1.hasCards() and player2.hasCards():
    noRounds += 1
    status = startRound(player1, player2)
    if status == 1:
        print("it is over")
        break
    printHands(player1, player2)
    #print('Nr runde: ',noRounds)
    print("Mirel: {}, Mihai: {}".format(player1.hand.__len__(), player2.hand.__len__()))
print("Game Over", noRounds)
