class Card:
    colors=('red','green','blue','yellow')
    numbers=list(range(10))+ list (range(1, 10))
    dcolors={color[0]: color for color in colors}
    def __init__(self, color: str, number: int):
        self.color=color
        self.number=number

    def __eq__(self, other):
        # TODO заглушка
        return True

    def __repr__(self):
        letter=self.color[0]
        return f'{letter}{self.number}'

    @classmethod
    def load(cls, text: str):
        """создает карту из строки вида 'y8' и возвращает её """
        #text = 'y8'
        letter = text[0]    #'y'
        number = text[1]    #'8'
        color=cls.dcolors[letter]
        card=Card(color, int(number))
        return card

    def playable(self, other):#можно ли играть карту?
        if self.color == other.color or self.number == other.number:
            return True
        else:
            return self.color == other.color or self.number == other.number
    @staticmethod
    def all_cards():
        """Возвращает все карты
        :param colors:
        :param numbers:"""


        cards = []
        for col in colors:
            for i in numbers:
                c= Card(col, i)
                cards.append(c)
        return cards
        #return[Card(col, i) for col in colors for i in numbers]