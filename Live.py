from _strings import hello_name, game_to_play, game_difficulty
from type_safety import type_check, options_1_to_
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import add_score

GAMES = (MemoryGame, GuessGame, CurrencyRouletteGame)

@type_check
def welcome(name: str):
  return hello_name.format(name)

def load_game():
  try:
    game = options_1_to_(3, game_to_play)
    difficulty = options_1_to_(5, game_difficulty)
  except EOFError as err:
    raise EOFError(f'{err}, please enable "-it" flags in "docker run" command') from err
  play_status = GAMES[game-1](difficulty).play()
  if play_status:
    print('lost')
  else:
    print('won')
    add_score(difficulty) 
