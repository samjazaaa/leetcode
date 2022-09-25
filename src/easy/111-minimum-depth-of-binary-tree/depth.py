# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if (root is None):
            return 0

        if (root.left is None and root.right is None):
            return 1

        if (root.left is None):
            return self.minDepth(root.right) + 1

        if (root.right is None):
            return self.minDepth(root.left) + 1

        depthLeft = self.minDepth(root.left) + 1
        depthRight = self.minDepth(root.right) + 1

        if (depthLeft <= depthRight):
            return depthLeft
        else:
            return depthRight
