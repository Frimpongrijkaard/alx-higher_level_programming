#!/usr/bin/python3
import urllib.request
import sys

"""define a script that take url, send and display X_id"""

def X_request_id(url):
    """function that display the x_request_id"""
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        content_id = response.headers.get('X-Request-Id')
    print(content_id)

if __name__ == "__main__":
    url = sys.argv[1]
    X_request_id(url)
