"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        length = len(grid)

        def dfs(row, col, n):
            all_same = True
            val = grid[row][col]

            if n == 1:
                return Node(val, True)
            
            for r in range(n):
                for c in range(n):
                    if val != grid[row + r][col + c]:
                        all_same = False
                        break
            
            if all_same:
                return Node(val, True)

            n //= 2
            topLeft = dfs(row, col, n)
            topRight = dfs(row, col + n, n)
            bottomLeft = dfs(row + n, col, n)
            bottomRight = dfs(row + n, col + n, n)

            return Node(val, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(0, 0, length)