#!/usr/bin/python3
"""
Bu modul safe_print_list funksiyasını təmin edir.
"""


def safe_print_list(my_list=[], x=0):
    """
    Siyahıdan x sayda elementi çap edən funksiya.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
