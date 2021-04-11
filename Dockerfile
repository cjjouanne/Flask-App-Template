FROM python:3.8

ADD . /usr/src/app

WORKDIR /usr/src/app

RUN apt-get update

COPY requirements.txt ./

EXPOSE 5000

RUN pip install -r requirements.txt

RUN export FLASK_APP=run.py

CMD ["flask", "run"]
