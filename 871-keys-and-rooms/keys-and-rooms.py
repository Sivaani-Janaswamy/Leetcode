class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        def dfs(node):
            visited.add(node)
            for key in rooms[node]:
                if key not in visited:
                    dfs(key)
        dfs(0)
        return len(visited)==len(rooms)
        