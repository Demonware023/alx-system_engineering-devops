#!/usr/bin/python3
"""
Script that uses a REST API to return information about an employee's TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
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

    employee_name = user_data.get("name")
    completed_tasks = [todo.get("title") for todo in todos_data if todo.get("completed")]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")
