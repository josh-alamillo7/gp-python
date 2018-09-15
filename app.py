def remove_empty_lists(input_list):

  #iterate through the list.
    #if the current element is an empty list, remove it.
    #if it's not empty and it's a list, pass that list into remove_empty_lists
  def is_empty(test_list):

    curr_list = test_list
    if len(curr_list) != 1:
      return False
    while len(curr_list) == 1:
      curr_element = curr_list[0]
      if type(curr_element) is not list:
        return False
      if type(curr_element) is list and not curr_element:
        return True
      curr_list = curr_element
    return False

  curr_index = 0
  copy_list = input_list[:]
  for element in copy_list:
    if type(element) is list and not element:
      input_list.remove(element)
      curr_index = curr_index - 1
    elif type(element) is list:
      if (is_empty(element)):
        input_list.remove(element)
        curr_index = curr_index - 1
      else:
        copy_element = element[:]
        emptied_list = remove_empty_lists(copy_element)
        input_list[curr_index] = emptied_list
    curr_index = curr_index + 1

  return input_list

print remove_empty_lists([[], 4, [], [[], 8, []], 'hey'])
#should print [4, [8], 'hey']
print remove_empty_lists([[[]], [[[]]], [7, [[]]], [8, []], [[2, []], [], 9]])
#should print [[7], [8], [[2]], 9]