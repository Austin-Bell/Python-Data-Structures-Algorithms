# Import randrange to produce a random index
from random import randrange, shuffle

# Define quicksort function
def quicksort(list, start, end):
    if start >= end:
        return list

    # Define your pivot variables below
    pivot_idx = randrange(start, end)

    # Swap the elements in list below
    pivot_element = list[pivot_idx]
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # Create lesser the lesser_than pointer
    lesser_than_pointer = start

    # Start a for loop, use 'idx' as the variable
    for idx in range(start, end):
        # Check if the value at idx is less than the pivot
        if list[idx] < pivot_element:
      # If so: 
        # 1) swap lesser_than_pointer and idx values
            list[lesser_than_pointer], list[idx] = list[idx], list[lesser_than_pointer]

        # 2) increment lesser_than_pointer
            lesser_than_pointer += 1
    
    # After the loop is finished...
    # swap pivot with value at lesser_than_pointer
    list[end], list[lesser_than_pointer] = list[lesser_than_pointer], list[end]

    # Call quicksort on the "left" and "right" sub-lists
    return quicksort(list, start, lesser_than_pointer - 1), quicksort(list, lesser_than_pointer + 1, end)
