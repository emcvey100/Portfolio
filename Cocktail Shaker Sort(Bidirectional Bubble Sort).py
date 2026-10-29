"""
Cocktail shaker sort (bidirectional bubble sort)
A variation of bubble sort that checks forward and then backwards down the list.
"""

def cocktail_shaker_sort(sorting_list):
    """
    Sorts  inputted list using a variation of bubble sort algorithm called the cocktail shaker sort.
    Parameters:
        sorting_list(list): An unsorted list of items that needs to be sorted.
    Returns:
        list: A sorted list of the given sorting_list.
    """
    start = 0
    end = len(sorting_list) - 1
    swapped = True
    while swapped: #loop if previous loop has swap
        swapped = False 
        for index in range(start, end):#traverse list
            if sorting_list[index] > sorting_list[index + 1]:#swap if bigger
                sorting_list[index], sorting_list[index + 1] = sorting_list[index + 1], sorting_list[index]
                swapped = True
        if not swapped: #check a swap has been made
            break
        end -= 1
        swapped = False
        for index in range(end, start, -1): # traverse list backwards
            if sorting_list[index - 1] > sorting_list[index]:#swap if bigger
                sorting_list[index - 1], sorting_list[index] = sorting_list[index], sorting_list[index - 1]
                swapped = True
        start += 1
    return sorting_list #return list

def decreasing_cocktail_shaker_sort(sorting_list):
    """
    Sorts in decreasing order inputted list using a variation of bubble sort algorithm called the cocktail shaker sort.
    Parameters:
        sorting_list(list): An unsorted list of items that needs to be sorted.
    Returns:
        list: A sorted list of the given sorting_list.
    """
    start = 0
    end = len(sorting_list) - 1
    swapped = True
    while swapped: #loop if previous loop has swap
        swapped = False
        for index in range(start, end): #traverse list
            if sorting_list[index] < sorting_list[index + 1]: #swap if smaller
                sorting_list[index], sorting_list[index + 1] = sorting_list[index + 1], sorting_list[index]
                swapped = True
        if not swapped: #check a swap has been made
            break
        end -= 1
        swapped = False
        for index in range(end, start, -1): #traverse list backwards
            if sorting_list[index - 1] < sorting_list[index]: #swap id smaller
                sorting_list[index - 1], sorting_list[index] = sorting_list[index], sorting_list[index - 1]
                swapped = True
        start += 1
    return sorting_list #return list
