import sqlite3
import uuid

class Todos:

    def add_task(self, title, description):
        conn = sqlite3.connect("todos.db")
        sql = "INSERT INTO todo VALUES (?, ?, ?)"
        cur = conn.cursor()
        id = str(uuid.uuid4())
        cur.execute(sql, (id, title, description))
        conn.commit()
        return cur.lastrowid

    def get_all(self):
        conn = sqlite3.connect("todos.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM todo")
        rows = cur.fetchall()
        results = []
        for item in rows:
            results.append({
                'id': item[0],
                'title': item[1],
                'description': item[2]
            })
        return results

    def get(self, todo_id):
        conn = sqlite3.connect("todos.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM todo WHERE id=?", (str(todo_id), ))
        row = cur.fetchall()
        result = {
            'id': row[0][0],
            'title': row[0][1],
            'description': row[0][2]
        }
        return result

    def update(self, todo_id, title, description):
        conn = sqlite3.connect('todos.db')
        sql = "UPDATE todo SET title = ?, description = ? WHERE id = ?"
        cur = conn.cursor()
        cur.execute(sql, (title, description, str(todo_id)))
        conn.commit()

    def delete(self, todo_id):
        conn = sqlite3.connect('todos.db')
        cur = conn.cursor()
        cur.execute("DELETE from todo WHERE id = ?", (str(todo_id), ))
        conn.commit()

todos = Todos()





