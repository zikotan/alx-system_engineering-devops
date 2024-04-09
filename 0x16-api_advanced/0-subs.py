#!/usr/bin/python3
"""
This module contains the function number_of_subscribers.
"""

import requests
from sys import argv

def get_subreddit_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    headers = {'User-Agent': 'Lizzie'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching subreddit information: {e}")
        return None
    except KeyError:
        print(f"Invalid subreddit name: {subreddit}")
        return None

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py <subreddit>")
    else:
        subreddit = argv[1]
        subscribers = get_subreddit_subscribers(subreddit)
        if subscribers is not None:
            print(f"Number of subscribers in r/{subreddit}: {subscribers}")
