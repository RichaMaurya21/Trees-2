# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, currNum, res):
            if node is None:
                return
            
            currNum = currNum * 10 + node.val
            
            # If it's a leaf node, add the current number to the result
            if node.left is None and node.right is None:
                res[0] += currNum
                return

            helper(node.left, currNum, res)
            helper(node.right, currNum, res)
        
        res = [0]
        helper(root, 0, res)
        return res[0]