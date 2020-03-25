# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: ListNode) -> ListNode:
    reverse = None
    while head:
        next = head.next
        head.next = reverse
        reverse = head
        head = next

    return reverse


myList = ListNode(1)
myList.next = ListNode(2)
myList.next = ListNode(3)
myList.next = None

print(reverseList(myList.val))

# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
