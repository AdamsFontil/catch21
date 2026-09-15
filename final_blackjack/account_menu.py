import main_menu_options
from play_round import game_logic

def account_menu(player, house):
  print('Welcome to the account menu!')
  while True:
    choice = str(input('type (v)iew account, make a (d)eposit, (p)lace a bet, (w)ithdraw funds, (q)uit program: '))
    match choice:
      case 'v':
        print(f'{player.name} has ${player.bank} in their bank')
      case 'd':
        while True:
          try:
            amount = int(input('how much would you like to deposit? '))
            if not (0 < amount <= 10000000):
              print('error: amount must be an integer between 0 and 10,000,000')
            else:
              player.deposit(amount)
              break
          except ValueError:
            print('pls type a number')
      case 'p':
        print('playing round...')
        while True:
          try:
            bet = int(input('How much would you like to bet? : '))
            if bet > player.bank:
              print(f'cannot bet more than you have. you have {player.bank} and you are betting {bet}.')
              print('please place a lower bet, or make a deposit')
              break
            elif bet < 0 or type(bet) != int:
              print('error: please place a bet that is a number greater than 0')
            else:
              game_logic(player, house, bet)
              break
          except ValueError:
            print('pls type a number')
      case 'w':
        while True:
          try:
            amount = int(input('how much would you like to withdraw? '))
            if not (0 < amount <= 10000000):
              print('error: amount must be an integer between 0 and 10,000,000')
            elif amount > player.bank:
              print(f'error: cannot withdraw more than you have. Your bank {player.bank} is less than the {amount} amount')
            else:
              player.withdraw(amount)
              break
          except ValueError:
            print('pls type a number')
      case 'q':
        print('quitting program')
        main_menu_options.quit_game()
        break

      case _:
        print('invalid input: please v, d, p, w or q to continue')
