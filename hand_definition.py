from hand import Hand



class IHandDefinition():

    def theoretical_probability():
       pass

    def does_hand_match_definition(hand: Hand):
        pass

class Flush(IHandDefinition):

    def theoretical_probability():
        return 0.001981

    def _get_suit_to_count_map(cards):
        output = {}
        for c in cards:
            output[c.suit] = output.get(c.suit, 0) + 1
        return output
    
    def does_hand_match_definition(hand: Hand):
        cards = hand.cards
        if len(cards) != 5:
            raise ValueError(f'Hand has incorrect number of cards {len(cards)}')
        suit_to_count_map = Flush._get_suit_to_count_map(cards)
        return max(suit_to_count_map.values()) == 5

class Pair(IHandDefinition):

    def theoretical_probability():
        return 0.4929

    def does_hand_match_definition(hand: Hand):
        cards = hand.cards
        card_values_list = [c.value for c in cards]
        card_values_set = set(card_values_list)
        return len(card_values_list) != len(list(card_values_set))

class NoHand(IHandDefinition):

    def theoretical_probability():
        0.50118

    def does_hand_match_definition(hand: Hand):
        pass

ALL_DEFINITIONS = [
    Flush,
    Pair
]