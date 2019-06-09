FROM python:3.7

RUN pip3 install aiogram

RUN mkdir /app
ADD . /app
WORKDIR /app

CMD python3 /app/botteganesimo.py
