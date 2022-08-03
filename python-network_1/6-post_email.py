#!/usr/bin/python3
""" requesting posting to
    a web link """
import sys
import requests


if __name__ == "__main__":
    # create dictionary of data to post
    res = requests.post(url=sys.argv[1], json={'email':sys.argv[2]})
    print(res.content)
