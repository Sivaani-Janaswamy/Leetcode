class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c_end = 0
        far_end = 0
        jumps = 0
        n = len(nums)
        for i in range(0,n-1):
            far_end = max(far_end,nums[i]+i)
            if i==c_end:
                jumps+=1
                c_end = far_end
        return jumps

        