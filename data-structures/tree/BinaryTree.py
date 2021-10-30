from model import TreeNode

class BinaryTree:
    def __init__(self, root) -> None:
        self.root = root
    
    """
        The idea is to do iterative level order traversal of the given tree using queue.
        If we find a node whose left child is empty, we make new key as left child of the node. 
        Else if we find a node whose right child is empty, we make the new key as right child. 
        We keep traversing the tree until we find a node whose either left or right child is empty
    """
    def insert_level_order(self,data):
        if not self.root:
            self.root = TreeNode(data)
            return
        
        q = []
        q.append(self.root)

        # Do level order traversal until we find an empty stall 
        while len(q):
            tmp = q[0]
            q.pop(0)

            if not tmp.left:
                tmp.left = TreeNode(data)
                break
            else:
                q.append(tmp.left)
            
            if not tmp.right:
                tmp.right = TreeNode(data)
                break
            else:
                q.append(tmp.right)
    
    # left root right
    def in_order_traversal(self, root):
        if not root:
            return
        
        self.inorder_traversal(root.left)
        print(root.data, end = " ")
        self.inorder_traversal(root.right)
    
    # root left right
    def pre_order_traversal(self,root):
        if not root:
            return
        print(root.data, end=" ")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)
    
    # left right root
    def post_order_traversal(self,root):
        if not root:
            return
        self.post_order_traversal(root.left)
        self.post_order_traversal(root.right)
        print(root.data, end=" ")
    
    # Replace by bottom most right most element
    """
        Algorithm:
        - Find bottom most, right most node to delete
        - Replace the deepest rightmost node’s data with the node to be deleted. 
        - Delete deepest rightmost node
    """
    def deletion(self,root,data):
        q = []
        q.append(root)

        while len(q):
            
        
        


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(11)
    root.left.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(8)

    bt = BinaryTree(root)

    bt.inorder_traversal(root)

    print("\nInserting {}".format(12))

    bt.insert_level_order(12)

    bt.inorder_traversal(root)