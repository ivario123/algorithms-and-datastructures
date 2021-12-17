class queue :
  def __init__(self,current_que : list= None):
    self.queue = current_que if current_que else []
    self.numel = len(queue)

  def enque(self,value):
    self.queue = self.queue+[value]
    self.numel+=1
  def deque(self):
    val = self.queue [0]
    self.queue = self.queue [1:self.numel-1]
    self.numel-=1
    return val
  def next_in_line(self):
    return self.queue[0]
  def last_in_line(self):
    return self.queue[self.numel-1]


