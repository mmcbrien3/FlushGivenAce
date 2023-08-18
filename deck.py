import random
from suit import Suit
from card import Card

class Deck():
    MIN_CARD_VALUE = 1
    MAX_CARD_VALUE = 13

    def __init__(self):
        self.cards = self._create_deck()

    def _create_deck(self):
        cards = set()
        for suit in Suit:
            for value in range(Deck.MIN_CARD_VALUE, Deck.MAX_CARD_VALUE + 1):
                cards.add(Card(value, suit))
        return cards

    def draw_random_card(self):
        card = self._get_random_card()
        return self._draw_card(card)
    
    def draw_n_random_cards(self, n):
        return [self.draw_random_card() for _ in range(n)]
    
    def draw_random_card_with_value(self, value):
        shuffled_cards = list(self.cards)
        random.shuffle(shuffled_cards)
        for card in shuffled_cards:
            if card.value == value:
                return self._draw_card(card)
        raise KeyError(f'Value {value} does not exist in deck')
    
    def _get_random_card(self):
        return random.sample(list(self.cards), 1)[0]
    
    def _draw_card(self, card):
        self.cards.remove(card)
        return card