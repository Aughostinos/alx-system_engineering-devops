#!/usr/bin/python3
"""API advanced project"""
import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit."""
    
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Augustbot/0.1'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException as e:
        print(None)