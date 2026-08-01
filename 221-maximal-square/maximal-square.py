class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for i in range(m)]
        max_size = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                  if i==0 and j==0:
                    dp[i][j] = 1
                  elif i==0 and j>0:
                    dp[i][j] = 1
                  elif j==0 and i>0:
                    dp[i][j] = 1
                  else:
                   dp[i][j] = 1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
                max_size = max(dp[i][j],max_size)
        return max_size*max_size