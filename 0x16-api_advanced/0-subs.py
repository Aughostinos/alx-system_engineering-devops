#!/usr/bin/python3
"""api advanced project"""
import praw
import sys


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given
    subreddit. If an invalid subreddit is given, returns 0.
    """
    reddit = praw.Reddit(
        client_id="_VeUTcfD1A12_rL3fxvyRQ",
        client_secret="u78lzkzPyQs68rNrPuaZTz4mpa1cjA",
        user_agent="AugustBot/0.0.1"
    )
    try:
        subreddit_obj = reddit.subreddit(subreddit)
        return subreddit_obj.subscribers
    except praw.exceptions.PRAWException:
        return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))