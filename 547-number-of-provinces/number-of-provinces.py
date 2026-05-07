class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = set()
        def dfs(node,visited):
            if node not in visited:
                visited.add(node)
                for i in range(0,n):
                    if i not in visited and isConnected[node][i]==1:
                       dfs(i,visited)
        provinces = 0
        for city in range(0,n):
            if city not in visited:
               dfs(city,visited)
               provinces+=1
        return provinces



