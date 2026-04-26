from flask import Flask
from flask import request
import json

database = {}
app = Flask(__name__)

@app.route("/")

def index():
    return "PE03 To-Do is running!"

# changed path to /tasks from /students
@app.route("/tasks", methods = ["POST"])
# Renamed function to post_tasks_details from post_students_details
def post_tasks_details():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))

        # Changed database value to "status" from "age"
        database[dict_json["name"]] = dict_json["status"]
        return "Success", 200
    
    except Exception as e:
        print("Error during saving object ", e)
        return "Failed", 400

# changed path to /tasks from /students
@app.route("/tasks", methods = ["PUT"])
# Renamed function to put_tasks_details from put_students_details
def put_tasks_details():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))

        # Changed database value to "status" from "age"
        database[dict_json["name"]] = dict_json["status"]
        return "Success", 200
    
    except Exception as e:
        print("Error during saving object ", e)
        return "Failed", 400

# changed path to /tasks from /students and removed parameter in order to return all tasks
@app.route("/tasks", methods = ["GET"])
# Renamed function to get_tasks_details from get_students_details and removed parameter in order to return all tasks
def get_tasks_details():
    try:
        task_list = "" # Initialized task_list as an empty string, removed unecessary name variable

        # Added loop to append task and its status to the task_list
        for task, status in database.items():
            task_list += task + ": " + status + "\n"

        return task_list, 200
    
    except KeyError: 
        return "Record not found", 404

# changed path to /tasks from /students and parameter to task_name from Student_name
@app.route("/tasks/<task_name>", methods = ["DELETE"])
# Renamed function to delete_tasks_details from delete_students_details and parameter to task_name from Student_name
def delete_tasks_details(task_name):
    try:
        # Changed database value to "status" from "age" and student_name to task_name
        status = database[task_name] 
        database.pop(task_name)
        
        return "Record deleted successfully", 200

    except KeyError: 
        return "Record not found", 404
    
    except Exception as e:
        print("Error while removing record", e)
        return "Error while removing record", 400