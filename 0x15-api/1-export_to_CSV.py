#!/usr/bin/python3
"""
Script that uses a REST API to return information about an employee's TODO list progress
and exports it in CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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

    user_id = user_data.get("id")
    username = user_data.get("username")

    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos_data:
            task_completed_status = todo.get("completed")
            task_title = todo.get("title")
            csv_writer.writerow([user_id, username, task_completed_status, task_title])

    print(f"Data exported to {csv_filename}")
