# app/models.py

from app import db

authors = db.Table('authors',
                   db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),
                   db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
                   )


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), index=True, nullable=False, unique=True)
    authors = db.relationship('Author', secondary=authors, lazy='subquery', backref=db.backref('books', lazy=True))
    stock = db.relationship('Stock', backref='book', lazy=True, cascade="all, delete")


    def __repr__(self):
        return f"{self.title}"


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True, nullable=False, unique=True)


    def __repr__(self):
        return f"{self.name}"


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    available = db.Column(db.Boolean, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)


    def __repr__(self):
        return f"{self.available}"
