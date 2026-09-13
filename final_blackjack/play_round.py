from classes import Player, Players
from deal_cards import deal_card, reset_deck


def game_logic(player,house,bet):
  print('hello game logic')
  for i in range(4):
    if i % 2 == 0:
      draw_card(house)
    else:
      draw_card(player)

  print('c hand', house.hand)
  print('c hand2', house.hand[:1])
  print('p hand', player.hand)

  p_hand_val = player.hand_val(player.hand)
  c_hand_val = house.hand_val(house.hand[:1])

  for i in range(15):
    p_hand_val = player.hand_val(player.hand)
    if p_hand_val[0] == 21 or p_hand_val[1] == 21:
      print('p hand is', p_hand_val)
      print('player has won!!!')
      break
    elif p_hand_val[0] != p_hand_val[1] and p_hand_val[1] <= 21:
      print(f'1computer has {c_hand_val} and you have {p_hand_val[0]} or {p_hand_val[1]}')
    elif p_hand_val[0] > 21:
      print('p hand is', p_hand_val)
      print('player has lost')
      break
    else:
      print(f'2computer has {c_hand_val} and you have {p_hand_val[0]}')
      print('p hand is', p_hand_val)

    choice = str(input('please type to (h)it, (s)tay or (q)uit to continue : '))
    match choice:
      case 'h':
        draw_card(player)
      case 's':
        print('s')
      case 'q':
        print('quit')
        break




  # while blackjack != True :
  #   # if player.hand[0] > 21:
  #   #   print('player lost')
  #   #   player.withdraw(bet)
  #   #   break
  #   choice = str(input('please type to (h)it, (s)tay or (q)uit to continue : '))
  #   match choice:
  #     case 'h':
  #       hand = p_turn(player, house)
  #       if hand[0] > 21:
  #         print('lost', hand)
  #         player.withdraw(bet)
  #         break
  #       elif hand[0] == 21 or hand[1] == 21:
  #         print('win', hand)
  #         player.deposit(bet)
  #         break
  #     case 's':
  #       while True:
  #         outcome = c_turn(player, house, bet)
  #         if outcome == 'p_lost' or outcome == 'p_win':
  #           break
  #     case 'q':
  #       print('going back to main menu')
  #       break
  #     case _:
  #       print('error: please type h or s to continue the game or q to quit game')

player = Player('adams', 250)
house = Players('computer')

def play_first_round(player, house, bet):
  for i in range(4):
    if i % 2 == 0:
      c_draw = deal_card()
      house.hand.append(c_draw)
    else:
      p_draw = deal_card()
      player.hand.append(p_draw)

  c_hand_val = house.hand_val(house.hand[:1])
  hand_val = player.hand_val(player.hand)
  if hand_val[0] == hand_val[1] or hand_val[1] > 21:
    print(f'The computer has {c_hand_val[0]} and you have {hand_val[0]}')
  elif hand_val[0] ==21 or hand_val[1] == 21:
    print(f'The computer has {c_hand_val[0]} and you have {hand_val[1]}')
    print('p hand', player.hand)
    print(f'you got blackjack!!!')
    player.deposit(bet)
    return True
  else:
    print(f'The computer has {c_hand_val[0]} and you have {hand_val[0]} or {hand_val[1]}')

def p_turn(player, house):
    p_draw = deal_card()
    player.hand.append(p_draw)
    c_hand_val = house.hand_val(house.hand[:1])
    hand_val = player.hand_val(player.hand)
    print(f'hand val', hand_val)
    print('p hand', player.hand)
    if hand_val[0] == hand_val[1] or hand_val[1] > 21:
      print(f'The computer has {c_hand_val[0]} and you have {hand_val[0]}')
      return hand_val
    else:
      print(f'The computer has {c_hand_val[0]} and you have {hand_val[0]} or {hand_val[1]}')
      return hand_val

def c_turn(player, house,bet):
    c_draw = deal_card()
    house.hand.append(c_draw)
    c_hand_val = house.hand_val(house.hand)
    hand_val = player.hand_val(player.hand)
    print(f'c_hand val', c_hand_val)
    print('c hand', house.hand)
    if c_hand_val[0] == c_hand_val[1] or c_hand_val[1] > 21:
      print(f'The computer has {c_hand_val[0]} and you have {hand_val[0]}')
    if c_hand_val[0] == 21 or c_hand_val[1] == 21:
      print('computer has blackjack, you lost')
      player.withdraw(bet)
      return 'p_lost'
    if c_hand_val[0] > 21:
      print('computer has busted, you won')
      player.deposit(bet)
      return 'p_win'
    else:
      print(f'you have {hand_val[0]} and computer has {c_hand_val[0]} or {c_hand_val[1]}')


def draw_card(player):
    card = deal_card()
    player.hand.append(card)





game_logic(player, house, 100)



#play round, takes player returns hand_val?
