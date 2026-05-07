class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        res = []
        def dfs(node,path):
            if node == n-1:
                res.append(path[:])
                return res
            for nei in graph[node]:
                path.append(nei)
                dfs(nei,path)
                path.pop()
        dfs(0,[0])
        return res

       