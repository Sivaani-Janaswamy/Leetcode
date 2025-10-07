class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ln = 0
        s=s.rstrip()
        n = len(s)-1
        while(n>=0):
          if(s[n]==" "):
            break
          else:
            ln+=1
            n-=1
        return ln