from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

# JSON読み込み関数
def load_todos():
    with open("todos.json", "r", encoding="utf-8") as f:
        return json.load(f)

# JSON保存関数
def save_todos(todos):
    with open("todos.json", "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2, ensure_ascii=False)

# メインページ（GETとPOSTどちらも受け取る）
@app.route("/", methods=["GET", "POST"])
def index():
    todos = load_todos()

    if request.method == "POST":
        new_todo = request.form["todo"].strip()
        if new_todo:
            todos.append(new_todo)
            save_todos(todos)
        return redirect("/")  # 2重送信防止

    return render_template("index.html", todos=todos)

if __name__ == "__main__":
    app.run(debug=True)
