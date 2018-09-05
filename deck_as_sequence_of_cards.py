import collections
from random import choice


# namedtuple can be used to build classes of objects that are
# just bundles of attributes with no custom methods, like a
# database record
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index: int):
        return self._cards[index]


deck = FrenchDeck()

print(len(deck))
# Outputs 52

print(deck[0])
# Outputs Card(rank='2', suit='spades')

print(choice(deck))
# Outputs random card from deck

print(deck[:3])
# Outputs 3 first cards of the deck

# Iterate through all the cards in deck
# Note : Iteration is often implicit. If a collection has
# no __contains__ method, the in operator does a sequential scan.
for card in reversed(deck):
    print(card)

print(Card('Q', 'hearts') in deck)
# Outputs True


suit_values = {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}


def get_card_value(card: Card) -> int:
    rank_value: int = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


print(f'Card {card} has value {get_card_value(card)}')
