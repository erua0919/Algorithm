# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            # 루트가 None 이면 None 을 반환
            return None

        root.left = self.pruneTree(root.left)
        # 왼쪽으로 들어가면서 탐색
        root.right = self.pruneTree(root.right)
        # 오른쪽으로 들어가면서 탐색
        if root.val == 0 and root.left is None and root.right is None:
            # 값이 0이고 왼쪽과 오른쪽 모두 None 이면 None 을 반환
            return None
        return root  
        