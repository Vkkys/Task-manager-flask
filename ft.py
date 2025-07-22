
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

# Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Create DB
with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def home():
    return "Task Manager API is running!"

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'completed': t.completed} for t in tasks])


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    # your logic to store task


# Mark task complete
@app.route('/tasks/<int:id>', methods=['PUT'])
def complete_task(id):
    task = Task.query.get(id)
    if task:
        task.completed = True
        db.session.commit()
        return jsonify({'message': 'Task marked as completed'})
    return jsonify({'error': 'Task not found'}), 404

# Delete task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted'})
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
