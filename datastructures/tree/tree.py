from typing_extensions import runtime


class tree_node:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None
        self.parent = None

    def insert_right(self, value):
        """
          O(1) since we are not itterating just inserting a new element 
        """
        if type(value) == tree_node:
          self.right_child = value
        else:
          self.right_child = tree_node(value)
        self.right_child.parent = self

    def insert_left(self, value):
        """
          O(1) since we are not altering the list just extending it.
          If however we need to itterate it becomes O(log(n)) worst case.
        """
        if type(value) == tree_node:
            self.left_child = value
        else:
            self.left_child = tree_node(value)
        self.left_child.parent = self
    
    def get_level(self):
        """
          O(log(n)) implementation since there are log(n) levels in a (balanced) tree 
        """
        if self.parent == None:
            return 0
        return 1+self.parent.get_level()
    def get_level_child(self,value,found=0,levels=0):
      """
        O(n) worst case implementation
        Kinda slow since we can't make anny assumptions regarding the order of the list
      """

      if type(value) == tree_node:
        value = value.value
      # catch find root 
      if self.value == value:
        return 1,levels
      # Catch find child

      if (self.left_child != None and self.left_child.value == value) or (self.right_child != None and self.right_child.value == value):
        return 1,levels+1
      # Don't continue down the tree if we are at a leaf
      if self.left_child != None:
        in_left,levels = self.left_child.get_level_child(value,0,levels+1)
        if in_left:
          return 1,levels+1
      # Don't continue down the tree if we are at a leaft
      if self.right_child!=None:
        in_right,levels = self.right_child.get_level_child(value,levels+1)
        if in_right:
          return 1,levels+1
      # return 0,0 if nothing is found
      return 0,0
      
      

    def __repr__(self) -> str:
        return f"Current element : {self.value}, left child = {self.left_child}, right child = {self.right_child}"


def test_tree():
    print("Testing the tree datastructure")
    root = tree_node("Schools")

    good = tree_node("Good schools")
    LTU = tree_node("LTU")
    good.insert_right(LTU)

    bad = tree_node("Bad schools")
    bad.insert_left("KTH")

    root.insert_right(bad)
    root.insert_left(good)
    print(root)
    print(LTU.get_level())
    print(root.get_level_child("KTH"))
if __name__ == "__main__":
  test_tree()