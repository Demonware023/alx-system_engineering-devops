#!/usr/bin/python3
import requests
import sys

def get_todo_list_progress(employee_id):
    # Get the details of the employee
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = response.json()

    # Get the TODOs of the employee
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos = response.json()

    # Calculate the progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo.get('completed')])

    # Print the first line
    print(f'Employee {employee.get("name")} is done with tasks({done_tasks}/{total_tasks}):')

    # Print the completed tasks
    for todo in todos:
        if todo.get('completed'):
            print(f'\t {todo.get("title")}')

if __name__ == "__main__":
    get_todo_list_progress(int(sys.argv[1]))
