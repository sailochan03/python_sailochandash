from card import Card
import random

class DeckOfCards:
    NUMBER_OF_CARDS = 52
    def __init__(self):
        self.current_card = 0
        self.list_card = []
        for index in range(DeckOfCards.NUMBER_OF_CARDS):
            face = Card.FACES[index % 13]
            suit = Card.SUITS[index // 13]
            self.list_card.append(Card(face, suit))

    def deal_card(self):
        try:
            card = self.list_card[self.current_card]
            self.current_card += 1
            return card
        except IndexError:
            return None

    def shuffle_deck(self):
        random.shuffle(self.list_card)

    def __str__(self):
        cards = ''
        for i in range(52):
            cards += f'{str(self.list_card[i]):<30}'
            if (i + 1) % 4 == 0:
                cards += '\n'
        return cards
    
# deck = DeckOfCards()
# print(deck)
# deck.shuffle_deck()
# print(deck)
# deck.deal_card()