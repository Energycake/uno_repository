import random
from scr.card import Card
from scr.deck import Deck

card_list = [Card('blue', 2), Card('yellow', 4), Card('red', 7)]

def test_create():
    deck = Deck(cards = card_list)
    assert deck.cards[0] == card_list


def test_repr():
    deck = Deck(cards = card_list)
    assert repr(deck) = 'b2 y4 r7'

def test_load():
    deck = Deck.load('b2 y4 r7')
    #assert repr(deck) == 'b2 y4 r7'
    assert deck.cards == card_list

def test_draw_card():
    deck = Deck(cards = card_list)
    c = deck.draw_card()
    assert str(c) == 'y4'
    assert str(deck) == 'b2 r7'

def test_shuffle():
    random.seed(7)
    deck = Deck.load('y2 y6 b3 b5 b1 g4 g6 g1 g2 r0')
    deck.shuffle()
    print(deck)
    deck.shuffle()
    print(deck)
    deck.shuffle()
    print(deck)
    deck.shuffle()
    print(deck)