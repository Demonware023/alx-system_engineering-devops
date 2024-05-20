#!/usr/bin/python3
"""
Script that uses a REST API to return information about all employee's TODO list
and exports it in JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: ./3-dictionary_of_list_of_dictionaries.py")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com"
    users_url = f"{url}/users"
    todos_url = f"{url}/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200:
        print("Error: Empty - No records found")
        sys.exit(1)

    users = users_response.json()
    todos = todos_response.json()

    # Process the data
    data = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [task for task in todos if task['userId'] == user_id]

        data[user_id] = []
        for task in user_tasks:
            data[user_id].append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })

    # Export to JSON
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("Data has been exported to todo_all_employees.json")
