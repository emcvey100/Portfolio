"""
Recursive Bubble Sort
An algorithm that compares the item next to it until the list is sorted.
"""


def recursive_bubble_sort(sorting_list):
	"""
	Sorts inputted list using the recursive bubble sort algorithm.
	Parameters:
	    sorting_list(list): An unsorted list of items that needs to be sorted.
	Returns:
        list: A sorted list of the given sorting_list.
	"""
	swapped = True
	while swapped: #loops if list isnt sorted
		swapped = False
		for index in range(len(sorting_list)-1): #traverse list
			if sorting_list[index] > sorting_list[index + 1]:#Swap if bigger
				sorting_list[index], sorting_list[index + 1] = sorting_list[index + 1], sorting_list[index]
				swapped = True
	return sorting_list #return list

def decresing_recursive_bubble_sort(sorting_list):
	"""
	Sorts in decreasing order inputted list using the recursive bubble sort algorithm.
	Parameters:
	    sorting_list(list): An unsorted list of items that needs to be sorted.
	Returns:
        list: A sorted list of the given sorting_list.
	"""
	swapped = True
	while swapped: #loops if list isnt sorted
		swapped = False
		for index in range(len(sorting_list)-1): #traverse list
			if sorting_list[index] > sorting_list[index + 1]:#Swap if bigger
				sorting_list[index], sorting_list[index + 1] = sorting_list[index + 1], sorting_list[index]
				swapped = True
	return sorting_list #return list