from random import choice


class Player1:
    def player1Name(name):
        print("Welcome to the game!")
        print("-----------------------------")
        name = input("Hello, Player 1! please enter your name: ")
        print("\033c", end="")
        return name

    def display_P1Hand(self, p1Name, p1Hand, p1Sum):
        print(p1Name + "'s hand: ")
        for c in p1Hand:
            print("The card is the " + c.get_card_face() + " of " + c.get_card_suit() + " with a value of " + str(c.get_card_value()))
        print("The sum of the cards is: " + str(p1Sum))
        print("")

    def uInput(self):
        playerMove = ""
        while True:
            playerMove = input("Do you want to hit or stay? Select either 'H' or 'S': ").upper()
            if playerMove == "H" or playerMove == "S":
                break
            else:
                print("Invalid input. Please enter 'H' to hit or 'S' to stay.")
                print("")
        return playerMove