FROM python:3
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-arrow
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt
