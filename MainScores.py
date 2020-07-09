from Utils import SCORES_FILE_NAME
from _strings import html_response, html_success, html_error
from pathlib import Path
from flask import Flask
app = Flask(__name__)

@app.route('/')
def score_server():
  scores_file = Path(SCORES_FILE_NAME)
  try:
    content = html_success.format(
      int(scores_file.read_text())
    )
  except Exception as err:
    content = html_error.format(err)
  return html_response.format(content)