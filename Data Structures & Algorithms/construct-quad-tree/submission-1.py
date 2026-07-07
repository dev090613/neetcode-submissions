'''
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
'''
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        사분면을 정의 - (row, col), (row + n // 2, col)
        Base - 사분면의 값이 동일
        Recursive - 사분면에 대하여 다시 재귀
        """

        def dfs(n, row, col):
            all_same = True

            for i in range(n):
                for j in range(n):
                    if grid[row][col] != grid[row + i][col + j]:
                        all_same = False
                        break
            
            if all_same:
                return Node(val=grid[row][col], isLeaf=True)

            n //= 2
            top_left = dfs(n, row, col)
            top_right = dfs(n, row, col + n)
            bot_left = dfs(n, row + n, col)
            bot_right = dfs(n, row + n, col + n)

            return Node(
                val=grid[row][col],
                isLeaf=False,
                topLeft=top_left,
                topRight=top_right,
                bottomLeft=bot_left,
                bottomRight=bot_right
            )
        
        return dfs(len(grid), 0, 0)