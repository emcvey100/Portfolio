"""
Bubble Sort
An algorithm that compares the item next to it until the list is sorted.
"""

def bubble_sort(sorting_list):
	"""
	Sorts inputted list using the bubble sort algorithm.
	Parameters:
	    sorting_list(list): An unsorted list of items that needs to be sorted.
	Returns:
        list: A sorted list of the given sorting_list.
	"""
	for end in range(len(sorting_list) - 1, 0, -1): #loops decreasing end to reduce list size
		swapped = False
		for index in range(end): #traverse list up to end amount
			if sorting_list[index] > sorting_list[index + 1]:#Swap if bigger
				sorting_list[index], sorting_list[index + 1] = sorting_list[index + 1], sorting_list[index]
				swapped = True
		if not swapped:
			break
	return sorting_list #return list

def decreasing_bubble_sort(sorting_list):
	"""
	Sorts in decresing order inputted list decreasinglyusing the bubble sort algorithm.
	Parameters:
	    sorting_list(list): An unsorted list of items that needs to be sorted.
	Returns:
        list: A sorted list of the given sorting_list.
	"""
	for end in range(len(sorting_list) - 1, 0, -1): #loops decreasing end to reduce list size
		swapped = False
		for index in range(end): #traverse list up to end amount
			if sorting_list[index] < sorting_list[index + 1]: #Swap if smaller
				sorting_list[index], sorting_list[index + 1] = sorting_list[index + 1], sorting_list[index]
				swapped = True
		if not swapped:
			break
	return sorting_list #return list
