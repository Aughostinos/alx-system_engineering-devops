#!/usr/bin/python3
"""API advanced project"""
import requests


#define the base url
api_url = "https://www.reddit.com/r/{subreddit}/about.json"
headers = {
    "User-Agent": "my_function"
}


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers) for a given 
    subreddit. If an invalid subreddit is given, the function should return 0.
    """
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0