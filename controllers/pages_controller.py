from db.db import clicks
from requests import HTTPResponseCode


class Controller:
    def __init__(self, request, response):
        self.request = request
        self.response = response
        self.response.add_header('Content-Type', 'text/html')


class PagesController(Controller):

    def home(self):
        self.response.set_body('<h1>Main page</h1><ul><li><h2><a href="/one">First page</a></h2></li><li><h2>'
                               '<a href="/two">Second page</a></h2></li><li><h2><a href="/three">Third page</a>'
                               '</h2></li><li><h2><a href="/game">Clicker</a></h2></li></ul>')

    def one(self):
        self.response.set_body('<a href="/"><h1>First page</h1></a>')

    def two(self):
        self.response.set_body('<a href="/"><h1>Second page</h1></a>')

    def three(self):
        self.response.set_body('<a href="/"><h1>Third page</h1></a>')

    def game(self):
        clicks["clicks"] = 0
        self.response.set_body(f'<h1>{clicks["clicks"]}</h1><form method="get" action="/add_click/">'
                               '<input type="submit" value="Click!"></form>')

    def add_click(self):
        clicks["clicks"] += 1
        self.response.set_body(f'<h1>{clicks["clicks"]}</h1><form method="get" action="/add_click/">'
                               '<input type="submit" value="Click!"></form><form method="get" action="/game/">'
                               '<input type="submit" value="Refresh!"></form>')

    @staticmethod
    def not_found(request, response):
        response.add_header('Content-Type', 'text/html')
        response.set_status(HTTPResponseCode.NOT_FOUND)
        response.set_body('<h1>404 Not Found</h1>')
