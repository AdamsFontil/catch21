from deal_cards import deal_card, reset_deck


def game_logic(player,house,bet):
  for i in range(4):
    if i % 2 == 0:
      draw_card(house)
    else:
      draw_card(player)
  c_hand_val = house.hand_val(house.hand[:1])
  blackjack = determine_winner(player, house, c_hand_val[0])
  if blackjack:
    read_card(player.hand, player)
    print(f'{player.name} got blackjack!!!')
    player.deposit(bet)
  while blackjack == None:
    read_card(player.hand, player)
    choice = str(input('please type to (h)it, (s)tay or (q)uit to continue : '))
    match choice:
      case 'h':
        draw_card(player)
        read_card(player.hand, player)
        winner = determine_winner(player, house, c_hand_val[0])
        if winner == player.name:
          print('you won!!!')
          player.deposit(bet)
          break
        elif winner == house.name:
          print('you busted')
          player.withdraw(bet)
          break
      case 's':
        print('s')
        c_blackjack = determine_winner(house, player, player.hand_val(player.hand))
        print('cblackjack',c_blackjack)
        while c_blackjack == None:
          draw_card(house)
          read_card(house.hand, house)
          winner = determine_winner(house, player, player.hand_val(player.hand))
          if winner == player.name:
            print('house busted, you won!!!')
            player.deposit(bet)
            break
          elif winner == house.name:
            print('house won')
            player.withdraw(bet)
            break
        break
      case 'q':
        print('quit')
        break
      case _:
        print('error: command not recognized')
  print('reseting!!!!')
  reset_deck()
  player.reset_hand()
  house.reset_hand()
  print('p at end', player.hand)
  print('h at end', house.hand)


def determine_winner(player, opponent, op_hand_val):
      hand_val = player.hand_val(player.hand)
      if hand_val[0] == 21 or hand_val[1] == 21:
        return player.name
      elif hand_val[0] != hand_val[1] and hand_val[1] <= 21:
        print(f'{opponent.name} has {op_hand_val} and {player.name} have {hand_val[0]} or {hand_val[1]}')
      elif hand_val[0] > 21:
        return opponent.name
      else:
        print(f'{opponent.name} has {op_hand_val} and {player.name} have {hand_val[0]}')

def draw_card(player):
    card = deal_card()
    player.hand.append(card)


def read_card(list, player):
  print(f'{player.name}, your cards are: ', end='')
  for item in list:
    print(f'|{item[0]} of {item[1]}|', end=' ')
  print()
