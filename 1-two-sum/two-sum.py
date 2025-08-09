class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a in range(len(nums)-1):
          for b in range(a,len(nums)-1):
            if((nums[a] + nums[b+1]) == target):
             self = [a,b+1]
             return self
 

         