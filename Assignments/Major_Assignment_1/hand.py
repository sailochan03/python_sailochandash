from card import Card, Rank

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def calculate_total(self):
        total = sum(card.rank.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == Rank.ACE)

        for _ in range(aces):
            if total + 10 <= 21:
                total += 10
        return total

    def __repr__(self):
        return f"Hand: {', '.join(map(str, self.cards))} (Total: {self.calculate_total()})"