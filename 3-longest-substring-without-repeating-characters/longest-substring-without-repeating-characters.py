class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left,right = 0,0
        hashset = set()
        max_len = 0
        while(right<n):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            right += 1
            max_len = max(max_len,len(hashset))
        return max_len

            
            
        