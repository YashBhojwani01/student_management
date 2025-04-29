from os import name
from flask import Flask, request, jsonify

app = Flask(__name__)
students = {}

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    student_id = data.get("id")
    students[student_id] = data
    return jsonify({"message": "Student added."}), 201

@app.route("/students/<id>", methods=["GET"])
def get_student(id):
    student = students.get(id)
    if student:
        return jsonify(student)
    return jsonify({"message": "Student not found."}), 404

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5001)
