Name: 
    Bubble Sort
Type: 
    Sorting algorithm
Description:
    A sorting algorithm which repeats swaping adjacent elements when they are in the wrong order.
Time Complexity:
    O(n2)
Auxiliary Space:
    O(1)
Pseudocode:
    1. Look at first item in list
    2. Compare to the next item in list
    3. If the next number is smaller then swap items else do not swap
    4. Move to the next item in list
    5. Repeat step 2-4 until at the last number of list
    6. If any numbers were swapped in the list then repeat from step 1 but step 5 being 1 less item.
    7. If no swaps in list then the list is sorted
    8. Algorithm ends.
Example:
    [7, 9, 2, 1, 3] //initial list to sorted
    [(7, 9), 2, 1, 3]//7 and 9 are in correct order, go to next step
    [7, (9, 2), 1, 3]//9 > 2 so swap them
    [7, 2, (9, 1), 3]//9 > 1 so swap them
    [7, 2, 1, (9, 3)]//9 > 1 so swap them, swap in list so go back to item 1
    [(7, 2), 1, 3, 9]//7 > 2 so swap them
    [2, (7, 1), 3, 9]//7 > 1 so swap them
    [2, 1, (7, 3), 9]//7 > 3 so swap them, swap in list so go back to item 1
    [(2, 1), 3, 7, 9]//2 > 1 so swap them
    [1, (2, 3), 7, 9]//2 and 3 are in the correct order, swap in list so go back to item 1
    [(1, 2), 3, 7, 9]// 1 and 2 are in the correct order, no swap in list so in correct order #sorted 
Advantages:
    * Easy to understand
    * Easy to implement
    * no additional memory Space
    * a stable sorting algorithm
Disadvantages:
    * time complexity of O(n2) so slow for large data sets
    * limited application
