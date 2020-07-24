from Utils import SCORES_FILE_NAME
from pathlib import Path
from pyxtermjs.app import app, socketio, index
from werkzeug.routing import Map

app.url_map = Map()

@app.route('/score')
def score_server():
  scores_file = Path(SCORES_FILE_NAME)
  try:
    return scores_file.read_text()
  except Exception:
    return "0"

app.add_url_rule('/terminal', 'index', index)

@app.route('/')
def main_page():
  return 'hello world'

app.config['cmd'] = ('python', '-i', './MainGame.py')
socketio.run(app, '0.0.0.0', '5000', debug=True, use_reloader=True, extra_files=(SCORES_FILE_NAME,))