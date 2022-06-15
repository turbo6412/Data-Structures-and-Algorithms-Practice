# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: 
            return root
        
        queue = deque()
        results = []
        queue.append(root)
        
        #queue = []
        #current_level = [15, 7 ]
        #results = [[3], [9, 20], [15, 7]]
        
        while queue: 
            # code to traverse by level and make a level array to add to results
            level_size = len(queue)
            current_level = []
            
            for i in range(level_size): 
                current_node = queue.popleft()
                current_level.append(current_node.val)
                
                if current_node.left: 
                    queue.append(current_node.left)

                if current_node.right: 
                    queue.append(current_node.right)
            
            results.append(current_level)
        
        return results
                
                
