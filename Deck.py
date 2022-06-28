import collections
from Card import Card
import collections

class Deck:
    def __init__(self):
        self._cards = collections.deque()
    
    def __str__(self):
        for card in self._cards:
            print(str(card))

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, new_cards):
        self._cards = new_cards

    def generate_deck(self):
        suits = [
            'Hearts', 'Spades',
            'Clubs', 'Diamonds'
            ]
        self._cards = collections.deque(
                Card(value,suit) for value in range(1,14) for suit in suits)