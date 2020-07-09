from pathlib import Path
from Utils import SCORES_FILE_NAME
from type_safety import type_check

@type_check
def add_score(difficulty: int):
  scores_file = Path(SCORES_FILE_NAME)
  try:
    current_score = int(scores_file.read_text())
  except:
    current_score = 0
  
  current_score += (difficulty * 3) + 5

  scores_file.write_text(repr(current_score))