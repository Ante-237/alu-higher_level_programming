#!/usr/bin/python3
""" requesting posting to
    a web link """
import sys
import requests


if __name__ == "__main__":
    # create dictionary of data to post
    data = {'email', sys.argv[2]}
    res = requests.post(sys.argv[1], data)
    print(res.content)
