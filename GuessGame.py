from _strings import get_guess
from type_safety import type_check, options_1_to_
from random import randint

class GuessGame:
  __slots__ = ('difficulty', '_secret')

  @type_check
  def __init__(self, difficulty: int):
    self.difficulty = difficulty

  def generate_number(self):
    self._secret = randint(1, self.difficulty)

  def get_guess_from_user(self):
    prompt = get_guess.format(self.difficulty)
    return options_1_to_(self.difficulty, prompt)
  
  @type_check
  def compare_results(self, guess: int):
    # return isEqual
    return guess == self._secret

  def play(self):
    self.generate_number()
    guess = self.get_guess_from_user()
    # return True if lost(nonEqual), False if won(equal)
    return not self.compare_results(guess)



