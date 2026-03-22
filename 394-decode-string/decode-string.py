class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        n = 0
        strs = ""
        for i in s:
            if i.isdigit():
                n = n*10 + int(i)
            elif i=='[':
                stack.append(n)
                stack.append(strs)
                strs,n = "",0
            elif i==']':
                strs = stack.pop() + strs*stack.pop()
            else:
                strs += i
        return strs
               
