#! /usr/bin/env python3
#-*- coding: utf-8 -*-


def dict_from_str(my_str):
    """
    A simple function which returns
    a dict whose keys/values are
    my_str's letters and their occurrences.
    """
    
    my_dict = dict()
    for letter in my_str:
        if my_dict.get(letter, False):
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1
    return my_dict


def anagrams(first_str, second_str):
    """
    A simple function which test if
    two strings are anagrams.
    """
    
    if not len(first_str) == len(second_str):
        return False
    return dict_from_str(first_str) == dict_from_str(second_str)


if __name__ == '__main__':
    str_one = "bored"
    str_two = "robed"
    print(str_one, str_two, " are " if anagrams(str_one, str_two) else " are not ", "anagrams")

    str_one = "night"
    str_two = "thing"
    print(str_one, str_two, " are " if anagrams(str_one, str_two) else " are not ", "anagrams")

    str_one = "dream"
    str_two = "derma"
    print(str_one, str_two, " are " if anagrams(str_one, str_two) else " are not ", "anagrams")
 
    str_one = "mother"
    str_two = "other"
    print(str_one, str_two, " are " if anagrams(str_one, str_two) else " are not ", "anagrams")

    str_one = "ABBA"
    str_two = "ACAB"
    print(str_one, str_two, " are " if anagrams(str_one, str_two) else " are not ", "anagrams")
    
