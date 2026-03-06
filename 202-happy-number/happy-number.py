class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getNext(n1):
            r,n2=0,0
            while(n1>0):
              r=n1%10
              n1=n1//10
              n2+=pow(r,2)
            return n2
        slow,fast = n,getNext(n)
        if fast==1:
            return True
        while(slow!=fast):
          slow = getNext(slow)
          fast = getNext(getNext(fast))
          if fast==1:
            return True
        return False

          
          
          

        