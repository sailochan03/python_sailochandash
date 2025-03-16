from hand import Hand
from deck import Deck

class BlackjackGame:
    def __init__(self, num_players):
        self.deck = Deck()
        self.players = [Hand() for _ in range(num_players)]
        self.dealer = Hand()
        self.dealer_busted = False

    def deal_initial_cards(self):
        for hand in self.players:
            hand.add_card(self.deck.draw_card())
            hand.add_card(self.deck.draw_card())
        self.dealer.add_card(self.deck.draw_card())
        self.dealer.add_card(self.deck.draw_card())

    def player_turn(self, player_index):
        hand = self.players[player_index]
        while True:
            print(f"\nPlayer {player_index + 1}'s hand: {hand}")
            if hand.calculate_total() > 21:
                print(f"Player {player_index + 1} busts!")
                return False
            action = input("Do you want to (h)it or (s)tand? ").lower()
            if action == 'h':
                hand.add_card(self.deck.draw_card())
            elif action == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")
        return hand.calculate_total() <= 21

    def dealer_turn(self):
        print(f"\nDealer's initial hand: {self.dealer.cards[0]}, Hidden Card")
        while self.dealer.calculate_total() < 17:
            self.dealer.add_card(self.deck.draw_card())
            print(f"Dealer's hand: {self.dealer}")
        if self.dealer.calculate_total() > 21:
            print("Dealer busts!")
            self.dealer_busted = True

    def compare_results(self):
        dealer_total = self.dealer.calculate_total()
        for i, hand in enumerate(self.players):
            player_total = hand.calculate_total()
            print(f"\nPlayer {i + 1}'s hand: {hand}")
            if player_total > 21:
                print(f"Player {i + 1} busts!")
            elif self.dealer_busted or player_total > dealer_total:
                print(f"Player {i + 1} wins!")
            elif player_total < dealer_total:
                print(f"Player {i + 1} loses!")
            else:
                print(f"Player {i + 1} ties with the dealer.")

    def play_game(self):
        self.deal_initial_cards()
        for i in range(len(self.players)):
            if not self.player_turn(i):
                continue
        if not self.dealer_busted:
            self.dealer_turn()
        self.compare_results()