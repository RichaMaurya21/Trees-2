# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        # The root is the last element in the postorder traversal
        rootVal = postorder.pop()
        root = TreeNode(rootVal)
        
        # Find the root in inorder list to split into left and right subtrees
        mid = inorder.index(rootVal)

        # Recursively build the right subtree first because we are using the last element of postorder
        root.right = self.buildTree(inorder[mid+1:], postorder)
        root.left = self.buildTree(inorder[:mid], postorder)

        return root
        