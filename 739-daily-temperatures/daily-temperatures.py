class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [] 
        answer = [0] * len(temperatures)
        for i in range(0,len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx = stack.pop() 
                answer[idx] = i-idx
            stack.append(i)
        return answer
            
