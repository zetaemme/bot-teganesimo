FROM debian:stretch
RUN apt-get update
RUN apt-get install -y python3-pip
WORKDIR /app
COPY requirements.txt /app/
COPY botteganesimo.py /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD python botteganesimo.py
