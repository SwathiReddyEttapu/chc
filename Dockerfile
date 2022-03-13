FROM python:3.8-slim-buster
RUN mkdir /app
WORKDIR /app

ADD . /app
RUN pip3 install -r requirements.txt

CMD [ "python3", "./webapp.py"]