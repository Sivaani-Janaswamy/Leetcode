class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ['a','e','i','o','u']
        start = 0
        maxcount,count = 0,0
        for i in range(len(s)):
            if s[i] in vowels:
                    count+=1
            if (i-start+1)>k:
                if s[start] in vowels:
                    count-=1
                start+=1
            if (i-start+1)==k:
                maxcount = max(maxcount, count)
        return maxcount
            
            
            

            