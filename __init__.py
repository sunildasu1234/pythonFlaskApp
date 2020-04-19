"""
Python wrapper for Chuck Norris jokes from API https://api.chucknorris.io/

:author:     --  Sunil Kumar <sunildasu1234@gmail.com>
:license:    --  MIT License - http://www.opensource.org/licenses/mit-license.php
"""
import requests
from flask import Flask
app = Flask(__name__)

class NorrisException(Exception):
    pass


class Norris(object):

    def __init__(self):
        self.id = None
        self.joke = None
        self.categories = None

    def __repr__(self):
        return '<{cls}: {joke}>'.format(
            cls=self.__class__.__name__,
            joke=self.joke
        )


class ChuckNorris(object):

    def __init__(self):
        self.base_url = 'http://api.icndb.com/jokes/'

    @app.route('/self')
    def get_jokes_count():
        url = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(url)
        return response.json()['value']

@app.route("/")
def main():
    return "Welcome! to Chuck-norris"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)