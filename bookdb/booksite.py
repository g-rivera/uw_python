# Guillermo Rivera
# week 7 assignment
# flask - bookdb

from flask import Flask, render_template
from bookdb import BookDB

bookdbapp = Flask(__name__)
db  = BookDB()

@app.route("/")
def index():
    return render_template('index.html', books=db.books(), num_books=len(db.books()))

@app.route("/info/<id>")
def detail(id=None):
    return render_template('info.html', book=db.book_info(id))

if __name__ == '__main__': 
    bookdbapp.run()
