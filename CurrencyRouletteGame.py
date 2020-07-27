from _strings import prompt_get_nis_guess, api_url
from type_safety import options_1_to_
from urllib.request import urlopen
from json import load
from random import randint

# self is difficulty
class CurrencyRouletteGame(int):
  upper = 100
  usd2nis = load(urlopen(api_url))['USD_ILS']['val']

  def get_money_interval(self):
    t = self.usd2nis * randint(1, self.upper) # exact value
    d = self # difficulty
    return (t-5+d, t+5-d)

  @classmethod
  def get_guess_from_user(cls):
    upper_bound = int(cls.upper * cls.usd2nis + 1)
    return options_1_to_(upper_bound, prompt_get_nis_guess)

  def play(self):
    _secret = self.get_money_interval()
    guess = self.get_guess_from_user()
    # return True if lost(nonEqual), False if won(equal)
    return guess < _secret[0] or _secret[1] < guess
