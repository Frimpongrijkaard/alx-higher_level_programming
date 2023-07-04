#!/usr/bin/python3
"""define post request function the response to email"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    data = urllib.parse.urlencode({'email' : email}).encode('utf-8')
    request = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
