from _strings import hello_name, game_to_play, game_difficulty, wrong_input
from _type_safety import types

@types(str)
def welcome(name):
  return hello_name.format(name)

@types(str)
def _int_or_none(string):
  if string.isnumeric():
    return int(string)

@types(int)
def _options_1_to_(high, prompt):
  error_prompt = wrong_input.format(high)
  while (num := _int_or_none(input(prompt)) is None
          or num <= 0 or num > high):
    prompt = error_prompt
    

def load_game():
  game = _options_1_to_(3, game_to_play)
  difficulty = _options_1_to_(5, game_difficulty)
  
