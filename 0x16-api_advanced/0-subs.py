import requests
from sys import argv

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    user_agent = {'User-Agent': 'Lizzie'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get('data', {}).get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0

if __name__ == "__main__":
    if len(argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(argv[1])))
