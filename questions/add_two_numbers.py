from typing import List


class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

"""
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
"""   
def addTwoNumbers(l1,l2):
    res = ListNode(-1)
    dummy = res

    carry = 0

    while l1 or l2 or carry != 0:
        nodeSum = 0
        
        if l1:
            nodeSum += l1.val
            l1 = l1.next
        
        if l2:
            nodeSum += l2.val
            l2 = l2.next
        
        nodeSum += carry

        #node Sum = 10 carry - 1 nodeSum - 0

        carry = nodeSum / 10

        nodeSum = nodeSum % 10
        newNode = ListNode(nodeSum)
        dummy.next = newNode
        dummy = dummy.next
    

    return res.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)


    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = addTwoNumbers(l1,l2)

    while result:
        print(result.val)

