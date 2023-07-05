# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck', 'draw_n']

# %% ../nbs/01_deck.ipynb 3
from .card import *
from fastcore.utils import *

# %% ../nbs/01_deck.ipynb 4
class Deck:
    "A deck of cards not including jokers"
    def __init__(self):
        self.cards = [Card(s, r) for s in range(4) for r in range(1,14)]
    def __len__(self):
        return len(self.cards)
    def __str__(self):
        return "; ".join(map(str, self.cards))
    def __contains__(self, card):
        return card in self.cards
    def shuffle(self):
        "Shuffle the cards in a deck"
        random.shuffle(self.cards)
    __repr__ = __str__

# %% ../nbs/01_deck.ipynb 13
@patch
def pop(self: Deck,
        idx :int = -1): # The index of the card to remove, defaulting to the last one
    "Remove one card from the deck"
    return self.cards.pop(idx)

# %% ../nbs/01_deck.ipynb 17
@patch
def remove(self: Deck,
        card: Card): # The card to remove
    "Remove card from the deck or raise exception if not present"
    return self.cards.remove(card)

# %% ../nbs/01_deck.ipynb 20
def draw_n(n:int, # Number of cards to draw
           replace: bool = True): # whether or not to draw with replacement
    d = Deck()
    d.shuffle()
    if replace:
        return [d.cards[random.choice(range(len(d.cards)))] for _ in range(n)]
    else:
        return d.cards[:n]
