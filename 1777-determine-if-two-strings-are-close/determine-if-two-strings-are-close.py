class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if set(word1)!=set(word2):
            return False
        if len(word1)!=len(word2):
            return False
        h1 = {}
        for i in word1:
            if i in h1:
                h1[i]+=1
            else:
                h1[i]=1
        h2 = {}
        for i in word2:
            if i in h2:
                h2[i]+=1
            else:
                h2[i]=1
        if sorted(h1.values())!=sorted(h2.values()):
            return False
        return True