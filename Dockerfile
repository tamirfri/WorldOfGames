FROM python

WORKDIR /usr/src/app

RUN [ "chmod", "777", "." ] # permissions to create Scores.txt

RUN [ "pip", "install", "--no-cache-dir", "eventlet", "gevent", "gevent-websocket", "flask", "pyxtermjs" ]


#ENV FLASK_APP=MainScores.py FLASK_ENV=development

EXPOSE 5000

# open http://localhost:5000/ in browser

#USER nobody



COPY *.py ./

# CMD python ./MainGame.py && flask run --host 0.0.0.0

# ENTRYPOINT [ "pyxtermjs", "--debug", "--command", "python", "--cmd-args" ]

CMD [ "python", "./MainScores.py" ]

# EOFError if not using "-it" flags in docker run