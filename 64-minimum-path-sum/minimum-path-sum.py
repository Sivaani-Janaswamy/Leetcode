class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(0,m):
            for j in range(0,n):
                if i>0 and j>0:
                   dp[i][j] = grid[i][j] + min(dp[i][j-1],dp[i-1][j])
                elif i==0 and j>0:
                   dp[i][j] = grid[i][j] + dp[i][j-1] 
                elif j==0 and i>0:
                   dp[i][j] = grid[i][j] + dp[i-1][j] 
                else:
                    continue
        return dp[m-1][n-1]
                
