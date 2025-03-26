import random
from card import Card

class DeckOfCards:
    def __init__(self, shuffle):
        self.suits = 4
        self.cards = 13
        self.suitChars = ['D', 'H', 'S', 'C']
        self.cardFaces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.deckOfCards = []

        self.generate_deck()
        if shuffle:
            self.shuffle_deck()

    def generate_deck(self):
        for x in range(self.suits):
            for y in range(self.cards):
                value = y + 1
                if value > 10:
                    value = 10
                self.deckOfCards.append(Card(value, self.suitChars[x], self.cardFaces[y]))

    def display_deck(self):
        for c in self.deckOfCards:
            print(f"The Card is the {c.get_card_face()} of {c.get_card_suit()} with a value of {c.get_card_value()}")

    def shuffle_deck(self):
        temp1 = list(self.deckOfCards)
        temp2 = []
        shuffleCount = 7

        while shuffleCount > 0:
            while len(temp1) > 0:
                temp3 = random.randint(0, len(temp1) - 1)
                temp2.append(temp1[temp3])
                temp1.pop(temp3)

            temp1 = list(temp2)
            temp2 = []

            shuffleCount -= 1

        self.deckOfCards = list(temp1)

    def draw_a_card(self):
        drawnCard = self.deckOfCards[0]
        self.deckOfCards.pop(0)
        return drawnCard

    def draw_cards(self, number):
        drawnCards = []

        for x in range(number):
            drawnCards.append(self.draw_a_card())

        return drawnCards
