class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        common = []
        for edge in edges:
            u,v = edge[0],edge[1]
            if u in common:
                return u
            if v in common:
                return v
            common.append(u)
            common.append(v)