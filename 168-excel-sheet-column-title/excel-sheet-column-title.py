class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        strs = ""
        while(columnNumber>0):
            columnNumber = columnNumber-1
            remainder = columnNumber%26
            strs+=alphabet[remainder]
            columnNumber //= 26
        return strs[::-1]




        