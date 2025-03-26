class Card:
    def __init__(self, value, suit, faceValue):
        self.value = value
        self.suit = suit
        self.faceValue = faceValue

    def get_card_value(self):
        return self.value

    def get_card_suit(self):
        suit = ""
        if self.suit == 'D':
            suit = "Diamond"
        elif self.suit == 'H':
            suit = "Heart"
        elif self.suit == 'S':
            suit = "Spade"
        elif self.suit == 'C':
            suit = "Clubs"
        return suit

    def get_card_face(self):
        face = self.faceValue
        if face == "A":
            face = "Ace"
        elif face == "J":
            face = "Jack"
        elif face == "Q":
            face = "Queen"
        elif face == "K":
            face = "King"
        return face