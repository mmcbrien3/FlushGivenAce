class Hand():
    def __init__(self):
        self.cards = set()

    def add_card(self, card):
        self.cards.add(card)

    def does_hand_contain_value(self, value):
        for c in self.cards:
            if value == c.value:
                return True
        return False