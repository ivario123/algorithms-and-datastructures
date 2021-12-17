class hash_table:
  def __init__(self,hashing_function,i:int = 0,uses_i = True,table_size:int=1,i_max= 9):
    self.hash_table = [float("-inf")]*table_size
    self.hashing_function = hashing_function
    self.table_size = table_size
    self.i_max = i_max
  def hash_using_i(self,value):
    i = 0
    hash_key = self.hashing_function(value,i)
    while self.hash_table[hash_key]!=float('-inf'):
      i+=1
      hash_key = self.hashing_function(value,i)
    self.hash_table[self.hashing_function(value,self.i)] = value

  def hash_using_extend(self,value):
    hash_key = self.hashing_function(value)
    if self.hash_table[hash_key] == float('-inf'):
      self.hash_table[hash_key] = [value]
      return
    self.hash_table[hash_key].append(value) 
  def lookup_using_extend(self,value):
    hash_key = self.hashing_function(value)
    if self.hash_table[hash_key] == float('-inf'):
      return None
    return hash_key, self.hash_table[hash_key]
    
  def lookup_using_i(self,value,i=0):
    i = 0
    hash_key = self.hashing_function(value,i)
    while self.hash_table[hash_key]!=value and i <=self.i_max:
      i+=1
      hash_key = self.hashing_function(value,i)
    if i > self.i_max:
      return None
    return hash_key,i

