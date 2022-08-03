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
    try:
        response = requests.post(url,data={'q',first_argv}).json()
        if 'id' in response and 'name' in response:
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
