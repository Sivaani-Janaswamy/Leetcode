from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """

        m, n = len(maze), len(maze[0])

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        queue = deque([entrance])
        visited = {tuple(entrance)}

        distance = 0

        while queue:

            for _ in range(len(queue)):

                r, c = queue.popleft()

                for dr, dc in directions:

                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and
                        0 <= nc < n and
                        maze[nr][nc] == '.' and
                        (nr, nc) not in visited):
                        if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                            return distance + 1

                        visited.add((nr, nc))
                        queue.append([nr, nc])

            distance += 1

        return -1