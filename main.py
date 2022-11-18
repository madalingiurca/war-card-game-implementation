from core.game_engine import Deck, start_round
from core.player import Player


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
name = input("Player 1: Name?\n").capitalize()
player1 = Player(name)
name = input("Player 2: Name?\n").capitalize()
player2 = Player(name)
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
rounds = 0
try:
    while True:
        rounds += 1
        start_round(player1, player2, table)
except IndexError:
    # print(player1, " | table cards:", len(table), " | ", player2)
    if len(player1.hand) == 0:
        player2.hand = table + player2.hand
        table.clear()
        print("\n________\nGameOver\n{} wins the game\nNo. of rounds: {}".format(player2.name, rounds))
    if len(player2.hand) == 0:
        player1.hand = table + player1.hand
        table.clear()
        print("\n________\nGameOver\n{} wins the game\nNo. of rounds: {}".format(player1.name, rounds))
