class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = [[] for i in range(n)]
        for edge in edges:
            u,v = edge[0],edge[1]
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(node,visited,graph):
            if node==destination:
                return True
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour,visited,graph):
                        return True
            return False

        return dfs(source, visited, graph)


        