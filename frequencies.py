from collections import Counter
"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    string_list = []
    for item in items:
        string_list.append(str(item))
    return Counter(string_list)
