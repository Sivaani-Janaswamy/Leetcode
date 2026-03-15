class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1 = len(str1)
        l2 = len(str2)
        if str1+str2 != str2+str1:
            return ""
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        return str1[:gcd(l1,l2)]
        
            
        
        