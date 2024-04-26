#!/usr/bin/python3
"""
lists 10 commits from a repository
"""
import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[1], sys.argv[2]
    )

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
