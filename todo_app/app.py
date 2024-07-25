from flask import Flask, render_template, request, redirect, url_for
from models import db, Todo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
	todos = Todo.query.all()
	return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    new_todo = Todo(content=request.form['content'])
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
	todo = Todo.query.get(todo_id)
	db.session.delte(todo)
	db.session.commit()
	return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)