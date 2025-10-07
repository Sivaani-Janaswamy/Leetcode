class Solution:
    def climbStairs(self, n: int,memo = None) -> int:
      def stairs(n,memo = None):
        if memo == None:
            memo = {}
        if n in memo:
            return memo[n]
        if n<=2:
            return n
        memo[n] = stairs(n-1,memo)+ stairs(n-2,memo)
        return memo[n]
      return stairs(n)