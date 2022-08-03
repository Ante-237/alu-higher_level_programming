#!/usr/bin/python3
""" sending a post request """
import requests
import sys


if __name__ == "__main__":
    # handling arguments
    first_argv = sys.argv[1]
    if first_argv == None:
        first_argv = ""
    url = 'http://0.0.0.0:5000/search_user'
    response = request.post(url,{'q',first_argv})
    if response.text:
        if isintance(response.text,json):
            print(response.text)
