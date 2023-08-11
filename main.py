from enum import Enum
import random

# Terms
## P(F) = probability of five hand flush
## Note: straight flush and royal flush are flushes
## P(A) = probability of having at least 1 ace present in five hand
## P(F | A) = probability of flush in five hand given at least one ace is present
## P(A | F) = probability of at least one ace is present given five hand flush

# Bayes
## P(F | A) = P(A | F) * P(F) / P(A)
## If P(F | A) = P(F) then P(A | F) must equal P(A)

# Numbers
## P(A) = 1 - ~P(A)
## ~P(A) = (48 choose 5) / (52 choose 5)
## Note: 52 choose 5 is how many five hands are possible from a 52 card deck
## Note: 48 choose 5 is how many five hands are possible from a 52 card deck excluding one value (e.g. ace)
## ~P(A) = 0.6588
## P(A) = 1 - ~P(A) = .3412

## P(F) = (4 choose 1) * (13 choose 5) / (52 choose 5)
## Note: 4 choose 1 chooses one from four suits
## Note: 13 choose 5 chooses 5 values from 13 possibilities within suit
## P(F) = 0.001981
## Note: wikipedia agrees: https://en.wikipedia.org/wiki/Poker_probability

## P(A | F) = ((13 choose 5) - (12 choose 5)) / (13 choose 5)
## Note: this method finds the number of flushes with a given card. 13 choose 5
## is the number of flushes possible within a single suit. 12 choose 5 would
## be the number of flushes possible, disregarding some value (e.g. Ace)
## P(A | F) = 0.3846
## Another way to arrive at the same result:
## Number of flushes from wikipedia: 5148
## Number of flushes with aces would be: (12 choose 4) * (4 choose 1). Start choosing any ace
## (4 choose 1) and then multiply by hands that make the flush: four cards and choose
## from 12 within the same suit.
## This gives: 1980
## 1980 / 5148 = 0.3846

# Result
## From here we see that P(A | F) = 0.3846 != P(A) = 0.3412
## This leads to P(F | A) = 0.3846 * 0.001981 / 0.3412 = 0.002233
## This implies that if it is known that a hand has an ace, the odds of flush increases?

class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4

class Card():
    VALUE_MAP = {
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King"
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit
    
    def __hash__(self):
        return hash(f'{self.value}{self.suit}')
    
    def __str__(self):
        value_name = str(self.value) if self.value not in Card.VALUE_MAP else Card.VALUE_MAP.get(self.value)
        return f'{value_name} of {self.suit.name}'
    
    def __repr__(self):
        return self.__str__()

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
            
class Hand():
    def __init__(self):
        self.cards = set()

    def add_card(self, card):
        self.cards.add(card)

    def _get_suit_to_count_map(self):
        output = {}
        for c in self.cards:
            output[c.suit] = output.get(c.suit, 0) + 1
        return output
    
    def is_flush(self):
        if len(self.cards) != 5:
            raise ValueError(f'Hand has incorrect number of cards {len(self.cards)}')
        suit_to_count_map = self._get_suit_to_count_map()
        return max(suit_to_count_map.values()) == 5

if __name__ == "__main__":
    def random_hand(hand, deck):
        [hand.add_card(card) for card in deck.draw_n_random_cards(5)]

    def first_card_ace(hand, deck):
        hand.add_card(deck.draw_random_card_with_value(1))
        [hand.add_card(card) for card in deck.draw_n_random_cards(4)]

    def run_n_simulations_for_flush(n, title, hand_generation):
        flush_count = 0
        for _ in range(n):
            deck = Deck()
            hand = Hand()
            hand_generation(hand, deck)
            if hand.is_flush():
                flush_count += 1
        print(f'Flush probability ({title}): {flush_count/n}')

    hands_to_create = 1_000_000
    run_n_simulations_for_flush(hands_to_create, "random hand", random_hand)
    run_n_simulations_for_flush(hands_to_create, "first card ace", first_card_ace)
