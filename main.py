from GameClasses import Deck, start_round
from Player import Player

deck = Deck()
# for card in deck.cards:
#     print(card.cardType + " " + str(card.number), end= ' | ')
#
deck.shuffleDeck()
# print('\n')
# for card in deck.cards:
#     print(card.cardType + " " + str(card.number), end= ' | ')
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

# for card in player1.hand:
#     print(card.number,' ',card.cardType, end='\n')
#
# print('\n')
# for card in player1.hand:
#     print(card.number,' ', card.cardType, end='\n')

print("| {p1Name}: {p1CardsNO} cards | VS |".format(p1Name=player1.name, p1CardsNO=player1.hand.__len__()), end=" ")
print("{p2Name}: {p2CardsNO} cards|".format(p2Name=player2.name, p2CardsNO=player2.hand.__len__()))

# Inceputul jocului
# Acesta se termina cand unul din jucatori ramane fara carti
# Castigatorul se declara cel care inca are Cards in lista self.hand
print("Mirel: ", end='')
for card in player1.hand:
    print(card.number, end='| ')
print('\n')
print("Mihai: ", end='')
for card in player2.hand:
    print(card.number, end='| ')
print('\n')
print("______________\nSTART GAME\n____________")
status = start_round(player1, player2)
while status != 1 and status != 2:
    status = start_round(player1, player2)
