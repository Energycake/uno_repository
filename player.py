class Human:
    """Взаимодействие с человеком"""
    pass
class AI:
    """AI interaction"""

    def choose_card(self, hand: Hand, top: Card, card_counts: list[int]) -> Card | None:
        """Выбирает первую подходящую карту, иначе None"""
        # random.choose
        cards = hand.playable_cards(top)
        ##FROM HAND.PY
        cards =[]
        for c in hand.cards:
            if top.playable(c):
                cards.append(c)
       cards = [c for c in hand.cards if top.playable(c)]
       # if cards: #bool([])
       #     return None
       # else:
       #     return cards[0]
        return cards[0] if cards else None
        ##FROM HAND.PY


class Player:
    def __init__(self, name: str, hand: Hand = None, is_human: bool = False):
        self.hand = hand or Hand()
        self.name = name
        if is_human:
            self.actor = Human()
        else:
            self.actor = AI()

    def __repr__(self):
        return f'{self.name}:{self.hand}'

    def to_dict(self):
        return {
            'name': self.name,
            'hand': self.hand.save()
            'is_human': isinstance(self.actor, Human)
        }

    @classmethod
    def from_dict(cls, data: dict):
        """параметр data: = {
        "name": "Alex
        hand: "r3 y5 g4 g1"
        "is_human" true"
        }
        return: Player
        """

        return cls(name=data['name'], hand=Hand.load(data['hand']), is_human = data['is_human'])

    def save(self):
        return self.to_dict()

    @classmethod
    def load(cls, text):
        return cls.from_dict(data)

    def choose_card(self, top:Card, card_counts: list[int]):
        return self.actor.choose_card(self.hand, top, card_counts)

