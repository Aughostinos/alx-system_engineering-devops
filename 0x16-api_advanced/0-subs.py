#!/usr/bin/python3
"""API advanced project"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": 'my_reddit_app/0.1 (by /u/AugustinosAbusaif)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            print(f"Error: Received status code {response.status_code}")
            return 0
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return 0