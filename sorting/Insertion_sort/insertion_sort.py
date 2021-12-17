def insertion_sort(array):
  """
    Sorts a list in O(n^2) time in the worstcase 
  """
  for i in range(0,len(array)):
    pointer = i
    while pointer > 0 and array[pointer] < array[pointer-1]:
      array[pointer],array[pointer-1] = array[pointer-1],array[pointer]
      pointer-=1