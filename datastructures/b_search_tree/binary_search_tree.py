
class binary_tree_node:
    def __init__(self,value:int=None,left = None, right = None, parent = None, number_of_children:list = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.number_of_children = number_of_children if number_of_children else [0,0,0]
    
    def search(self,value):
        if self.value == value:
            return self
        if value > self.value:
            if self.right :
                return self.right.search()
        else:
            if self.left:
                return self.left.search()
        return None
        
class binary_tree:
    def __init__(self,root_value:int = None, root:binary_tree_node = None ):
        if root:
            self.root = root
        elif root_value:
            self.root = binary_tree_node(root_value)
        else:
            self.root = None
    
    def insert(self,value):
        if not self.root:
            self.root = binary_tree_node(value)
            return
        node = self.root
        while node:
            node.number_of_children[2]+=1
            if value > node.value:
                # Going right
                node.number_of_children[1]+=1
                if node.right:
                    node = node.right
                else:
                    node.right = binary_tree_node(value,parent = node)
                    break
            else:
                node.number_of_children[0]+=1
                if node.left:
                    node = node.left
                else:
                    node.right = binary_tree_node(value,parent = node)
                    break
    def binary_tree_from_sorted_list(list):
        new_root = binary_tree.binary_tree_from_sorted_list_helper(list,0,len(list)-1)
        return binary_tree(root = new_root)
        
    def binary_tree_from_sorted_list_helper(list,lower,upper) -> binary_tree_node:
        if lower == upper:
            return binary_tree_node(list[upper])
        middle = (lower+upper)//2
        new_root = binary_tree_node(middle)
        new_root.left = binary_tree.binary_tree_from_sorted_list_helper(list,lower,middle)
        new_root.left.parent = new_root
        new_root.right = binary_tree.binary_tree_from_sorted_list_helper(list,middle+1,upper)
        new_root.right.parent = new_root
        return new_root
    def delete(self,value):
        pass
    