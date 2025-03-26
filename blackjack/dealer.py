class Dealer:
    def display_dealerHand(self, dealHand, dealSum, playerTurn):
        print("Dealer's hand: ")
        for c in dealHand:
            if playerTurn != "Dealer":
                if (c != len(dealHand) - 1):
                    print("The card is the " + c.get_card_face() + " of " + c.get_card_suit() + " with a value of " + str(c.get_card_value()))
                else:
                    print("The card is currenly hidden.")
            else:
                print("The card is the " + c.get_card_face() + " of " + c.get_card_suit() + " with a value of " + str(c.get_card_value()))
        if playerTurn == "Dealer":
            print("The sum of the cards is: " + str(dealSum))
        print("")