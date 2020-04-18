"""
Python wrapper for `The Internet Chuck Norris Database` API at http://www.icndb.com/api/.

:author:     --  Adiyat Mubarak <adiyatmubarak@gmail.com>
:link:       --  http://adiyatmubarak.web.id/
:license:    --  MIT License - http://www.opensource.org/licenses/mit-license.php
"""
import requests
import os
from flask import Flask
app = Flask(__name__)

class NorrisException(Exception):
    pass


class Norris(object):

    def mycode(self):
        self.id = None
        self.joke = None
        self.categories = None

    def __repr__(self):
        return '<{cls}: {joke}>'.format(
            cls=self.__class__.__name__,
            joke=self.joke
        )


class ChuckNorris(object):

    def mycode(self):
        self.base_url = 'http://api.icndb.com/jokes/'

    @app.route('/self')
    def get_jokes_count():
        # url = self.base_url + 'count/'
        url ='http://api.icndb.com/jokes/random'
        response = requests.get(url)
        return response.json()['value']

@app.route("/")
def main():
    return "Welcome! Hello world"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)