from flask import render_template
from app import app


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/favorite")
def favorite():
    my_favorite_five_books = [
        {
            'Book': 'The Divine Conspiracy',
            'Author': 'Dallas Willard',
            'Published': 'March, 1998'
        },
        {
            'Book': 'Deliverance by Force',
            'Author': 'Idong Wilson',
            'Published': 'December, 2011'   
        },
        {
            'Book': 'Living a Life of Fire',
            'Author': 'Reinhard Bonnke',
            'Published': 'October, 2009'   
        },
        {
            'Book': 'Ben Hur',
            'Author': 'Lew Wallace',
            'Published': 'March, 1880'   
        },
        {
            'Book': 'Who Moved the Cheese?',
            'Author': 'Spencer Johnson & Kenneth Blanchard',
            'Published': 'September, 1998'   
        },
    ]
    return render_template('my_favorite.html', favorite=my_favorite_five_books)  