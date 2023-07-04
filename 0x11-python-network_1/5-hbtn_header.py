#!/usr/bin/python3
<<<<<<< HEAD
 """python script that takes in url ans return the x-Request-id"""
=======
"""python script that takes in url ans return the x-Request-id"""
>>>>>>> a6af882c77b15d179d46c5296d2dd4407278c658

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
