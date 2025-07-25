from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

FILE = "todos.json"

def load_todos():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(FILE, "w") as f:
        json.dump(todos, f)

@app.route("/", methods=["GET", "POST"])
def index():
    todos = load_todos()
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            todos.append({"text": task, "done": False})
            save_todos(todos)
        return redirect("/")
    return render_template("index.html", todos=todos)

@app.route("/toggle/<int:index>")
def toggle(index):
    todos = load_todos()
    todos[index]["done"] = not todos[index]["done"]
    save_todos(todos)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    todos = load_todos()
    todos.pop(index)
    save_todos(todos)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
