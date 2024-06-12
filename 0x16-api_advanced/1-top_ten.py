#!/usr/bin/python3
"""
Module for querying the top ten hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If not a valid subreddit, print None.
    
    :param subreddit: The name of the subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User-Agent for Project'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print("None")
                return
            for post in posts:
                print(post.get('data', {}).get('title', "None"))
        else:
            print("None")
    except requests.RequestException as e:
        print("None")

