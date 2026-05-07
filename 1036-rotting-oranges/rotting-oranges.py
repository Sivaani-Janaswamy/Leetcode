class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                if grid[i][j]==1:
                    fresh+=1
        res = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            i,j,t = queue.popleft()
            res = t
            for di,dj in directions:
                ni,nj = i+di,j+dj
                if 0<=ni<m and 0 <= nj < n and grid[ni][nj] == 1:
                     grid[ni][nj] = 2
                     fresh -= 1
                     queue.append((ni, nj, t+1))
        return res if fresh == 0 else -1
            