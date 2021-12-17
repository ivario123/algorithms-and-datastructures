class heap:
  def __init__(self,max_size:int = 10,heap:list=None):
    if heap:
      self.heap = heap
      self.size = len(heap)
    else:
      self.heap = []*max_size
      self.size = 0
  def parent(pos):
    return (pos-1)//2 if pos > 0 else None
  def right_child(pos):
    return 2*pos+2
  def left_child(pos):
    return 2*pos+1
  
  def swap(self,pos):
    parent = heap.parent(pos)
    self.heap[pos],self.heap[parent] = self.heap[parent],self.heap[pos]
  def __repr__(self) -> str:
      return str(self.heap)


    
