FROM python:alpine

WORKDIR /usr/src/app

RUN [ "chmod", "777", "." ] # permissions to create Scores.txt

ARG user=tamir

RUN yes | adduser --disabled-password ${user}



RUN [ "pip", "install", "--no-cache-dir", "flask" ]

ENV FLASK_APP=MainScores.py FLASK_ENV=development

EXPOSE 5000

# open http://localhost:5000/ in browser

USER ${user}



CMD python ./MainGame.py && flask run --host 0.0.0.0

# EOFError if not using "-it" flags in docker run

COPY *.py ./