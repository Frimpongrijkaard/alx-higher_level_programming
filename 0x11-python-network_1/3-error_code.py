#!/usr/bin/python3
"""python script  that display Error code from url"""
import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8')
            print(body)
    except HTTPError as e:
        print("Error code: {}".format(e.code))

