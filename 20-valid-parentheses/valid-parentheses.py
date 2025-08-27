class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {'(': ')', '{': '}', '[':']'}
        stack = []
        for i in s:
            if i in brackets:
               stack.append(i)
            else:
               if not stack or brackets[stack.pop()] != i:
                  return False 
        return not stack

            