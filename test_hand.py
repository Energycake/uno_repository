from scr.card import Card
from scr.hand import Hand
def test_init():
    lst = Hand()
    assert lst.cards == []
def test_repr():
    lst = Hand()
    lst.cards.append(Card('r', 6))
    lst.cards.append(Card('g', 4))
    assert repr(lst) == 'r6 g4'
def test_add():
    lst = Hand()
    c = Card('r', 6)
    lst.add(c)
    c = Card('g', 4)
    lst.add(c)
    c = Card('y', 2)
    lst.add(c)

    assert lst.cards[0] == Card('r', 6)
    assert lst.cards[1] == Card('g', 4)
    assert lst.cards[2] == Card('y', 2)