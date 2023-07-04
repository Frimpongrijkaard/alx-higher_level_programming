#!/usr/bin/python3
"""define a function that fetch url content"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"""


    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
        print("Body response:")
        print("\t- type: {} ".format(type(content)))
        print("\t- content: {} ".format(content))
        print("\t- utf8 content: {}".format(utf8_cont))
