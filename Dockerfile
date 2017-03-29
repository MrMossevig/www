FROM python:3-onbuild

MAINTAINER Alf Petter Mossevig "ap.mossevig@gmail.com"

CMD [ "python", "./flask_web/app.py" ]