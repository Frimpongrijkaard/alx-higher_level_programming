#!/usr/bin/python3
import sys
import urllib.request
from urllib.error import HTTPError

def Error_code(url):
    """function that display Error code from url"""
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as respomse:
            body = response.read().encode('utf-8')
    execpt HTTPError as e:
        print("Error code: {}".format(e.code))

if __name__ == "__main__":
    url = sys.argv[1]
    Error_code(url)
