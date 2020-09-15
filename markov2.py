import sys
import string
import random

class Markov:
    """For Markov Analysis of text.

    Attributes: suffix_map, prefix
    """

    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()


    def process_file(self, filename, format='utf8', order=2):
        """Reads a file and performs Markov analysis.
        filename: string
        order: integer number of words in the prefix
        returns: map from prefix to list of possible suffixes.
        """
        fp = open(filename, encoding = format)
        for line in fp:
            if line.startswith('*** START OF THIS'):
                break

        for line in fp:
            if line.startswith('*** END OF THIS'): 
                break

            for word in line.rstrip().split():
                self.process_word(word.lower(), order)


    def process_word(self, word, order):
        """Processes each word.
        word: string
        order: integer
        During the first few iterations, all we do is store up the words; 
        after that we start adding entries to the dictionary.
        """
        if len(self.prefix) < order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            # if there is no entry for this prefix, make one
            self.suffix_map[self.prefix] = [word]

        self.shift(word)

    def random_text(self,n=100):
        """Generates random words from the analyzed text.
        Starts with a random prefix from the dictionary.
        n: number of words to generate
        """
        # choose a random prefix (not weighted by frequency)
        start = random.choice(list(self.suffix_map.keys()))
    
        for i in range(n):
            suffixes = self.suffix_map.get(start, None)
            if suffixes == None:
                # if the start isn't in map, we got to the end of the
                # original text, so we have to start again.
                random_text(n-i)
                return

            # choose a random suffix
            word = random.choice(suffixes)
            print(word, end=' ')
            start = start[1:] + (word,)


    def shift(self, word):
        """Forms a new prefix by removing the head and adding word to the tail.
        word: string
        """
        self.prefix = self.prefix[1:] + (word,)


if __name__ == '__main__':
    file1 = 'sherlock_holmes.txt'
    sherlock_markov = Markov()
    sherlock_markov.process_file(file1)
    sherlock_markov.random_text()
    sherlock_markov.random_text(50)

    print('\n')

    file2 = 'alice_in_wonderland.txt'
    sherlock_alice = sherlock_markov
    sherlock_alice.process_file(file2)
    sherlock_alice.random_text()
    sherlock_alice.random_text(50)
