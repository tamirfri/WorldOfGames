from _strings import wrong_input
from inspect import getfullargspec
from functools import wraps

def type_check(func):
  spec = getfullargspec(func)
  names_to_check = {name : spec.annotations.get(name) for name in spec.args}
  if all(val is None for key, val in names_to_check.items()):
    return func
  @wraps(func)
  def _wrapper(*args, **kwargs):
    params = list(names_to_check)
    for param in names_to_check.keys() & kwargs.keys():
      # check from **kwargs
      params.remove(param)
      a, t = kwargs[param], names_to_check[param]
      if t and not isinstance(a, t):
        msg = f"{func.__name__}([{param}: {t.__name__},]) got {a}: {type(a).__name__}."
        raise TypeError(msg)
    for param, val in zip(params, args):
      # check from *args
      a, t = val, names_to_check[param]
      if t and not isinstance(a, t):
        msg = f"{func.__name__}([{param}: {t.__name__},]) got {a}: {type(a).__name__}."
        raise TypeError(msg)
    return func(*args, **kwargs)
  return _wrapper

@type_check
def int_or_none(parse: str):
  if parse.isdigit():
    return int(parse)

@type_check
def options_1_to_(high: int, prompt: str):
  error_prompt = wrong_input.format(high)
  while (None is (num := int_or_none(input(prompt)))
          or num <= 0 or num > high):
    prompt = error_prompt
  return num
