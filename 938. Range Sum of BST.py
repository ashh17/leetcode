from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rangeSumBST(root, L, R):
    ans = 0
    stack = [root]  # since dfs
    while stack:
        node = stack.pop()
        if node:
            if L <= node.val <= R:
                ans += node.val
            if L < node.val:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
    return ans


def rangeSumBSTRecursive(self, root: TreeNode, L: int, R: int) -> int:
    self.sum = 0

    def recursiveDFS(root):
        if root:
            recursiveDFS(root.left)
            recursiveDFS(root.right)
            if L <= root.val <= R:
                self.sum += root.val

    recursiveDFS(root)
    return self.sum
