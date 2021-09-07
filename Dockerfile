FROM python:3.8

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

RUN apt-get update

EXPOSE 5000

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

# Development (comment production lines and uncomment development lines)
RUN export FLASK_APP=run.py

CMD ["flask", "run"]
