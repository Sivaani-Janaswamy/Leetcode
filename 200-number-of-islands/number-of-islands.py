class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m,n = len(grid),len(grid[0])
        def dfs(i,j):
             if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                 grid[i][j]='0'
                 dfs(i+1, j)
                 dfs(i-1, j)
                 dfs(i, j+1)
                 dfs(i, j-1)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': 
                    dfs(i, j)
                    cnt += 1
        return cnt
        