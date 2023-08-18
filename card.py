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