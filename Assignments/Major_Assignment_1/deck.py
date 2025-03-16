import random
from card import Card, Suit, Rank

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def __repr__(self):
        return f"Deck with {len(self.cards)} cards."