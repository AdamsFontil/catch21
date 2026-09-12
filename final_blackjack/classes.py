class Players:
  def __init__(self, name):
    self.name = name
    self.hand = []

  def hand_val(self, arrayOfCards):
    if not arrayOfCards:
      print('error: please provide a deck')
      return
    hand_val = [0, 0]
    for val in arrayOfCards:
      if val in ('j', 'q', 'k'):
        hand_val = [hand_val[0] + 10, hand_val[1] + 10]
      elif val == 'a':
        hand_val = [hand_val[0] + 1, hand_val[1] + 11]
      else:
        n = int(val)
        hand_val = [hand_val[0] + n, hand_val[1] + n]
    if hand_val[0] == hand_val[1] or hand_val[1] > 21:
      print(f'{self.name} has {hand_val[0]}')
    else:
      print(f'{self.name} has {hand_val[0]} or {hand_val[1]}')

  def reset_hand(self):
      self.hand = []

class Player(Players):
  def __init__ (self, name, deposit):
    super().__init__(name)
    self.bank = deposit

  def deposit(self, amount):
    if type(amount) != int or not (0 < amount <= 10000000):
      print('error: amount must be an integer between 0 and 10,000,000')
    else:
      self.bank += amount
      print(f'sucessly deposited {amount} you now have {self.bank}')

  def withdraw(self, amount):
    if type(amount) != int or not (0 < amount <= 10000000):
      print('error: amount must be an integer between 0 and 10,000,000')
    elif amount > self.bank:
      print(f'error: cannot withdraw more than you have. Your bank {self.bank} is less than the {amount} amount')
    else:
      self.bank -= amount
      print(f'sucessly withdrew {amount} you now have {self.bank}')
