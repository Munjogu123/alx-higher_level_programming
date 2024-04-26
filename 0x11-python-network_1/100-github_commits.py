#!/usr/bin/python3
"""
lists 10 commits from a repository
"""
import requests
import sys

if __name__ == '__main__':
    url = f'https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits'

    response = requests.get(url)
    commits = response.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
