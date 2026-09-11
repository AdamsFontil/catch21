import main_menu as main

def start_game():
    print("welcome to Blackjack.py a fun interactive casino game that you can play via your terminal!")
    main.main_menu()

start_game()




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
