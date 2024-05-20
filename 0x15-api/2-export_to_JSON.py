#!/usr/bin/python3
"""
Script that uses a REST API to return information about an employee's TODO list progress
and exports it in JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: /2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users/{employee_id}"
    todos_url = f"{url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print("Error: Employee not found")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    user_id = str(user_data.get("id"))
    username = user_data.get("username")

    tasks = []
    for todo in todos_data:
        task_dict = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        tasks.append(task_dict)

    data = {user_id: tasks}

    json_filename = f"{user_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file)

    print(f"Data exported to {json_filename}")
