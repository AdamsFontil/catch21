import main_menu_options
from play_round import play_round

def account_menu(player, house):
  print('Welcome to the account menu here you 1. view your account (b)alance, 2.(d)eposit funds, 3.(p)lay a round of blackjack, 4.(w)ithdraw funds,  5.(q)uit game')
  while True:
    choice = str(input('what would you like to do: '))
    match choice:
      case 'b':
        print(f'{player.name} has {player.bank}')
        account_menu(player)
      case 'd':
        while True:
          amount = int(input('how much would you like to deposit? '))
          if type(amount) != int or not (0 < amount <= 10000000):
            print('error: amount must be an integer between 0 and 10,000,000')
          else:
            player.deposit(amount)
            account_menu(player)
      case 'p':
        print('playing round...')
        play_round(player, house)
        break
      case 'w':
        while True:
          amount = int(input('how much would you like to withdraw? '))
          if type(amount) != int or not (0 < amount <= 10000000):
            print('error: amount must be an integer between 0 and 10,000,000')
          elif amount > player.bank:
            print(f'error: cannot withdraw more than you have. Your bank {player.bank} is less than the {amount} amount')
          else:
            player.withdraw(amount)
            account_menu(player)
      case 'q':
        print('quitting program')
        main_menu_options.quit_game()
        break

      case _:
        print('error: please type h or s to continue the game or q to quit game')
