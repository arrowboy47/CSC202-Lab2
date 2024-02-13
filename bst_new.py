from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left_child: 'Node' = None
    right_child: 'Node' = None

@dataclass
class BinaryTree:
    root: Node = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            # will send child to the bottom left of the tree if the lowest value
            if current_node.left_child is not None:
                self._insert_recursive(current_node.left_child, value)
            else:
                current_node.left_child = Node(value)
        elif value > current_node.value:
            if current_node.right_child is not None:
                self._insert_recursive(current_node.right_child, value)
            else:
                current_node.right_child = Node(value)
        else:
            # Value already exists in the tree, handle as per your requirement.
            raise ValueError("Value already exists in the tree.")

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if not current_node:
            return False
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left_child, value)
        else:
            return self._search_recursive(current_node.right_child, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current_node, value):
        if current_node is None:
            return current_node # If the tree is empty or the node is not found, return None.
       # Recursive calls for ancestors of the node to be deleted.
        if value < current_node.value:
            current_node.left_child = self._delete_recursive(current_node.left_child, value)# Recur down the left subtree if the value is smaller.
        elif value > current_node.value:
            current_node.right_child = self._delete_recursive(current_node.right_child, value) # Recur down the left subtree if the value is greator.
        else:
            # Node with only one child or no child
            if current_node.left_child is None:
                temp_node = current_node.right_child
                del current_node
                return temp_node
            elif current_node.right_child is None:
                temp_node = current_node.left_child
                del current_node
                return temp_node

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            current_node.value = self._find_min_value(current_node.right_child)

            # Delete the inorder successor
            current_node.right_child = self._delete_recursive(current_node.right_child, current_node.value)

        return current_node

    def _find_min_value(self, node):
        current = node
        while current.left_child is not None:
            current = current.left_child
        return current.value
    
    # returns True if the tree is a binary search tree
    # since it is a method of the binary tree class, it is assumed that the tree is a binary tree
    # conditions for a binary search tree:
    # 1. the left subtree of a node contains only nodes with values less than the node's value
    # 2. the right subtree of a node contains only nodes with values greater than the node's value 
    def isBST(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive_bst(self, current_node):
        if current_node is None:
            # whenever we reach a leaf node, we return True
            return True
        else:
            # check conditions of bst
            # check if left child is less than current node value
            if current_node.left_child is not None:
                if current_node.left_child.value > current_node.value:
                    print("Not a BST")
                    return False
            # check if right child is greater than current node value
            if current_node.right_child is not None:
                if current_node.right_child.value < current_node.value:
                    print("Not a BST")
                    return False
            
            # traverse left subtree
            # if left subtree is not a bst, return False
            # if there is even one False, the whole tree is not a bst
            left_check = self._inorder_recursive(current_node.left_child)
            # traverse right subtree
            right_check = self._inorder_recursive(current_node.right_child)
            #returning true only if both left and right subtrees are bst
            return left_check and right_check

# returns array of elements in the tree in sorted order
def convertToSortedArray(self):
    sorted_array = []
    self._convert_recursive(self.root, sorted_array)
    return sorted_array

def _convert_recursive(self, current_node, sorted_array):
    if self.root is not None:
        _convert_recursive(current_node.left_child, sorted_array)
        sorted_array.append(current_node.value)
        _convert_recursive(current_node.right_child, sorted_array)

# deletes the tree
def deleteTree(self):
    # traverse the tree in post-order and delete every node
    self._delete_tree_recursive(self.root)

def _delete_tree_recursive(self, current_node):
    if current_node is not None:
        self._delete_tree_recursive(current_node.left_child)
        self._delete_tree_recursive(current_node.right_child)
        del current_node
        
def lowestCommonAncestor(self, root, p, q):
    # 1. check if both nodes in the tree    
    if not self.search(p) or not self.search(q):
        return None
    
    # 2. find depth of both nodes
    p_depth = self.depth_to_list(root, [], p)
    q_depth = self.depth_to_list(root, [], q)

    # 3. find the lowest shared value in the two lists
    for i in range(len(p_depth)):
        if p_depth[i] == q_depth[i]:
            return p_depth[i]
        
    # if no shared value is found, return None
    return None


    

# calculates the depth of a node in the tree and saves each node to a list
# returns list of nodes in the path to the node
def depth_to_list(self, current_node, the_list, depth):
    # if the current node is at the depth we are looking for, return the list
    if current_node.value is depth:
        return the_list
    else:
        # add the current node to the list
        the_list.append(current_node.value)
        # det which tree to traverse
        if current_node.left_child.value < depth:
            depth_to_list(current_node.left_child, the_list, depth)
        if current_node.right_child > depth:
            depth_to_list(current_node.right_child, the_list, depth)



# Example usage:
if __name__ == "__main__":
    binary_tree = BinaryTree()
    elements = [44, 17, 88, 8, 32, 65, 97,54,82,93,78,80]

    for element in elements:
        binary_tree.insert(element)

    print(binary_tree.search(65))  # Output: True
    print(binary_tree.search(9))  # Output: False
    print("Original Binary Search Tree:")
    print(binary_tree.search(65))  # Output: True

    # Deleting a node with one child
    binary_tree.delete(65)
    print("Binary Search Tree after deleting 65:")
    print(binary_tree.search(65))  # Output: False

    # Deleting a node with no children
    binary_tree.delete(8)
    print("Binary Search Tree after deleting 8:")
    print(binary_tree.search(8))   # Output: False

    # Deleting a node with two children
    binary_tree.delete(88)
    print("Binary Search Tree after deleting 88:")
    print(binary_tree.search(88))  # Output: False