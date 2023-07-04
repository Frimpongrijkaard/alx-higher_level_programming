#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password) 
and uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    headers = {"Authentication": f"Token {access_token}"}
    url = "https://api.github.com/user"
    response = requests.get(url, headers=headers)
    code = response.status_code

    if code == 200:
        json_d = response.json()
        j_id = json_d.get('id')
        if j_id:
            print(j_id)
        else:
            print("None")
    else:
        print("None")

