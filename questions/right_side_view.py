from typing import Collection


def rightSideView(root):
    if not root:
        return []
    
    res = []

    q = Collection.deque()

    q.append(root)

    while q:
        rightSide = 0

        for _ in range(len(q)):

            node = q.popleft()
            rightSide = node.val

            if node:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        res.append(rightSide)

    
    return res





