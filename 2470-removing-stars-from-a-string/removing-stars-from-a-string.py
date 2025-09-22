class Solution:
    def removeStars(self, s: str) -> str:
        a=[]
        for i in s:
            if i not in "*":
                a.append(i)
            elif i=="*":
                a.pop()
        return "".join(a)