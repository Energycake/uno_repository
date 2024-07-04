
class Hand:
    def __init__(self):
        self.cards_hand = []


    def current_cards(self):
        for i in range (len(self.cards_hand)):
            print(f'{i+1}.{self.cards_hand[i]}')

    def __repr__(self):
        s = ' '.join(map(str, self.cards_hand))
        return s
    def add_card(self,card):
        self.cards_hand.append(card)

    def __eq__(self, other):
        return self.cards_hand == other.cards

    
    def remove_card(self, point):
        return self.cards_hand.remove(point)

    def last_card(self):
        if len(self.cards_hand) == 1:
            print("uno!")
    def no_cards(self):
        if len(self.cards_hand) == 0:
            print("game finished")
