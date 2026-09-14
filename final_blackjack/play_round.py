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

  c_hand_val = house.hand_val(house.hand[:1])
  blackjack = determine_winner(player, house, c_hand_val)
  print('blackjack', blackjack)
  if blackjack:
    print(f'{player.name} won!!!')
    player.deposit(bet)

  while blackjack == None:
    choice = str(input('please type to (h)it, (s)tay or (q)uit to continue : '))
    match choice:
      case 'h':
        draw_card(player)
        winner = determine_winner(player, house, c_hand_val)
        print('winner is ', winner)
        if winner == player.name:
          print('you won!!!')
          player.deposit(bet)
          break
        elif winner == house.name:
          print('busted')
          player.withdraw(bet)
          break
      case 's':
        print('s')
        c_blackjack = determine_winner(house, player, player.hand_val(player.hand))
        print('cblackjack',c_blackjack)
        while c_blackjack == None:
          draw_card(house)
          winner = determine_winner(house, player, player.hand_val(player.hand))
          print('winner is ', winner)
          if winner == player.name:
            print('you won!!!')
            player.deposit(bet)
            break
          elif winner == house.name:
            print('busted')
            player.withdraw(bet)
            break
        break
      case 'q':
        print('quit')
        break
      case _:
        print('error: command not recognized')

def determine_winner(player, opponent, op_hand_val):
      hand_val = player.hand_val(player.hand)
      if hand_val[0] == 21 or hand_val[1] == 21:
        print(f'{player.name} hand is', hand_val)
        print(f'{player.name} have won!!!')
        return player.name
      elif hand_val[0] != hand_val[1] and hand_val[1] <= 21:
        print(f'{opponent.name} has {op_hand_val} and {player.name} have {hand_val[0]} or {hand_val[1]}')
      elif hand_val[0] > 21:
        print(f'{player.name} hand is', hand_val)
        print(f'{player.name} has lost')
        return opponent.name
      else:
        print(f'{opponent.name} has {op_hand_val} and {player.name} have {hand_val[0]}')
        print(f'{player.name} hand is', hand_val)

player = Player('adams', 250)
house = Players('computer')

def draw_card(player):
    card = deal_card()
    player.hand.append(card)

game_logic(player, house, 100)
