#!/usr/bin/python3
"""Write a Python script that, using this REST API"""
import csv
import requests
import sys


if __name__ == '__main__':
    data_to_write = []
    USER_ID = sys.argv[1]
    todos_url = f'https://jsonplaceholder.typicode.com/users/{USER_ID}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{USER_ID}'
    todos_data = requests.get(todos_url).json()
    user_data = requests.get(user_url).json()
    USERNAME = user_data.get('username')
    TASK_COMPLETED_STATUS = []
    TASK_TITLE = []

    for todo in todos_data:
        tmp = []
        tmp.append(USER_ID)
        tmp.append(USERNAME)
        tmp.append(todo.get('completed'))
        tmp.append(todo.get('title'))
        data_to_write.append(tmp)

    with open(f'{USER_ID}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(data_to_write)
