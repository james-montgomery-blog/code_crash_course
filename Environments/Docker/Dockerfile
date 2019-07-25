FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    curl \
    python3-dev \
    python3-pip \
    nano

ADD requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install jupyter
