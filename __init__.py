"""
Python wrapper for Chuck Norris jokes from API https://api.chucknorris.io/

:author:     --  Sunil Kumar <sunildasu1234@gmail.com>
"""
import requests
from flask import Flask

app = Flask(__name__)


class ChuckNorris(object):

    @app.route("/")
    def main():
        return "Welcome! to Chuck-norris"

    @app.route('/jokes')
    def get_jokes():
        url = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(url)
        return response.json()['value']

    if __name__ == "__main__":
        app.run(host="127.0.0.1", port=8080)
