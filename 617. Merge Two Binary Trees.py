# Example 1:
#
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 is None:
        return t2
    stack = [[t1, t2]]
    while stack:
        node = stack.pop()
        if node[0] is None or node[1] is None:
            continue

        node[0].val += node[1].val
        if node[0].left is None:
            node[0].left = node[1].left
        else:
            stack.append([node[0].left, node[1].left])

        if node[0].right is None:
            node[0].right = node[1].right
        else:
            stack.append([node[0].right, node[1].right])
    return t1
