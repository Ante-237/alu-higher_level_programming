#!/usr/bin/python3
""" send a request and
getting a particular header
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers['X-Request-Id'])
