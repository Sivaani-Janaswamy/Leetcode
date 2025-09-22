class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        calc = ['+','D','C']
        for i in operations:
            if not stack:
                stack.append(i)
            elif i == '+':
                newScore = int(stack[-1]) + int(stack[-2])
                stack.append(newScore)
            elif i == 'C':
                stack.pop(-1)
            elif i == 'D':
                newScore = 2*int(stack[-1])
                stack.append(newScore)
            else:
                stack.append(i)
        sums = 0
        for i in stack:
            sums += int(i)
        return sums

            
        