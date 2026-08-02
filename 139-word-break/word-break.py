class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        hashmap = {}
        for i in wordDict:
            hashmap[i] = len(i)
        n = len(s)
        dp = [False]*(n+1)
        dp[n]=True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                wlen = hashmap[w]
                if (i+wlen)<=n and s[i:i+wlen]==w:
                    dp[i]=dp[i+wlen]
                if dp[i]:
                    break
        return dp[0]
        