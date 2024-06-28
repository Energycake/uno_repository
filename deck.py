class Deck:
    """Колода карт уно"""
    def __init__(self, cards=None):
        if cards is None:
            cards=[]
        #cards = cards or []
    self.cards = cards.copy()
    def __repr__(self):
    s = ' '.join(map(str, self.cards))
    return s

    def save(self):
        return repr(self)

    @classmethod
    def load(cls, text:str):
        """Из строки вида 'b2 y4 r7' возвращает колоду"""
        text = 'b2 y4 r7'
        words = text.split()    #['b2','y4','r7']
        cards=[]
        for w in words:
            c = Card.load(w)
            cards.append(c)

        #cards=[Card.load(w) for w in words]

        deck = Deck(cards=cards)
        return deck

    def draw_card(self):
        """Берем карту из колоды (ее там больше нет) и возвращаем ее"""
        c =self.cards.pop(0)
        return c
    def shuffle(self):
        """перемешиваем колоду"""
        random.shuffle(self.cards)