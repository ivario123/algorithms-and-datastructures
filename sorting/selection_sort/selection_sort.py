def select(array):
  """
    Selects the smallest element in the list and delets it in O(n) time
  """
  smallest, smallest_index = array[0],0
  for i in range(1,len(array)):
    if smallest > array[i]:
      smallest = array[i]
      smallest_index = i
  return smallest_index

def selection_sort(array):  
  for i in range(0,len(array)):
    smallest_index = select(array[i:])
    array[i],array[smallest_index+i] = array[smallest_index+i],array[i]
l = [1,2,5,7,7,1,1,2,2,6,6,4]
selection_sort(l)
print(l)