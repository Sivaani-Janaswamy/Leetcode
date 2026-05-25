class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1])
        answer = 0
        last_interval = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]<last_interval[1]:
                answer+=1
            else:
                last_interval = intervals[i]
        return answer

        