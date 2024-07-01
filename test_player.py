from scr.card import Card
from scr.hand import Hand
from scr.player import Player, AI

def test_create():
    cards = Card.load('r1 b7 g3')
    p = Player(name = 'Richard', hand = hand)

    assert p.name == 'Richard'
    assert p.hand == hand
    assert isinstance(p.actor, AI)

def test_repr():
    hand = Hand.load(cards)
    p = Player(name='Richard', hand=hand)
    assert repr(p) == 'Richard: r1 b7 g3'

def test_save():
    hand= Hand.load('r1 b7 g3')
    p = Player(name='Richard', hand=hand)
    dres = p.save()
    assert dres == {'name': 'Richard', 'hand': 'r1 b7 g3', 'is_human': False}

    p = Player(name='', hand=hand)
    dres = p.save()
    assert dres == {'name': 'John', 'hand': 'r1 b7 g3', 'is_human': True}
