#!/usr/bin/python3

import sys
import requests

def response_header_value(url):
    """function that takes in url ans return the x-Request-id"""
    response = requests.get(url)
    value = response.headers.get("X-Request-Id")
    print(value)

if __name__ == "__main__":
    url = sys.argv[1]
    response_header_value(url)
