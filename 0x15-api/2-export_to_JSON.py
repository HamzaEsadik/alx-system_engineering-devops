#!/usr/bin/python3
'''export data in the json format'''
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    todos_url = f'https://jsonplaceholder.typicode.com/users/{USER_ID}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{USER_ID}'
    todos_data = requests.get(todos_url).json()
    user_data = requests.get(user_url).json()
    USERNAME = user_data.get('username')

    with open(f'{USER_ID}.json', 'w') as json_file:
        json.dump({USER_ID: [{
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': USERNAME
        } for todo in todos_data]}, json_file)
