#!/bin/env python3
from urllib.request import urlopen
from xml.etree.ElementTree import parse

def test_scores_service():
  value = tuple(parse(urlopen('http://localhost:5000/score')).iter())[-1].text
  return value.isnumeric() and 1 <= int(value) <= 1000

def main_function():
  try:
    exit(0 if test_scores_service() else -1)
  except:
    exit(-2)