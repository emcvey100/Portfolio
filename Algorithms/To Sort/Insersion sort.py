"""
Insersion sort
An algorithm comparing each item all the previous items.
"""
def insertion_sort(sorting_list):
	"""
	Sorts inserted list using insersion sort.
	Parameter:

	Returns:
	
	"""
	for index in range(1, len(sorting_list)):
		current = sorting_list[index]
		position = index - 1

		while position >= 0 and sorting_list[position] > current:
			sorting_list[position + 1] = sorting_list[position]
			position -= 1

		sorting_list[position + 1] = current

	return sorting_list
