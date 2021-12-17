class hash_table:
  def __init__(self,hashing_function,i:int = 0,uses_i = True):
    self.hash_table = {"":""}
    self.hashing_function = hashing_function
    self.uses_i = uses_i
    self.i = i
  def hash(self,value):
    if self.uses_i:
      self.hash_table[self.hashing_function(value,self.i)] = value
    else:
      self.hash_table[self.hashing_function(value)] = value
    self.i+=1
    return self.i-1
  def lookup(self,value,i=0):
    if self.uses_i:
      return self.hash_table[self.hashing_function(value,i)]
    return self.hash_table[self.hashing_function(value)]

