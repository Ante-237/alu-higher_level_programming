#!/usr/bin/python3


def best_score(a_dictionary):
    list_me = list(sorted(a_dictionary, key=lambda x : x[1], reverse=True))
    return list_me[0]
