from _strings import get_guesses
from type_safety import type_check, options_1_to_
from random import choices
from time import sleep
from os import system, name

def clear_screen():
  print('\r')
  if name != 'nt':
    system('clear')
  if name != 'posix':
    system('cls')

class MemoryGame:
  __slots__ = ('difficulty', '_secret')

  @type_check
  def __init__(self, difficulty: int):
    self.difficulty = difficulty

  def generate_sequence(self):
    self._secret = tuple(choices(range(1, 102), k=self.difficulty))

  def get_list_from_user(self):
    return tuple(
      options_1_to_(101, get_guesses.format(i, self.difficulty))
      for i in range(1, 1+self.difficulty)
    )
  
  def is_list_equal(self, listA, listB):
    # return isEqual
    if len(listA) != len(listB):
      return False
    return all(a == b for a, b in zip(listA, listB))

  def play(self):
    self.generate_sequence()
    print("secret:", *self._secret, end='', flush=True)
    sleep(0.7)
    clear_screen()
    
    guesses = self.get_list_from_user()
    # return True if lost(nonEqual), False if won(equal)
    return not self.is_list_equal(guesses, self._secret)
  