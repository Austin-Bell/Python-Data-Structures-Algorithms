# define function with two arguments a list and target to be found
def linear_search(search_list, target_value):
    # iterate over list argument
  for idx in range(len(search_list)):
      # if target value is found return index where it was located
    if search_list[idx] == target_value:
      return idx
      # if target value not found raise error
  raise ValueError("{0} not in list".format(target_value))

