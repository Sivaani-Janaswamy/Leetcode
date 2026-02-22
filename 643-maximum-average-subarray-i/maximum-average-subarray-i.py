class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        sums = sum(nums[0:k]) #first k elements sum
        max_sum = sums
        for i in range(k,n):
            sums -= nums[i-k]
            sums += nums[i]
            max_sum = max(max_sum,sums)
        return max_sum/float(k)


        