def index_all(search_list, item):
  # search and index given values in a list
  index_list = []   # where we will store the indicies of where our items are
  for index, value in enumerate(search_list): # numbers each value and index in a list
      if value == item:               # IF we get a match...
        index_list.append([index])    # add the current index (matching the item) to index_list
      elif isinstance(search_list[index], list):        # Checks if the values is another list, if yes
         for i in index_all(search_list[index], item):  # recursively call the function, index_all
            index_list.append([index] + i)              # to search through the new list
            
  return index_list





  # commands used in solution video for reference
if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]
