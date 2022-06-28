from Card import Card
from Deck import Deck
import DeckFactory
from random import shuffle

class Sorter:
    def __init__(
            self, number_of_decks):
        self._number_of_decks = number_of_decks
        self._super_deck = Deck()

    @property
    def super_deck(self):
        return self._super_deck

    @super_deck.setter
    def super_deck(
            self, new_val):
        self.super_deck = new_val

    def shuffle_sorter(self):
        shuffle(self.super_deck.cards)

    def generate_decks(self):
        for i in range(self._number_of_decks):
            temp_deck = DeckFactory.generate_deck()
            self.super_deck.cards += temp_deck.cards
        self.shuffle_sorter()

    def request_card(self) -> Card:
        if(len(self.super_deck.cards) < 1):
            return Card(0, "End of Deck")
                     
        return self.super_deck.cards.popleft()
        
    def number_of_cards_left(self):
        return len(self.super_deck.cards)

    def reset_sorter(self):
        self.super_deck.cards.clear()
        self.generate_decks()
