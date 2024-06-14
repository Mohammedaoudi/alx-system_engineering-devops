#!/usr/bin/python3
""" Getting Reddit data using Reddit API """


import requests


headers = {"User-Agent": "MyAlxCustomUserAgent/1.0"}


def number_of_subscribers(subreddit):
    """Returning the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
