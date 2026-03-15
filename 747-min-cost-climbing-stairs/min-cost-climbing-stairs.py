class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        cost.append(0)
        for i in range(n-2,-1,-1):
            cost[i] = min(cost[i]+cost[i+1],cost[i]+cost[i+2])
        return min(cost[0],cost[1])

        