class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        lsums,rsums = 0,0
        for i in range(0,n):
            rsums = total-lsums-nums[i]
            if lsums==rsums:
                return i
            lsums = lsums + nums[i]
        return -1