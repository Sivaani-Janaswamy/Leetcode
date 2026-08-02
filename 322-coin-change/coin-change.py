class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')]*(amount+1)
        dp[0]=0
        for amt in range(amount+1):
            for c in coins:
                if c<=amt:
                    dp[amt] = min(dp[amt],dp[amt-c]+1)
        if dp[amt]!=float('inf'):
            return dp[amt]
        return -1