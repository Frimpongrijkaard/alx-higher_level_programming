#!/usr/bin/python3
"""define post request function the response to email"""
import urllib.request
import urllib.parse
import sys

def post_an_email(url, email):
    """function that takes email, and send as post request and display body"""
    data = urllib.parse.urlencode({'email' : email}).encode('utf-8')
    request = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print("Your email is: {}".format(body))

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_an_email(url, email)
