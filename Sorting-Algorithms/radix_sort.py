# Define radix sort function wiht a list as an argument
def radix_sort(to_be_sorted):
    
    # In order to determine how many digits are in the longest number in the list, we’ll need to find the longest number.
    maximum_value = max(to_be_sorted)

    # Turn the maximum_value into a string
    max_exponent = len(str(maximum_value))

    # Create copy of to_be_sorted here
    being_sorted = to_be_sorted[:]

    # Create ten different buckts for our numbers 0 - 9
    digits = [[] for digit in range(10)]

    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position

        # Create ten different buckts for our numbers 0 - 9
        digits = [[] for digit in range(10)]

        # Create a for loop here:
        for number in being_sorted:
            number_as_a_string = str(number)
            try:
                digit = number_as_a_string[index]
                digit = int(digit)
            except IndexError:
                digit = 0

            digits[digit].append(number)

    # reassign being_sorted here:
        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)

    return being_sorted


