#!/bin/env python3
from Live import load_game, welcome

def main():
  print(welcome('Guy'))
  while True:
    load_game()

if __name__ == '__main__':
  main()