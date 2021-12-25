from datastructures.heap.min_heap import min_heap
from ...datastructures.heap import *
def heap_sort(self,array):
  heap = min_heap(max_size=len(array))
  heap.