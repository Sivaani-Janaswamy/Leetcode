class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        u = 0
        for i in range(0,len(nums)):
            if(nums[i]!=val):
                nums[u] = nums[i]
                u+=1
        return u
                
