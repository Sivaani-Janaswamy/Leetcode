class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k = 0
        new = 0
        r = 0
        while(True):
          while(n>0):
            r = n%10
            n = n//10
            new += pow(r,2)
          if new == 1:
            return True
          n = new
          new = 0
          k+=1
          if k>1000:
            return False
          

        