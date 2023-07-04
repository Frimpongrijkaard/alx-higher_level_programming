#!/usr/bin/python3
"""send a post post request to the passed URL with the email as a parameter"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    mail = {"email": sys.argv[2]}

    response = requests.post(url, data=mail)
    print(response.text)
