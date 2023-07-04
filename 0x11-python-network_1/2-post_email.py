#!/usr/bin/python3
""" post request script that response to given email.
Usage: ./2-post_email.py <URL> <Email>
    - Display the body of the response.
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    mail = {"email" : sys.argv[2]}
    
    data = urllib.parse.urlencode(mail).encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
        print(body)
