class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(0,n):
            k = abs(nums[i])-1
            nums[k] = -1*abs(nums[k])
        result = []
        for i in range(0,n):
            if nums[i]>0:
                result.append(i+1)
        return result
        