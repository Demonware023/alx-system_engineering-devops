#!/usr/bin/python3
"""
Script that uses a REST API to return information about all employee's TODO list
and exports it in JSON format.
"""
import json
import requests
import sys

def export_all_employee_tasks():
    # Get all users
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    # Initialize an empty dictionary to hold the data
    data = {}

    # Loop through each user
    for user in users:
        # Get the user's ID and username
        user_id = user['id']
        username = user['username']

        # Get the user's tasks
        tasks = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos').json()

        # Format the tasks as required
        formatted_tasks = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in tasks
        ]

        # Add the tasks to the data dictionary
        data[user_id] = formatted_tasks

    # Write the data to a JSON file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    export_all_employee_tasks()

