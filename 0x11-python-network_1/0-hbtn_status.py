#!/usr/bin/python3

<<<<<<< HEAD
"""define a function that fetch url content"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
=======
"""define a function that fetch url content
Usage: ./0-bntn_status.py

"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"""

>>>>>>> dd68ababf31684a9a1dd71c605ac30bcb4aa1b18
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

<<<<<<< HEAD
        print("Body response:")
        print("\t- type: {} ".format(type(content)))
        print("\t- content: {} ".format(content))
        print("\t- utf8 content: {}".format(utf8_cont))
=======
    print("Body response:")
    print("\t- type: {} ".format(type(content)))
    print("\t- content: {} ".format(content))
    print("\t- utf8 content: {}".format(utf8_content))

>>>>>>> dd68ababf31684a9a1dd71c605ac30bcb4aa1b18
