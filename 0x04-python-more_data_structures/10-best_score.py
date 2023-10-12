#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_score_search = list(a_dictionary.keys())[0]
    for key, value in a_dictionary.items():
        if best_score_search < key:
            best_score_search = key
    return best_score_search
