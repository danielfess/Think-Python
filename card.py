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

	def pop_card(self):
		return self.cards.pop()

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

class Hand(Deck):
	"""Represents a hand of playing cards.

	Attributes: cards, label
	"""

	def __init__(self, label =''):
		self.cards = []
		self.label = label

if __name__ == '__main__':
	card1 = Card(3,13)
	print(card1)
	card2 = Card(3,12)
	card3 = Card(0,13)
	print(card1 < card2)
	print(card3 < card2)

	deck1 = Deck()
	print('\nPre-shuffle')
	print(deck1)
	deck1.shuffle()
	print('\nPost-shuffle')
	print(deck1)
	deck1.sort()
	print('\nPost-sort')
	print(deck1)

	deck1.shuffle()
	hand1 = Hand('First player')
	hand2 = Hand('Second player')
	h = [hand1, hand2]
	for i in range(2):
		deck1.move_cards(h[i],5)
		print(h[i].label)
		print(h[i])



