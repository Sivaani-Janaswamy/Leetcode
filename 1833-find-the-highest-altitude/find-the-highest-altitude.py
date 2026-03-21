class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        n = len(gain)
        sums,maxi = 0,0
        for i in range(1,n+1):
            sums = sums + gain[i-1] 
            maxi = max(sums,maxi)
        return maxi       