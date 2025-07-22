from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy in-memory storage for tasks
tasks = []

# Home route
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Task Manager API!", 200

# POST /tasks - create a new task
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    title = data['title']
    task = {"id": len(tasks) + 1, "title": title}
    tasks.append(task)

    return jsonify({'message': 'Task added successfully', 'task': task}), 201

# GET /tasks - list all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

if __name__ == "__main__":
    app.run(debug=True)
