import json
import requests

# Fetch users and their tasks
users_response = requests.get('https://jsonplaceholder.typicode.com/users')
todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')

users = users_response.json()
todos = todos_response.json()

# Create a dictionary to hold the data
all_users_tasks = {}

# Populate the dictionary with user tasks
for user in users:
    user_id = user['id']
    username = user['username']
    user_tasks = []

    for task in todos:
        if task['userId'] == user_id:
            user_tasks.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })
    
    all_users_tasks[user_id] = user_tasks

# Write the data to a JSON file
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(all_users_tasks, json_file)

