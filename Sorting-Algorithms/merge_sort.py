def merge_sort(items):
    # if parameter items as a list is empty or has a single element return list
    if len(items) <= 1:
        return items

    # Split initial array as evenly as possible
    middle_index = len(items) // 2

    left_split = items[:middle_index]
    right_split = items[middle_index:]

    # Recursively call merge_sort until there are lists with only one element
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)


    return merge(left_sorted, right_sorted)




# Helper function to sort the list by checking if the left value is smaller than the right value
def merge(left, right):
    results = []

    while (left and right):
        if left[0] < right[0]:
            results.append(left[0])
            left.pop(0)
        else:
            results.append(right[0])
            right.pop(0)

    # Adds remaining elements in the left sublist    
    if left:
        results += left
    # Adds remaining elements in the right sublist    
    if right:
        results += right
    
    return results

