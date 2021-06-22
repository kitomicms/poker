# start a game
from Deck import *

deck = Deck()

while deck.card_left() > 0:
  print(deck.deal())


