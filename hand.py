from scr.card import Card
from scr.deck import Deck
class Hand:
    def __init__(self):
        self.cards_hand = []
        self.cards_hand_text = []

    def current_cards(self):
        for i in range (len(self.cards_hand_text)):
            print(f'{i+1}.{self.cards_hand[i]}')
    def add_card(self,card):
        self.cards_hand.append(card)
        self.cards_hand_text.append(str(card))
    def select_card(self, point):
        point =

    def remove_card(self, point):
        self.cards_hand_text.pop(point)
        return self.cards_hand.pop(point)

    def last_card(self):
        if len(self.cards_hand) == 1:
            print("uno!")
    def no_cards(self):
        if len(self.cards_hand) == 0:
            print("game finished")