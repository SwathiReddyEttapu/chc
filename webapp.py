from flask import Flask
from random import randint
import requests

app = Flask(__name__)


@app.route("/")
def index():
    print('hello world')
    return "Hello World!"


@app.route("/getString")
def getString():
    """
    This api picks up a player count then get data from rest api as a json object
    :return: a string as described
    """
    players = [1, 2, 3, 4, 5, 8]
    count = players[randint(0, 5)]
    response = requests.get(f'http://www.boredapi.com/api/activity?participants={count}')
    data = response.json()
    return_string = f'An activity suitable for {data["participants"]} participants would be {data["activity"]} which is of type {data["type"]}'
    return return_string


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)
