class Dealer:
    def display_dealerHand(self, dealHand, dealSum, playerTurn):
        print("Dealer's hand: ")
        for x in range(len(dealHand)):
            if playerTurn != "Dealer":
                if (x != len(dealHand) - 1):
                    print("The card is the " + dealHand[x].get_card_face() + " of " + dealHand[x].get_card_suit() + 
                          " with a value of " + str(dealHand[x].get_card_value()))
                else:
                    print("The card is currenly hidden.")
            else:
                print("The card is the " + dealHand[x].get_card_face() + " of " + dealHand[x].get_card_suit() + 
                      " with a value of " + str(dealHand[x].get_card_value()))
        if playerTurn == "Dealer":
            print("The sum of the cards is: " + str(dealSum))
        print("")