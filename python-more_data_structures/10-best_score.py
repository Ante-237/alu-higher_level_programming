#!/usr/bin/python3


def best_score(a_dictionary):
    if len(a_dictionary) <= 0:
        return "None"
    elif len(a_dictionary) > 0:
        list_me = dict(sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True))
        return list_me.keys()[0]
    else:
        return "None"
