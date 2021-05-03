# library.py

from app import app, db
from app.models import Book, Author, authors, Stock

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Book": Book,
        "Author": Author,
        "authors": authors,
        "Stock": Stock
    }

app.run(debug=True)