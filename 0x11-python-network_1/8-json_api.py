#!/usr/bin/python3
"""python script that take letter and send post to url
Usage: ./8-json_api.py <letter>

"""
import requests
import sys

if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]


    url = "http://0.0.0.0:5000/search_user"
    data = {'q' : q}

    response = request.post(url, data=data)
    try:
        json_d = response.json()
        if isinstance(json_d, dict):
            if 'id' in json_d and 'name' in json_d:
                print("[{}] {}".format(json_d['id'], json_d['name']))
            else:
                print("No result")
    except ValueError:
        print("Not a valid JSON")


