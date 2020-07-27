FROM python:alpine

WORKDIR /usr/src/app

RUN [ "chmod", "777", "." ] # permissions to create Scores.txt

RUN [ "apk", "add", "--no-cache", "build-base" ]

RUN [ "pip", "install", "--no-cache-dir", "--target", ".",\
 "eventlet", "flask", "pyxtermjs" ] # "gevent", "gevent-websocket"

# patch
RUN [ "sed", "-i", "s/<body>/<body style='overflow:hidden'>/", "pyxtermjs/index.html" ]

USER nobody



COPY *.py ./

CMD [ "python", "./MainScores.py" ]

EXPOSE 5000

# open http://localhost:5000/ in browser
# EOFError if not using "-it" flags in docker run
# docker run -tip 5000:5000...