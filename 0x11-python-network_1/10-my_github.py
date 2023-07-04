#!/usr/bin/python3
"""Python script that takes credential from GitHub API to display your id"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    authorized = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=authorized)
    print(response.json().get("id"))
