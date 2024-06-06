#!/usr/bin/python3
"""
Module for querying all hot articles of a subreddit recursively
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all
    hot articles for a given subreddit. If no results are found for the given
    subreddit, the function should return None.

    :param subreddit: The name of the subreddit
    :param hot_list: The list of hot article titles
    :param after: The parameter for pagination
    :return: List of titles or None if invalid subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User-Agent for Project'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts and not hot_list:
                return None

            hot_list.extend(post.get('data', {}).get('title', "None") for post in posts)

            after = data.get('data', {}).get('after', None)
            if after is None:
                return hot_list
            return recurse(subreddit, hot_list, after)
        else:
            return None
    except requests.RequestException:
        return None

