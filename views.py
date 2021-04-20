from flask import Flask, request, render_template, redirect, url_for
from forms import TodoForm
from models import todos

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/todos/", methods=["GET", "POST"])
def todos_list():
    form = TodoForm()
    if request.method == "POST":
        if form.validate_on_submit():
            title = request.form["title"]
            description = request.form["description"]
            todos.add_task(title, description)
        return redirect(url_for("todos_list"))
    return render_template("todos.html", form=form, todos=todos.get_all())


@app.route("/todos/<uuid:todo_id>/", methods=["GET", "POST"])
def todo_details(todo_id):
    todo = todos.get(todo_id)
    form = TodoForm(data=todo)

    if request.method == "POST":
        if form.validate_on_submit():
            title = request.form["title"]
            description = request.form["description"]
            todos.update(todo_id, title, description)
        return redirect(url_for("todos_list"))
    return render_template("todo.html", form=form, todo_id=todo_id)


@app.route("/todos/delete/<uuid:todo_id>/", methods=["GET"])
def todo_delete(todo_id):
    form = TodoForm()
    todos.delete(todo_id)

    return render_template("todos.html", form=form, todos=todos.get_all())


if __name__ == "__main__":
    app.run(debug=True)
