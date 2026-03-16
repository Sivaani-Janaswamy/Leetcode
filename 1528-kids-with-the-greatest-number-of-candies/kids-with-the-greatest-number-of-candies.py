class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_n = max(candies)
        result = []
        for i in candies:
            curr_n = i+extraCandies
            if curr_n>=max_n:
                result.append(True)
            else:
                result.append(False)
        return result