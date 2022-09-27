#!/usr/bin/python3
""""""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    user = {'User-Agent': 'Test123'}
    response = requests.get(url, headers=user, allow_redirects=False)
    if response.status_code == 404:
        return None
    data = response.json().get('data')
    after = data.get('after')
    for post in data.get('children'):
        if post.get('title') in hot_list:
            return hot_list
        hot_list.append(post.get('data').get('title'))
    return recurse(subreddit, hot_list, after)
