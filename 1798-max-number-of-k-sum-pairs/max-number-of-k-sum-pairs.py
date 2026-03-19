class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i,j = 0,len(nums)-1
        pair = 0
        while(i<j):
            sums = nums[i]+nums[j]
            if sums<k:
                i+=1
            elif sums>k:
                j-=1
            else:
                pair+=1
                i+=1
                j-=1
        return pair
            