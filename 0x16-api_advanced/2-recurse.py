#!/usr/bin/python3
"""API advanced project"""
import requests

def get_reddit_token(client_id, client_secret, username, password):
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {'grant_type': 'password', 'username': username, 'password': password}
    headers = {'User-Agent': 'myAPIbot/0.1'}

    response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    response.raise_for_status()
    token = response.json().get('access_token')
    return token

def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given subreddit, returns None.
    """
    client_id = 'I89Gxobf1Iskg-ZjHb_9cg'
    client_secret = '68NzNnNJqk3g0dVDprHo6eORqQepeQ'
    username = 'AugustinosAbusaif'
    password = 'Alx@123#!'
    token = get_reddit_token(client_id, client_secret, username, password)

    if not token:
        return None

    url = f'https://oauth.reddit.com/r/{subreddit}/hot'
    headers = {'Authorization': f'bearer {token}', 'User-Agent': 'myAPIbot/0.1'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list if hot_list else None
        else:
            return None
    except requests.RequestException:
        return None

