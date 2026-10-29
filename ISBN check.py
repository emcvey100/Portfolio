import requests
import json

def ISBN_check13(ISBN):
    '''Check if ISBN is valid'''
    if len(ISBN) != 13:
        return False
    total = 0
    for i in range(12):
        if i % 2 == 0:
            total += int(ISBN[i])
        else:
            total += int(ISBN[i]) * 3
    check_digit = (10 - (total % 10)) % 10
    return check_digit == int(ISBN[12])

def ISBN_check10(ISBN):
    '''Check if ISBN is valid'''
    if len(ISBN) != 10:
        return False
    total = 0
    for i in range(9):
        total += int(ISBN[i]) * (10 - i)
    check_digit = (11 - (total % 11)) % 11
    if check_digit == 10:
        return ISBN[9] == 'X'
    else:
        return check_digit == int(ISBN[9])

def find_ISBN_type(ISBN):
    '''Find if ISBN is 10 or 13'''
    if len(ISBN) == 10:
        return '10'
    elif len(ISBN) == 13:
        return '13'
    else:
        return None

def check_ISBN(ISBN):
    '''Check if ISBN is valid'''
    if len(ISBN) == 10:
        return ISBN_check10(ISBN)
    elif len(ISBN) == 13:
        return ISBN_check13(ISBN)
    else:
        return False
