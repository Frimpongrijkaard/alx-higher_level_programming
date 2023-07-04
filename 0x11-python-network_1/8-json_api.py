#!/usr/bin/python3
import requests
import sys

def  Search_API(q):
    """function that take letter and send post to url"""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q' : q}

    response = request.post(url, data=data)
    json_d = response.json()
    if isinstance(json_d, dict):
        if 'id' in json_d and 'name' in json_d:
            print("[{}] {}".format(json_d['id'], json_d['name']))
        else:
            print("No result")
    else:
        print("Not a valid JSON")

if __name__ == "__main__":
    q = sys.argv[1]
    if len(q) < 2:
        q = " "
    else:
        q = sys.argv[1]
    search_API(q)
