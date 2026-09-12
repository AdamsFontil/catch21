from classes import Player, Players
from deal_cards import deal_card, reset_deck


def game_menu():
  print('you currently have # and the computer has #')
  while True:
    choice = str(input('what would you like to do: '))
    match choice:
      case 'h':
        print('h')
        break
      case 's':
        print('s')
        break
      case 'q':
        print('going back to main menu')
        break
      case _:
        print('error: please type h or s to continue the game or q to quit game')

player = Player('adams', 250)
house = Players('computer')

def play_round(player, house):
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
  else:
    print(f'The computer has {c_hand_val[0]} and you have {hand_val[0]} or {hand_val[1]}')




play_round(player, house)

# Function game_menu:
# prompt the user asking them what would they like to do next
# if they respond with ‘h’ or ‘hit’
# call_deal card for the player
# print you now have {player.hand_val}
# if player.hand_val > 21:
# print player lost
# reduces the player’s bank by the bet amount
# reset player.hand and house.hands to [ ]
# reset cards_dealt to [ ]
# set game_over to true
# else if player.hand_val = 21:
# print player won
# increases the player’s bank by the bet amount
# reset player.hand and house.hands to [ ]
# reset cards_dealt to [ ]
# set game_over to true
# else:
# call game_menu

# else if they respond with ‘s’ or ‘stay’
# call_deal card for the house
# if house.hand_val > 21:
# print player won
# increases the player’s bank by the bet amount
# reset player.hand and house.hands to [ ]
# reset cards_dealt to [ ]
# set game_over to true
# else if house.hand_val = 21:
# print player lost
# decreases the player’s bank by the bet amount
# reset player.hand and house.hands to [ ]
# reset cards_dealt to [ ]
# set game_over to true
# else:
# call game_menu
# else:
# tell user to choose (‘hit or stay’)

# Function play_round()
# while game_over is false
# for 4 rounds:
# if the round is odd:
# call the deal cards function and add the card to the player.hand
# else:
# call the deal cards function and add the card to the house.hand
# print player has this value, and computer has one val, where one card is hidden
# call the game_menu function
