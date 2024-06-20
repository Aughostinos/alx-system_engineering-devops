#!/usr/bin/python3
"""api advanced project"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given
    subreddit. If an invalid subreddit is given, returns 0.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Augustbot'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print(f"Response status code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response data: {data}")
            return data['data']['subscribers']
        else:
            print(f"Non-200 status code: {response.status_code}")
            return 0
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return 0