class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,z=0,0
        while(i<len(nums)):
            if nums[i]!=0:
               temp = nums[i]
               nums[i] = nums[z]
               nums[z] = temp
               z+=1
            i+=1
        print(nums)
        
            
