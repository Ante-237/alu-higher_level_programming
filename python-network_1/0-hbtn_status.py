#!/usr/bin/python3
import urllib.request
""" module uses another module to request to make request """



if __name__ == "__main__":
    """making request to provided url"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print("  - type: {}".format(type(html)))
        print("  - content: {}".format(html))
        temp = str(html)
        print("  - utf8 content: {}".format(temp[2:-1]))
