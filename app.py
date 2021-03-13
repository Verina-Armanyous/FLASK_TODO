from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
import os
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)


# create database module
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    state = db.Column(db.String(20))

# create flask WTF form to take input from user


class TodoForm(FlaskForm):
    """Todo form."""
    title = StringField(label=('Enter Task:'),
                        validators=[DataRequired()])
    state = SelectField(u'Select State', choices=[(
        'todo'), ('in-progress'), ('done')])
    submit = SubmitField('Add')


# routing for the main page that renders all the todo items
@app.route("/", methods=["GET", "POST"])
def index():
    """Standard `contact` form."""
    form = TodoForm()
    todo_list = Todo.query.all()
    return render_template(
        "base.html",
        form=form, todo_list=todo_list)


# routing for adding a new todo entry
@app.route('/add', methods=['POST', 'GET'])
def new_task():
    title = request.form.get("title")
    state = request.form.get("state")
    new_todo = Todo(title=title, state=state)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


# routing for deleting a todo entry
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


# routing to move a todo entry to a right state
@app.route("/update_right/<int:todo_id>")
def update_right(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo.state == "todo":
        todo.state = "in-progress"
    elif todo.state == "in-progress":
        todo.state = "done"
    db.session.commit()
    return redirect(url_for("index"))

# routing to move a todo entry to a left state


@app.route("/update_left/<int:todo_id>")
def update_left(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo.state == "done":
        todo.state = "in-progress"
    elif todo.state == "in-progress":
        todo.state = "todo"
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
