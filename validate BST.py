#Time Complexity: O(n)
#Space Complexity: Recursive call stack size O(height of the tree)
#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.flag=True;
        self.previous=float(-inf);
        self.InOrder(root);
        
        return self.flag;
    def InOrder(self,root):
        if root==None:
            return;
        self.InOrder(root.left);
        if root.val<=self.previous:
            self.flag=False;
        self.previous=root.val;
      
        self.InOrder(root.right);