#!/usr/bin/python3
"""
Module for counting keywords in titles of hot articles of a subreddit recursively
"""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """
    Queries the Reddit API and parses the title of all hot articles,
    printing a sorted count of given keywords (case-insensitive).

    :param subreddit: The name of the subreddit
    :param word_list: List of keywords to count
    :param counts: Dictionary to store the counts of keywords
    :param after: The parameter for pagination
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User-Agent for Project'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts and not counts:
                return

            if not counts:
                counts = {word.lower(): 0 for word in word_list}

            for post in posts:
                title = post.get('data', {}).get('title', "").lower().split()
                for word in word_list:
                    count = title.count(word.lower())
                    counts[word.lower()] += count

            after = data.get('data', {}).get('after', None)
            if after is None:
                sorted_counts = sorted(
                    [(k, v) for k, v in counts.items() if v > 0],
                    key=lambda item: (-item[1], item[0])
                )
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
            else:
                count_words(subreddit, word_list, counts, after)
        else:
            return
    except requests.RequestException:
        return

