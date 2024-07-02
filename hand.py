from scr.card import Card
from scr.deck import Deck
class Hand:
    def __init__(self):
        self.cards_hand = []

    def current_cards(self):
        for i in range (len(self.cards_hand)):
            print(f'{i+1}.{self.cards_hand[i]}')
    def add_card(self,card):
        self.cards_hand.append(str(card))

    def remove_card(self, card):
        return self.cards_hand.pop(card - 1)

    def one_card(self):
        if len(self.cards_hand) == 1:
            print("uno!")
    def no_cards(self):
        if len(self.cards_hand) == 0:
            print("game finished")