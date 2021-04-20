import sqlite3


conn = sqlite3.connect("todos.db")
c = conn.cursor()

conn.execute(
    """CREATE TABLE todo (
            id TEXT PRIMARY KEY,
            title char(55) NOT NULL,
            description char(255) NOT NULL
            )"""
)