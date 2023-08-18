from enum import Enum
import random

from deck import Deck
from hand import Hand
from hand_definition import Flush
from hand_definition import Pair

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


if __name__ == "__main__":
    def random_hand(hand, deck):
        [hand.add_card(card) for card in deck.draw_n_random_cards(5)]

    def first_card_ace(hand, deck):
        hand.add_card(deck.draw_random_card_with_value(1))
        [hand.add_card(card) for card in deck.draw_n_random_cards(4)]

    def run_n_simulations_for_hand(n, title, hand_generation, hand_defintion_type):
        flush_count = 0
        for _ in range(n):
            deck = Deck()
            hand = Hand()
            hand_generation(hand, deck)
            if hand_defintion_type.does_hand_match_definition(hand):
                flush_count += 1
        print(f'Flush probability ({title}): {flush_count/n}')

    hands_to_create = 1_000
    run_n_simulations_for_hand(hands_to_create, "random hand", random_hand, Flush) # Flush probability (random hand): 0.002068
    run_n_simulations_for_hand(hands_to_create, "first card ace", first_card_ace, Flush) # Flush probability (first card ace): 0.00193
