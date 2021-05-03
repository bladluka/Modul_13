# app/routes.py

from flask import render_template, request, redirect
from app import app, db
from app.models import Book, Author, authors, Stock
from sqlalchemy.exc import IntegrityError


@app.route("/books/", methods=["GET", "POST"])
def book_list():
    books = Book.query.all()
    authors = Author.query.all()

    if request.method == "POST":
        if request.form["title"] == '':
            pass
        else:
            try:
                title = request.form["title"]
                book = Book(title=title)
                db.session.add(book)
                db.session.commit()
                stock = Stock(available=True, book=book)
                db.session.add(stock)
                db.session.commit()
            except IntegrityError:
                pass

        return redirect("/books/")

    return render_template("books.html", books=books, authors=authors)


@app.route("/authors/", methods=["GET", "POST"])
def author_list():
    authors = Author.query.all()

    if request.method == "POST":
        if request.form["name"] == '':
            pass
        else:
            try:
                name = request.form["name"]
                author = Author(name=name)
                db.session.add(author)
                db.session.commit()
            except IntegrityError:
                pass

        return redirect("/authors/")

    return render_template("authors.html", authors=authors)


@app.route("/books/delete/<int:book_id>/", methods=["GET"])
def book_delete(book_id):

    b = Book.query.get(book_id)
    db.session.delete(b)
    db.session.commit()

    return redirect("/books/")


@app.route("/authors/delete/<int:author_id>/", methods=["GET"])
def author_delete(author_id):

    author = Author.query.get(author_id)
    db.session.delete(author)
    db.session.commit()


    return redirect("/authors/")


@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_modify(book_id):
    Authors = Author.query.all()
    book = Book.query.get(book_id)

    if request.method == "POST":

        if request.form["title"] == '':
            pass
        else:
            book.title = request.form["title"]
            db.session.add(book)
            db.session.commit()

        if request.form["author"] == '0':
            pass
        else:
            param_book_id = book.id
            param_author_id = request.form["author"]
            try:
                db.session.execute(authors.insert(), params={"author_id": param_author_id, "book_id": param_book_id}, )
                db.session.commit()
            except IntegrityError:
                pass

        return redirect("/books/")

    return render_template("book.html", book=book, Authors=Authors)


@app.route("/books/out/<int:book_id>/", methods=["GET"])
def book_out(book_id):

    book = Book.query.get(book_id)
    stock = Stock(available=False, book=book)
    db.session.add(stock)
    db.session.commit()

    return redirect("/books/")


@app.route("/books/in/<int:book_id>/", methods=["GET"])
def book_in(book_id):

    book = Book.query.get(book_id)
    stock = Stock(available=True, book=book)
    db.session.add(stock)
    db.session.commit()

    return redirect("/books/")