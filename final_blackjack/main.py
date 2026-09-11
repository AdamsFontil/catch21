import main_menu as main

def start_game():
    print("welcome to Blackjack.py a fun interactive casino game that you can play via your terminal!")
    main.main_menu()

start_game()


# Function deal_cards, takes no input:
# create cards_dealt to keep track of the cards already dealt.
# Create deal_val to randomly output a number from 1 – 13, 1 represents ace, 11-13 are the face cards(jack,queen, king)
# create deal_suit to randomly outputs a number from 0-3, representing each suit in a deck
# create card_dealt function (deal_val, deal_suit) returns a tuple of card val and their suit

# while card_dealt is in the cards_dealt(history of cards dealt) and cards_dealt is not empty
# repeatedly call card_dealt until a unique card is dealt
# else:  if unique card found then append it to the cards_dealt and return that unique combo to the function that called it

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
