from main_menu_options import create_character, more_info, quit_game

def main_menu():
    option = str(input("what would you like to do today? 1. (P)lay 2. (M)ore info 3. (Q)uit: "))
    if option.lower() == 'p':
        while True:
            name = input('what is your name? ')
            if name == 'q':
                print('Going back to main menu')
                main_menu()
                break
            elif 3 <= len(name) <= 15:
                break
            print('error: name must be 3-15 characters, or type q to go back')

        while True:
            choice = input('how much would you like to deposit? ')
            if choice == 'q':
                print('Going back to main menu')
                main_menu()
                break
            try:
                deposit = int(choice)
            except ValueError:
                print('error: deposit must be a number')
                continue
            if 1 <= deposit <= 10000000:
                break
            print('error: deposit must be between 1 and 10,000,000')

        create_character(name, deposit)

    elif option.lower() == 'm':
      more_info() # this just prints info about the game it doesn’t manipulate or do any game logic
      print('m')
      main_menu()
    elif option.lower() == 'q':
       print('q')
       quit_game()
    else:
      print("error: selection not recognized, the only options are to play, view more info, or quit the program please type an appropriate input")
      main_menu()
