from card import Card, Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def __init__(self, label =''):
        self.cards = []
        self.score = {}
        self.label = label

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.
        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for score with more than 5 cards.
        """
        if 'flush' in self.score.keys():
            return self.score['flush']

        self.score['flush'] = False
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                self.score['flush'] = True
                break
        return self.score['flush']

    def has_pair(self):
        if 'pair' in self.score.keys():
            return self.score['pair']

        self.score['pair'] = False
        try:
            self.ranks
        except AttributeError:
            self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                self.score['pair'] = True
                break
        return self.score['pair']

    def has_twopair(self):
        if 'twopair' in self.score.keys():
            return self.score['twopair']

        self.score['twopair'] = False
        if self.has_pair():
            pairs = 0
            for val in self.ranks.values():
                if val >= 2:
                    pairs += 1
                if pairs == 2:
                    self.score['twopair'] = True
                    break
        return self.score['twopair']

    def has_three(self):
        if 'three' in self.score.keys():
            return self.score['three']

        self.score['three'] = False
        if self.has_pair():
            for val in self.ranks.values():
                if val >= 3:
                    self.score['three'] = True
        return self.score['three']

    def has_straight(self):
        if 'straight' in self.score.keys():
            return self.score['straight']

        self.score['straight'] = False
        try:
            self.ranks
        except AttributeError:
            self.rank_hist()
        run_length = 0
        for rank in range(1,14):
            if self.ranks.get(rank,0) == 0:
                run_length = 0
            else:
                run_length += 1
                if run_length == 5:
                    self.score['straight'] = True
        if run_length == 4 and self.ranks.get(1,0) != 0:
            self.score['straight'] = True
        return self.score['straight']

    def has_fullhouse(self):
        if 'fullhouse' in self.score.keys():
            return self.score['fullhouse']

        self.score['fullhouse'] = self.has_three() and self.has_twopair()
        return self.score['fullhouse']

    def has_four(self):
        if 'quads' in self.score.keys():
            return self.score['quads']

        self.score['quads'] = False
        if self.has_pair():
            for val in self.ranks.values():
                if val >= 4:
                    self.score['quads'] = True
        return self.score['quads']

    def has_strflush(self):
        if 'strflush' in self.score.keys():
            return self.score['strflush']

        self.score['strflush'] = False
        if self.has_flush() and self.has_straight():
            try:
                self.suits
            except AttributeError:
                self.suit_hist()
            for suit in range(4):
                if self.suits.get(suit,0) >= 5:
                    subhand = PokerHand()
                    for card in self.cards:
                        if card.suit == suit:
                            subhand.add_card(card)
                    if subhand.has_straight():
                        self.score['strflush'] = True
        return self.score['strflush']

    def classify(self):
        possible_score = ['high card','pair','twopair','three','straight','flush','fullhouse','quads','strflush']
        self.label = 'high card'
        self.has_pair()
        self.has_twopair()
        self.has_three()
        self.has_straight()
        self.has_flush()
        self.has_fullhouse()
        self.has_four()
        self.has_strflush()
        for i in range(8):
            if self.score[possible_score[8-i]]:
                self.label = possible_score[8-i]
                break

if __name__ == '__main__':

    possible_score = ['high card','pair','twopair','three','straight','flush','fullhouse','quads','strflush']
    count = {}
    for score in possible_score:
        count[score] = 0
    m = 200000
    n = 1
    total_hands = m*n
    for j in range(m):
        deck = Deck()
        deck.shuffle()
        for i in range(n):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.classify()
            count[hand.label] += 1
    print(count)
    probability = {}
    for score in possible_score:
        probability[score] = count[score]/total_hands
    print(probability)

