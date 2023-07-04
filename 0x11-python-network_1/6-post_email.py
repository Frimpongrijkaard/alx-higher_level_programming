#!/usr/bin/python3
import sys
import requests

def post_an_emai(url, email):
    """send a post post request to the passed URL with the email as a parameter"""
    data = {"Email" : email}
    response = requests.post(url, data=data)
    p_request = response.get('Email')
    print("Your email is: {}".format(p_request))

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_an_email(url, email)
