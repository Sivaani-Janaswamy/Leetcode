class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        n = len(heights)
        maxarea = 0
        for i in range(0,n):
            while stack and heights[i]<heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i-stack[-1]-1
                area = h*w
                maxarea = max(area,maxarea)
            stack.append(i)
        while stack:
                h = heights[stack.pop()]
                w = n if not stack else n-stack[-1]-1
                area = h*w
                maxarea = max(area,maxarea)
        return maxarea
        