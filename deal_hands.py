import random

class Card:
	"""Represents a card from a deck of 52 playing cards.

	Attributes: suit, rank
	"""

	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8' , '9', '10', 'Jack', 'Queen', 'King']

	def __init__(self, suit=0, rank=2):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

	def __eq__(self,other):
		return self.suit == other.suit and self.rank == other.rank

	def __lt__(self,other):
		t1 = (self.suit, self.rank)
		t2 = (other.suit, other.rank)
		return t1 < t2

class Deck:
	"""Represents a deck of playing cards.

	Attributes: cards
	"""

	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def shuffle(self):
		random.shuffle(self.cards)

	def remove_card(self, card):
        self.cards.remove(card)

	def pop_card(self, i=-1):
		"""Removes and returns a card from the deck.
		i: index of the card to be removed (default=last card)
		"""

		return self.cards.pop(i)

	def add_card(self,card):
		self.cards.append(card)

	def sort(self):
		self.cards.sort()

	def move_cards(self,hand,n):
		"""Moves n cards from self to hand.

		hand: Deck or Hand object
		"""

		for i in range(n):
			hand.add_card(self.pop_card())

	def deal_hands(self,n_hands,n_cards):
		"""Deals n_hands number of hands from self,
		with each hand having n_cards number of cards.
		"""

		hands = []
		for i in range(n_hands):
			hands.append(Hand())
			self.move_cards(hands[i],n_cards)
		return hands


class Hand(Deck):
	"""Represents a hand of playing cards.

	Attributes: cards, label
	"""

	def __init__(self, label =''):
		self.cards = []
		self.label = label


if __name__ == '__main__':
	deck = Deck()
	deck.shuffle()
	hands = deck.deal_hands(4,2)
	for item in hands:
		print(item)
		print('\n')

	c1 = Card(0,1)
	c2 = Card(0,1)
	print(c1 is c2)



