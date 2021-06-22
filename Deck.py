# create a deck class
class Deck():
  def __init__(self):
    patterns = ['spade','diamond','heart','cube']
    numbers = [x for x in range(2,11)] + ['J','Q','K','A']
    self.deck = []
    for pattern in patterns:
      for number in numbers:
        self.deck.append([pattern,number])
  def shuffle(self):
    random.shuffle(self.deck)


  def card_left(self):
    return len(self.deck)

  def deal(self,no_of_cards):
    dealed_card = self.deck.pop(0)
    return dealed_card
