#!/usr/bin/python3
"""Function to query subscribers"""
import json
import requests


def number_of_subscribers(subreddit):
    user = {"User-Agent": "Hamza_esadik"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=user)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
