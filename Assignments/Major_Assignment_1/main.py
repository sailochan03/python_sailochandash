from blackjack import BlackjackGame

def main():
    while True:
        try:
            num_players = int(input("Enter number of players: "))
            if num_players > 0:
                break
            else:
                print("Number of players must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    game = BlackjackGame(num_players)
    game.play_game()

if __name__ == "__main__":
    main()