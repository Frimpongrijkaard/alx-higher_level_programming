#!/usr/bin/python3
import requests

def my_status(url):
    """function that fetch url"""
    response = requests.get(url)
    body = response.json()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}". format(body))

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    my_status(url)
