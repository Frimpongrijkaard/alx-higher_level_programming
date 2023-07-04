#!/usr/bin/python3

import sys
import requests

def Error_short_code(url):
    """function that takes url and send a request to url"""
    response = requests.get(url)
    code = response.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(response.text)

if __name__ == "__main__":
    url = sys.argv[1]
    Error_short_code(url)
