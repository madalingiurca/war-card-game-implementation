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
player1 = Player("Claudia")
# name = input("Player 2: Name?\n")
player2 = Player("Aron")

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

# print("{}: ".format(player1.name), end='')
# for card in player1.hand:
#     print(card.number, end='| ')
# print('\n')
# print("{}: ".format(player2.name), end='')
# for card in player2.hand:
#     print(card.number, end='| ')
# print('\n')

# Inceputul jocului
# Acesta se termina cand unul din jucatori ramane fara carti
# De asemenea daca se ajunge la razboi si unul din jucatori nu detine suficiente carti acesta este invins
msg = "Start Game"
print("*" * len(msg))
print(msg)
print("*" * len(msg))
status = start_round(player1, player2)
round = 1
while status == 0:
    print("#{} ".format(round), end="")
    status = start_round(player1, player2)
    round += 1
    print("{} vs {}".format(len(player1.hand), len(player2.hand)))

if status == 1:
    print("GAME OVER\n{} wins the game!".format(player1.name))
elif status == 2:
    print("GAME OVER\n{} wins the game!".format(player2.name))
