#!/usr/bin/python3
"""define a script that take url, send and display X_id"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        content_id = response.headers.get('X-Request-Id')
        print(content_id)
