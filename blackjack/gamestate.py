import time

class GameState:
    def initialize_message(self, p1Name):
        print(f"Hello, {p1Name}! The game will start in a while...")
        print("Initializing deck...")
        time.sleep(2.5)
        print("Initializing players...")
        time.sleep(2.5)
        print("Drawing cards for the players...")
        time.sleep(2.5)
        print("")

    def player_hand(self, cardHand):
        playerHand = cardHand.pop(0)
        return playerHand

    def card_sum(self, cardHand):
        playerSum = 0
        for x in range(len(cardHand)):
            playerSum += cardHand[x].get_card_value()
        return playerSum

    def hit_or_stand(self, playerSum, player):
        choice = "S" if playerSum > 16 else "H"
        print(f"\n{player} is thinking...")
        time.sleep(3)
        return choice

    def check_player_state(self, playerSum):
        return playerSum <= 21

    def check_21_win(self, p1Sum, dealSum, players):
        winner = ""
        if p1Sum == 21:
            winner = players[0]
        elif dealSum == 21:
            winner = players[1]
        return winner

    def compare_player_values(self, p1Sum, dealSum, players):
        winner = ""
        if p1Sum > dealSum:
            winner = players[0]
        elif dealSum > p1Sum:
            winner = players[1]
        elif p1Sum == dealSum:
            winner = "None"
        return winner