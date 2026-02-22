class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        count = [0]*(max(nums)+1)
        for i in range(0,n):
            count[nums[i]] += 1
        sums = 0
        for i in range(0,len(count)):
            sums += count[i]
            count[i] = sums 
        for i in range(0,n):
            if nums[i]==0:
                nums[i]=0
            else:
                nums[i] = count[nums[i]-1]
            
        return nums
            

        

        