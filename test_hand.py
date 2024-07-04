from card import Card
from hand import Hand


def test_init():
    lst = Hand()
    assert lst.cards_hand == []

def test_repr():
    lst = Hand()
    lst.cards_hand.append(Card('r', 6))
    lst.cards_hand.append(Card('g', 4))
    assert repr(lst) == 'r6 g4'

def test_add():
    lst = Hand()
    c1 = Card('r', 6)
    lst.add_card(c1)
    c2 = Card('g', 4)
    lst.add_card(c2)
    c3 = Card('y', 2)
    lst.add_card(c3)

    assert lst.cards_hand[0] == Card('r', 6)
    assert lst.cards_hand[1] == Card('g', 4)
    assert lst.cards_hand[2] == Card('y', 2)
