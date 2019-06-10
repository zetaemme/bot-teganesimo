FROM python:3.7

RUN pip3 install --trusted-host pypi.python.org aiogram

RUN mkdir /app
ADD . /app
WORKDIR /app

CMD ["python3", "botteganesimo.py"]
