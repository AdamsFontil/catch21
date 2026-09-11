from random import choices

card_vals = ['a', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k']
suit_vals = ['s', 'h', 'd', 'c']

cards_dealt = []

def deal_card():
  while True:
    val = choices(card_vals)
    suit = choices(suit_vals)
    card = (val, suit)
    print('suit', suit)
    print('val', val)
    if card not in cards_dealt:
      cards_dealt.append(card)
      return card

def reset_deck():
   global cards_dealt
   cards_dealt = []
