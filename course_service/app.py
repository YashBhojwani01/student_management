from os import name
from flask import Flask, request, jsonify

app = Flask(__name__)
courses = {}

@app.route("/courses", methods=["POST"])
def add_course():
    data = request.json
    course_id = data.get("id")
    courses[course_id] = data
    return jsonify({"message": "Course added."}), 201

@app.route("/courses/<id>", methods=["GET"])
def get_course(id):
    course = courses.get(id)
    if course:
        return jsonify(course)
    return jsonify({"message": "Course not found."}), 404

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5002)