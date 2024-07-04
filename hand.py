from card import Card


class Hand:
    def __init__(self, cards=None):
        if cards is None:
            cards=[]
        self.cards_hand = cards.copy()

    def __repr__(self):
        s = ' '.join(map(str, self.cards_hand))
        return s
    def add_card(self,card):
        self.cards_hand.append(card)

    def __eq__(self, other):
        print(self.cards_hand, other.cards_hand)
        print(self.cards_hand == other.cards_hand)
        return self.cards_hand == other.cards_hand

    @classmethod
    def load_card(cls, text: str):
            words = text.split()  # ['b2','y4','r7']
            cards = []
            for w in words:
                c = Card.load(w)
                cards.append(c)
            hand = Hand(cards=cards)
            return hand

    def remove_card(self, point):
        return self.cards_hand.remove(point)

    def last_card(self):
        if len(self.cards_hand) == 1:
            print("uno!")
    def no_cards(self):
        if len(self.cards_hand) == 0:
            print("game finished")
