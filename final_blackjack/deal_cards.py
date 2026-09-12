from random import choice

card_vals = ['a', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k']
suit_vals = ['s', 'h', 'd', 'c']

cards_dealt = []

def deal_card():
  while True:
    val = choice(card_vals)
    suit = choice(suit_vals)
    card = (val, suit)
    if card not in cards_dealt:
      cards_dealt.append(card)
      return card

def reset_deck():
   global cards_dealt
   cards_dealt = []
