class stack:
  def __init__(self,current_stack:list = None) -> None:
      self.stack = current_stack if current_stack else []
      self.numel = len(current_stack)
  def push(self,value):
    self.stack = [value]+self.stack
    self.numel+=1
  def pop(self):
    val = self.stack[0]
    self.stack = self.stack[1:self.numel-1]
    self.numel-=1
    return val
  def next(self):
    return self.stack[0]
  def last(self):
    return self.stack[self.numel-1]
  def __repr__(self) -> str:
    return str(self.stack)
