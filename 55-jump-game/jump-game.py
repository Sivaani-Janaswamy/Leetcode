class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        maxreach = 0
        for i in range(0,n):
            if maxreach<i:
                return False
            maxreach = max(maxreach, nums[i]+i)
        return True
              
      