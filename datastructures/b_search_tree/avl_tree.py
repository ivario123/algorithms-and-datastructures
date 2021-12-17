from binary_search_tree import*
class avl_tree_node(binary_tree_node):
    def rotate_left(self):
        
        if not self.right:
            return self
        new_root_children = [self.number_of_children[0]+self.right.number_of_children[0]+1,self.right.number_of_children[1],0]
        new_root_children[2] = new_root_children[0]+new_root_children[1]
        new_root = binary_tree_node(self.value,parent = self.parent,right = self.right.right,left = self,number_of_children=new_root_children)
        self.right = self.right.left
        if self.right:
            self.number_of_children[1] = self.right.number_of_children[2]+1
        else:
            self.number_of_children[1] = 0