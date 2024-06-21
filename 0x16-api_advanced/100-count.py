#!/usr/bin/python3
"""
Queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after='', count_dict=None):
    """
    Recursive function to query the Reddit API, parse the titles of all hot articles,
    and count the occurrences of specified keywords.
    """
    if count_dict is None:
        count_dict = {word.lower(): 0 for word in word_list}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'AugustBot'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data')
    after = data.get('after')

    for post in data.get('children'):
        title = post.get('data').get('title').lower().split()
        for word in word_list:
            count_dict[word.lower()] += title.count(word.lower())

    if after is None:
        sorted_counts = sorted(count_dict.items(), key=lambda item: (-item[1],
                                                                     item[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f'{word}: {count}')
        return

    return count_words(subreddit, word_list, after, count_dict)

