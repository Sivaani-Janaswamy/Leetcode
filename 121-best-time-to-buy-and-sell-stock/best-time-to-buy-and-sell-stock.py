class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = 999999
        maxProfit = 0
        for price in prices:
            if price<minPrice:
                minPrice = price
            profit = price-minPrice
            if profit>maxProfit:
                maxProfit = profit
        return maxProfit

        