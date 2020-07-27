from _strings import get_guess
from type_safety import type_check, options_1_to_
from random import randint

# self is difficulty
class GuessGame(int):

  def generate_number(difficulty):
    return randint(1, difficulty)

  def get_guess_from_user(difficulty):
    prompt = get_guess.format(difficulty)
    return options_1_to_(difficulty, prompt)

  @staticmethod
  @type_check
  def compare_results(guess: int, _secret: int):
    # return isEqual
    return guess == _secret

  def play(self):
    _secret = self.generate_number()
    guess = self.get_guess_from_user()
    # return True if lost(nonEqual), False if won(equal)
    return not self.compare_results(guess, _secret)



