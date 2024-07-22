# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursice DFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if(not root):
#             return 0
#         return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

# Iterative BFS (level order)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        q = deque([root]) 
        level = 0
        while(q):
            for i in range(len(q)):
                node = q.popleft()
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            level+=1
        return level