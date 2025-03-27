import time
from winsound import PlaySound

class GameState:
    def initialize_message(self, p1Name):
        print(f"Hello, {p1Name}! The game will start in a while...")
        print("Initializing deck...")
        time.sleep(2.5)
        print("Initializing players...")
        time.sleep(2.5)
        print("Drawing cards for the players...")
        time.sleep(2.5)
        print("\033c", end="")


    def player_hand(self, cardHand):
        playerHand = cardHand.pop(0)
        return playerHand

    def card_sum(self, cardHand):
        playerSum = 0
        for x in range(len(cardHand)):
            playerSum += cardHand[x].get_card_value()
        return playerSum

    def hit_or_stand(self, playerSum, player):
        playerMove = "" 
        if playerSum > 16:
            playerMove = "S"
        else:
            playerMove = "H"
        print(f"\n{player} is thinking...")
        time.sleep(3)
        return playerMove

    def check_player_state(self, playerSum):
        winFlag = True
        if playerSum > 21:
            winFlag = False
        return winFlag 

    #checks if card valuis over 21
    def check_21_win(self, p1Sum, dealSum, players):
        winner = ""
        if p1Sum == 21:
            winner = players[0]
        elif dealSum == 21:
            winner = players[1]
        return winner

    #checks if card value is greater than other player's card value
    def compare_player_values(self, p1Sum, dealSum, players):
        winner = ""
        if p1Sum > dealSum:
            winner = players[0]
        elif dealSum > p1Sum:
            winner = players[1]
        elif p1Sum == dealSum:
            winner = "None"
        return winner