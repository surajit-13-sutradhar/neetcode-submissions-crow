# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, low=None, high=None):
#         self.val = val
#         self.low = low
#         self.high = high

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)
        
        return valid(root, float("-inf"), float("inf"))