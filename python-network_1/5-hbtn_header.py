#!/usr/bin/python3
""" send a request and
getting a particular header
"""
import requests
import sys


url = 'https://intranet.hbtn.io'

if __name__ == "__main__":
    r = requests.get(url)
    dict_got = r.headers
    print(dict_got['x-request-id'])
