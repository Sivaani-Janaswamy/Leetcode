class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = []
        for i in range(0,rowIndex+1):
            row = []
            for j in range(0,i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j]+triangle[i-1][j-1])
            triangle.append(row)
        return triangle[rowIndex]