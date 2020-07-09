from os import system, name

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = -1

def screen_cleaner():
  print('\r')
  if name != 'nt':
    system('clear')
  if name != 'posix':
    system('cls')