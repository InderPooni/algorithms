class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        pass

    def search(self, root, key):
        if not root:
            return None
        
        if root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        
        if value < root.val:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        
        return root
    
    # Case 1: Node to delete is a leaf node
    # Case 2: Node to delete has one child -> Copy child to Node and delete the child
    # Case 3: Node to delete has two children -> Find the inorder successor (left most child of right subtree), copy inorder successor to the node and delete successor
    def deletion(self,root, key):
        if not root:
            return root
        
        if root.val > key:
            root.left = self.deletion(root.left, key)
        elif root.val < key:
            root.right = self.deletion(root.right, key)

        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            if root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.minValue(root.right)

            root.val = temp.val

            root.right = self.deletion(root.right, temp.val)

        return root
        
        

    
    def minValue(self, root):
        curr = root

        while curr.left != None:
            curr = curr.left
        
        return curr

    def maxValue(self, root):
        curr = root

        while curr.right != None:
            curr = curr.right
        
        return curr

    def inorderTraversal(self,root):
        if not root:
            return None
        
        self.inorderTraversal(root.left)
        print(root.val, end=" ")
        self.inorderTraversal(root.right)


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)


    tree = BinarySearchTree()

    tree.insert(root, 8)
    
    tree.deletion(root, 1)

    tree.inorderTraversal(root)
