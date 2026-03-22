class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hashmap = {}
        n = len(grid)
        for rows in grid:
            row = tuple(rows)
            if row in hashmap:
                hashmap[row]+=1
            else:
                hashmap[row]=1
        pair=0
        for col in range(0,n):
            cols = []
            for row in range(0,n):
                cols.append(grid[row][col],)
            cols = tuple(cols)
            if cols in hashmap:
                pair+=hashmap[cols]
        return pair
      



        