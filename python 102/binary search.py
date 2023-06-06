def binary_search(sorted_list, value):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = int((left + right)/2)
        if sorted_list[mid] > value:
            right = mid - 1
        elif sorted_list[mid] < value:
            left = mid + 1
        elif sorted_list[mid]==value:
            return True
        else:
            return mid
    return False
from random import randint

sorted_list = [i + randint(0,9) for i in range(0,100,10)]
