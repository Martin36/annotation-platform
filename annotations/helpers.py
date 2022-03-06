

from typing import List


def find_first_missing_int(int_list: List[int]):
  """Find the first consequtive int that is missing 
  e.g. if the list contains the following elements [1, 2, 4, 7] 
  it returns 3
  For empty lists it returns 1
  For lists with complete sequences it returns the next int after 
  the largest in the list
  
  Args:
      list (List[int]): The list in which to find the first missing int
  """
  
  if len(int_list) == 0:
    return 1
  # Remove duplicates and sort
  int_list = sorted(list(set(int_list)))
  prev_i = None
  for i in int_list:
    if prev_i and prev_i+1 != i:
      return prev_i+1
    prev_i = i
  # If no int is missing, return the next one in the sequence
  return int_list[-1]+1