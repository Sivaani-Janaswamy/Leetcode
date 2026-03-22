class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for ast in asteroids:
            survive = True
            while(stack and stack[-1]>0 and ast<0 ):
                if abs(stack[-1])<abs(ast):
                    stack.pop()
                elif abs(stack[-1])==abs(ast):
                    stack.pop()
                    survive = False
                    break
                elif abs(stack[-1])>abs(ast):
                    survive = False
                    break
            if survive:
                stack.append(ast)
        return stack
                
            

                
            
                
                 