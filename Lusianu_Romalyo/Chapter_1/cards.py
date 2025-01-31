import collections

Card = collections.namedtuple('Card', ['rank', 'suite'])


class RussianDeck:
    ranks = [str(i) for i in range(2, 11)] + list('ВДКТ')
    suits = 'пики крести буби черви'.split()

    def __init__(self):
        self._cards = [Card(rank, suite) for suite in self.suits for rank in self.ranks]  # вложенный цикл в генераторе списка

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]




