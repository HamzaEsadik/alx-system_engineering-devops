#!/usr/bin/python3
"""Write a Python script that, using this REST API"""
import csv
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/" + user_id
    res = requests.get(url_user).json()
    username = res.get("username")
    req = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (user_id) + '/todos')
    with open("{}.csv".format(sys.argv[1]), "w") as file_c:
        writer = csv.writer(file_c, quoting=csv.QUOTE_ALL)
        for task in req.json():
            writer.writerow([user_id, username,
                            task.get("completed"), task.get("title")])
