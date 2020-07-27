from _strings import get_guesses
from type_safety import options_1_to_
from random import choices
from time import sleep
from Utils import screen_cleaner

# self is difficulty
class MemoryGame(int):

  def generate_sequence(difficulty):
    return tuple(choices(range(1, 102), k=difficulty))

  def get_list_from_user(difficulty):
    return tuple(
      options_1_to_(101, get_guesses.format(i, 101))
      for i in range(1, 1+difficulty)
    )

  @staticmethod
  def is_list_equal(listA, listB):
    # return isEqual
    if len(listA) != len(listB):
      return False
    return all(a == b for a, b in zip(listA, listB))

  def play(self):
    _secret = self.generate_sequence()
    print("secret:", *_secret, end='', flush=True)
    sleep(0.7)
    screen_cleaner()
    guesses = self.get_list_from_user()
    # return True if lost(nonEqual), False if won(equal)
    return not self.is_list_equal(guesses, _secret)