sequence = ['A','B','C','D']

#Example 1 - A while loop
position = 0
while position < len(sequence):
    print(sequence[position], "is at position", str(position))
    position += 1

#Example 2 - A for loop over a range
for position in range(len(sequence)):
    print(sequence[position], "is at position", str(position))

#Example 3 - The enumerate function
for position, item in enumerate(sequence):
    print(item, "is at position", position)
