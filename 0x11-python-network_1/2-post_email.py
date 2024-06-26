#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter,
and displays the body of the response
"""
import urllib.parse
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
