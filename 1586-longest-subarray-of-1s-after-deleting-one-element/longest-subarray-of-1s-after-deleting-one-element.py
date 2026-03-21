class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        zeros = 0
        maxcount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros+=1
            if zeros>1:
                if nums[start]==0:
                    zeros-=1
                start+=1
            maxcount = max(maxcount,i-start)
        return maxcount

            
        