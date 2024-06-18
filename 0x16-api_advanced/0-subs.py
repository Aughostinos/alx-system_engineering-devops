#!/usr/bin/python3
"""API advanced project"""
import requests


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers) for a given
    subreddit. If an invalid subreddit is given, the function should return 0.
    """
    api_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": 'my_app_name/0.1 by my_reddit_username'
    }
    
    try:
        response = requests.get(api_url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException as e:
        print("Request failed: {}".format(e))
        return 0
    except ValueError as e:
        print("JSON decoding failed: {}".format(e))
        return 0