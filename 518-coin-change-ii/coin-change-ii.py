class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0]*(amount+1)
        dp[0]=1 
        for c in coins:
            for amt in range(amount+1):
                if c<=amt:
                    dp[amt]+=dp[amt-c]
        return dp[amount]