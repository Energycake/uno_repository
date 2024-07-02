from scr.card import Card
from scr.hand import Hand
from scr.player import Player, AI, Human


def test_create():
    hand = Hand.load('r1 b7 g3')
    p = Player(name='John', hand=hand)

    assert p.name == 'John'
    assert p.hand == hand
    assert isinstance(p.actor, AI)

def test_repr():
    hand = Hand.load('r1 b7 g3')
    p = Player(name='John', hand=hand)
    assert repr(p) == 'John: r1 b7 g3'

def test_save():
    hand = Hand.load('r1 b7 g3')
    p = Player(name='John', hand=hand)
    dres = p.save()
    assert dres == {'name': 'John', 'hand': 'r1 b7 g3', 'is_human': False}

    p = Player(name='Richard', hand=hand, is_human=True)
    dres = p.save()
    assert dres == {'name': 'Richard', 'hand': 'r1 b7 g3', 'is_human': True}

def test_AI_choose_card():
    hand = Hand.load('r1 b7 g3')
    p = Player(name='John', hand=hand)
    # первую из нескольких
    top = Card('green', 7)
    card = p.actor.choose_card(hand=hand, top=top, card_counts=[len(p.hand.cards), 3, 4])
    assert repr(card) == 'b7'

    # одну
    top = Card('yellow', 1)
    card = p.actor.choose_card(hand=hand, top=top, card_counts=[len(p.hand.cards), 3, 4])
    assert repr(card) == 'r1'

    # ни одной
    top = Card('yellow', 5)
    card = p.actor.choose_card(hand=hand, top=top, card_counts=[len(p.hand.cards), 3, 4])
    assert card is None

def test_Human_choose_card():
    import sys
    stdin = sys.stdin
    with open('human_input_data', 'r') as fin:
        sys.stdin = fin
        # ....
    sys.stdin = stdin
