#!/usr/bin/python3
"""Script that queries subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Reddit Sub Counter."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Linux:0x16 api.advanced:v1.0.0 (by u/nm01)'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
