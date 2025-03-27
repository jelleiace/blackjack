##PROG FLOW
#main menu: insert player name to start
#ini deck [DONE]
#ini player1, cpu player 2, dealer [DONE]
#draw 1 card for p1, p2, dealer (ALL SHOW) [DONE]
#draw 1 more card for p1, p2, dealer (dealer only: hidden) [DONE]
#ask each player to hit/stand [DONE]
#  if hit:
#  -draw card [DONE]
#  -get card sum [DONE]
#  -go back to asking the player [DONE]
#FOR HIT LOGIC
#create a checker for comparing card sum total [DONE]

#  if stand:
#  -move on to next player [DONE]
#once p1 and p2 are done, reveal dealer card [DONE]
#dealer will also hit/stand [DONE]
#display game winners and losers
import time
import sys
from player1 import Player1
from dealer import Dealer
from deckofcards import DeckOfCards
from gamestate import GameState

def main():
    #initialize game
    p1 = Player1()
    d = Dealer()
    doc = DeckOfCards(True)
    gs = GameState()

    p1Name = p1.player1Name()

    #drawing cards for each player
    startCount = 0
    p1Hand = []
    dealerHand = []
    hand = doc.draw_cards(4) #value of 4 came from: 2 players * 2 bc each player needs 2 cards
    while startCount < 2:
        p1Hand.append(gs.player_hand(hand))
        dealerHand.append(gs.player_hand(hand))
        startCount += 1

    #start game
    gs.initialize_message(p1Name)
    playerTurn = [p1Name, "Dealer"]
    moveHistory = []
    playerMove = ""
    x = 0
    p1Sum = 0
    dealerSum = 0
    currPlayerSum = 0
    checkAgain = True
    winFlag = True

    while x < len(playerTurn):
        p1Sum = gs.card_sum(p1Hand)
        dealerSum = gs.card_sum(dealerHand)

        #display players' hands
        p1.display_P1Hand(playerTurn[0], p1Hand, p1Sum)
        d.display_dealerHand(dealerHand, dealerSum, playerTurn[x])

        if len(moveHistory) != 0:
            print(moveHistory[len(moveHistory) - 1])
        print("-----------------------------------------------")

        #check player and game state
        if not gs.check_player_state(currPlayerSum):
            print(f"{playerTurn[x]} busted!")
            checkAgain = False
            break

        for i in range(len(playerTurn)):
            if gs.check_21_win(p1Sum, dealerSum, playerTurn) == playerTurn[i]:
                print(f"{playerTurn[i]} won!")
                checkAgain = False
                winFlag = False
                break

        if not winFlag:
            break

        # Choose which player and ask H/S
        print(f"{playerTurn[x]}, would you like to hit or stand?")

        if x == 0:
            playerMove = p1.uInput()
        elif x == 1:
            playerMove = gs.hit_or_stand(gs.card_sum(dealerHand), playerTurn[x])

        # H/S logic
        if playerMove == "H":
            hand = doc.draw_cards(1)

            if x == 0:
                p1Hand.append(gs.player_hand(hand))
                currPlayerSum = gs.card_sum(p1Hand)
            elif x == 1:
                dealerHand.append(gs.player_hand(hand))
                currPlayerSum = gs.card_sum(dealerHand)

            moveHistory.append(f"{playerTurn[x]} decided to hit.")

        elif playerMove == "S":
            moveHistory.append(f"{playerTurn[x]} decided to stand.")
            x += 1
            playerMove = ""
        
        print("\033c", end="")

    while checkAgain: #scenario: no one went over 21 and no one won yet
        # Display player's hand
        p1.display_P1Hand(playerTurn[0], p1Hand, gs.card_sum(p1Hand))
        d.display_dealerHand(dealerHand, gs.card_sum(dealerHand), playerTurn[len(playerTurn) - 1])

        if moveHistory:
            print(moveHistory[len(moveHistory) - 1])
        print("-----------------------------------------------")

        for i in range(len(playerTurn)):
            if gs.compare_player_values(gs.card_sum(p1Hand), gs.card_sum(dealerHand), playerTurn) == playerTurn[i]:
                print(f"{playerTurn[i]} won!")
                break
            if gs.compare_player_values(p1Sum, dealerSum, playerTurn) == "None":
                print("Push!")
                checkAgain = False
                break

        checkAgain = False

    sys.exit()

if __name__ == "__main__":
    main()