import sys
from classes import Player, Players

def player_menu():
  pass

def quit_game():
  print('thanks for playing our game. See you next time!')
  sys.exit

def more_info():
    print('Blackjack.py manual: The objective is to get as close to 21 as possible without going over, create a player, place bets, and try to win some money.')
    print('If you run out of money go to the player menu and deposit more funds into your account')
    print('Once you are satisfied with your earnings you may withdraw as money as your bank allows')
    print('Follow the prompts carefully, play logically and press q at anytime (except for when a blackjack round is in session) to quit program')
    print('Lastly the expected inputs are 1 character long for commands, and sometimes a numeric value is required for deposits and withdrawls, and a string for giving your player a name')
    print('The expected commands are the ones between the parantheses for in (P)lay press p is correct command to start the game')

def create_character(name, deposit):
  player = Player(name, deposit)
  house = Players('house')
  print(f'sucess: {name} created and {deposit} added')
  print('what is player', player)
  print('what is house', house)
  print(f'welcome {player.name} you have successfully deposited {deposit} into your account. You now have {player.bank} USD to play with. Have fun!')
  player.hand_val(['a', 'j', 1])
  player.hand_val([7, 'a', 1])
  player.hand_val([])
  player_menu()
