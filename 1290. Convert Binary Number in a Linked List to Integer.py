# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getDecimalValue(head:ListNode) -> int:
    result = 0
    while head:
        result = result * 2 + head.val
        head = head.next
    return result


# Example 1:
#
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
#
# Example 2:
#
# Input: head = [0]
# Output: 0
#
# Example 3:
#
# Input: head = [1]
# Output: 1
#
# Example 4:
#
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880
#
# Example 5:
#
# Input: head = [0,0]
# Output: 0
