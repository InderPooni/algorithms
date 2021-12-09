from collections import deque

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None


def inOrderTraversal(root):
    stack = deque()

    curr = root

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        
        else:
            curr = stack.pop()
            print(curr.val)
            curr = curr.right



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    inOrderTraversal(root)

