#!/usr/bin/python3
"""define post request script that response to given email
Usage: ./2-post_email.py <URL> <Email>
    - Display the body of the response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    data = urllib.parse.urlencode({'email' : email}).encode('utf-8')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
