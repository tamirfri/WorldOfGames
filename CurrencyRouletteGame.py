from _strings import get_nis_guess, api_url
from type_safety import type_check, options_1_to_
from urllib.request import urlopen
from json import load
from random import randint

class CurrencyRouletteGame:
  __slots__ = ('difficulty', '_secret', 'usd2nis')
  upper = 100

  @type_check
  def __init__(self, difficulty: int):
    self.difficulty = difficulty
    response = load(urlopen(api_url))
    self.usd2nis = response['USD_ILS']['val']

  def get_money_interval(self):
    t = self.usd2nis * randint(1, self.upper) # exact value
    d = self.difficulty
    self._secret = (t-5+d, t+5-d)

  def get_guess_from_user(self):
    upper_bound = int(self.upper * self.usd2nis + 1)
    return options_1_to_(upper_bound, get_nis_guess)

  def play(self):
    self.get_money_interval()
    guess = self.get_guess_from_user()
    # return True if lost(nonEqual), False if won(equal)
    return guess < self._secret[0] or self._secret[1] < guess
