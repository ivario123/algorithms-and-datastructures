def merge(left,right):
  """
    Merges 2 lists in O(m+n)
  """
  ret = []
  while left or right:
    if not left:
      ret.extend(right)
      return ret
    elif not right:
      ret.extend(left)
      return ret
    if left[0]>right[0]:
      ret.append(right[0])
      del right[0]
    else:
      ret.append(left[0])
      del left[0]
  return ret

def merge_sort(array):
  """
    Sorts a list using log(n) divisions where each division takes O(n+m) time, thus the entire sorting takes O(nlogn) time 
  """
  if len(array)==1:
    return array
  mid = (len(array))//2
  left = merge_sort(array[:mid])
  right = merge_sort(array[mid:])
  return merge(left,right)