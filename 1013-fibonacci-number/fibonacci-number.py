class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return n
        dp = [0]*(n+1)
        dp[1],dp[2]=1,1
        for i in range(3,n+1):
           dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
        