from functools import wraps

def types(*type_list):
  def _decorator(func):
    @wraps(func)
    def _wrapper(*args, **kwds):
        for a, t in zip(args, type_list):
          if not isinstance(a, t):
            raise TypeError(f"Expected {t}, got {a} of type {type(a)}")
        return func(*args, **kwds)
    return _wrapper
  return _decorator