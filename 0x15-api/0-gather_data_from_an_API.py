#!/usr/bin/python3
'''gather data from api'''
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    try:
        # fetch data
        user_response = requests.get(url)
        # parse data
        user_data = user_response.json()
        # name
        EMPLOYEE_NAME = user_data.get('name')
    except requests.RequestException as e:
        print(e)

    all_todos_url = (
        'https://jsonplaceholder.typicode.com/todos?userId=' +
        sys.argv[1])
    try:
        # fetch data
        all_todos_response = requests.get(all_todos_url)
        # parse data
        all_todos_data = all_todos_response.json()
        # TOTAL_NUMBER_OF_TASKS
        TOTAL_NUMBER_OF_TASKS = len(all_todos_data)
    except requests.RequestExceptions as e:
        print(e)

    todos_url = (
        'https://jsonplaceholder.typicode.com/todos?userId=' +
        sys.argv[1] +
        '&completed=true')
    try:
        # fetch data
        todos_response = requests.get(todos_url)
        # parse data
        todos_data = todos_response.json()
        # NUMBER_OF_DONE_TASKS
        NUMBER_OF_DONE_TASKS = len(todos_data)
    except requests.RequestExceptions as e:
        print(e)

    # print resaults
    print(f'Employee {EMPLOYEE_NAME} is done with tasks \
({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for todo in todos_data:
        print(todo.get('title'))
