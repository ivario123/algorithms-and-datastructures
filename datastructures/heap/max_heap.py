from heap import heap
class max_heap(heap):
  
  def insert(self,value):
    if self.size > len(self.heap)-1:
      self.heap.append(value)
    else:
      self.heap[self.size] = value

    current_index = self.size

    while heap.parent(current_index)!= None  and self.heap[current_index] > self.heap[heap.parent(current_index)]:
      self.swap(current_index)
      current_index = heap.parent(current_index)
    self.size+=1
  def Print(self):
        print(self.heap)

if __name__ == "__main__":
  _heap = max_heap()
  _heap.insert(1)
  _heap.insert(2)
  _heap.insert(3)

  _heap.insert(4)
  _heap.insert(5)
  _heap.insert(6)
  _heap.insert(7)
  _heap.insert(9)
  _heap.insert(-1)
  _heap.Print()

