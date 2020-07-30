#!/bin/env python3
from Utils import SCORES_FILE_NAME
from pathlib import Path
from pyxtermjs.app import app, socketio, index
from werkzeug.routing import Map
from threading import Timer
from _thread import interrupt_main

app.url_map = Map()

@app.route('/score')
def score_frame():
  scores_file = Path(SCORES_FILE_NAME)
  try:
    score = scores_file.read_text()
  except:
    score = '0'
  return """<html>
<head>
  <title>Score</title>
  <meta http-equiv="refresh" content="8"/>
</head>
<body style="overflow:hidden">
  <h1><strong id="score" style="color:red">{}</strong></h1>
</body>
</html>""".format(score)

app.add_url_rule('/terminal', 'index', index)

@app.route('/')
def main_page():
  return """<html>
<head>
  <title>Tamir Fridman - Game</title>
</head>
<body style="overflow:hidden">
  <h1 style="height:35px;float:left;margin:6px">The score is</h1>
  <iframe height="45px" style="border:none;float:left;overflow:hidden" src="/score" title="score"></iframe>
  <iframe width="100%" style="height:calc(100% - 45px);border:none;float:left;overflow:hidden" src="/terminal" title="terminal"></iframe>
</body>
</html>"""

@app.route('/stop')
def stop():
  Timer(0.1, interrupt_main).start()
  return "exit"

app.config['cmd'] = ('python', '-i', './MainGame.py')
socketio.run(app, '0.0.0.0', '5000', debug=True, use_reloader=False)