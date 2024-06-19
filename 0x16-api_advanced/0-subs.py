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

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """
    client_id = 'I89Gxobf1Iskg-ZjHb_9cg'
    client_secret = '68NzNnNJqk3g0dVDprHo6eORqQepeQ'
    username = 'AugustinosAbusaif '
    password = 'Alx@123#!'
    token = get_reddit_token(client_id, client_secret, username, password)

    if not token:
        print("Failed to get access token")
        return 0

    url = f'https://oauth.reddit.com/r/{subreddit}/about'
    headers = {'Authorization': f'bearer {token}', 'User-Agent': 'myAPIbot/0.1'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return 0
