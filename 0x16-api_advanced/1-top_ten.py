#!/usr/bin/python3
"""API advanced project"""
import requests


def get_reddit_token(client_id, client_secret, username, password):
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {'grant_type': 'password', 'username': username, 'password': password}
    headers = {'User-Agent': 'Augustbot/0.1'}

    response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    response.raise_for_status()
    token = response.json().get('access_token')
    return token

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If not a valid subreddit, prints None.
    """
    client_id = 'I89Gxobf1Iskg-ZjHb_9cg'
    client_secret = '68NzNnNJqk3g0dVDprHo6eORqQepeQ'
    username = 'AugustinosAbusaif'
    password = 'Alx@123#!'
    token = get_reddit_token(client_id, client_secret, username, password)

    if not token:
        print("Failed to get access token")
        return

    url = f'https://oauth.reddit.com/r/{subreddit}/hot'
    headers = {'Authorization': f'bearer {token}', 'User-Agent': 'myAPIbot/0.1'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException as e:
        print(None)
