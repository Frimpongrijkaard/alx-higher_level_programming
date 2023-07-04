#!/usr/bin/python3
 """python script that takes in url ans return the x-Request-id"""


import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
