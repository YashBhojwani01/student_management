from os import name
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
enrollments = []

STUDENT_SERVICE_URL = "http://student_service:5001/students/"
COURSE_SERVICE_URL = "http://course_service:5002/courses/"

@app.route("/enroll", methods=["POST"])
def enroll_student():
    data = request.json
    student_id = data.get("student_id")
    course_id = data.get("course_id")

    student_resp = requests.get(STUDENT_SERVICE_URL + student_id)
    course_resp = requests.get(COURSE_SERVICE_URL + course_id)

    if student_resp.status_code != 200:
        return jsonify({"message": "Student not found."}), 404
    if course_resp.status_code != 200:
        return jsonify({"message": "Course not found."}), 404

    enrollments.append(data)
    return jsonify({"message": "Enrollment successful."}), 201

@app.route("/enrollments", methods=["GET"])
def list_enrollments():
    return jsonify(enrollments)

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5003)