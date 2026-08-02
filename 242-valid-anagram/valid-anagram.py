class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        hashmap = {}

        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1

        for c in t:
            if c not in hashmap:
                return False
            hashmap[c] -= 1
            if hashmap[c] < 0:
                return False

        return True