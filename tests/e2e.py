#!/bin/env python3
from urllib.request import urlopen
from xml.etree.ElementTree import parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import argv

def test_scores_service():
  host = argv[1] if argv[1:] else 'localhost'
  port = argv[2] if argv[2:] else '5000'
  value = tuple(parse(urlopen(f'http://{host}:{port}/score')).iter())[-1].text
  return value.isnumeric() and 1 <= int(value) <= 1000

def main_function():
  with webdriver.Firefox as driver:
    driver.get('http://localhost:5000/terminal')
    # in "211 ", the trailing space is ment to be
    driver.find_element_by_id('terminal').sendKeys(Keys.ENTER.join("211 "))
    # 2. game
    # 1. difficulty
    # 1. guess
  try:
    exit(0 if test_scores_service() else -1)
  except:
    exit(-2)

if __name__ == '__main__':
  main_function()