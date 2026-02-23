class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        class Stack:
            def __init__(self):
                self.stack = []
                self.operations = []
            def push(self,x):
                self.stack.append(x)
                self.operations.append("Push")
            def pop(self):
                self.stack.pop()
                self.operations.append("Pop")
            def top(self):
                return self.stack[-1]
        s = Stack()
        for i in range(1,n+1):
            s.push(i)
            if s.top() not in target:
                s.pop()
            if s.stack == target:
                break
        return s.operations


        