from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        R = deque()
        D = deque()
        n = len(senate)
        for i in range(0,n):
            if senate[i] == 'D':
                D.append(i)
            else:
                R.append(i)
        while(R and D):
            d = D.popleft()
            r = R.popleft()
            if r<d:
                R.append(r+n)
            else:
                D.append(d+n)
        if R:
            return "Radiant"
        else:
            return "Dire"
