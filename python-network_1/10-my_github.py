#!/usr/bin/python3
""" get user id
    from github
"""
import sys
import requests


user_name = "Ante-237"

if __name__ == "__main__":
    res = requests.get('https://api.github.com/user',auth=(sys.argv[1], sys.argv[2]))
    if 'id' in res:
        print(res['id'])
    else:
        print(None)
