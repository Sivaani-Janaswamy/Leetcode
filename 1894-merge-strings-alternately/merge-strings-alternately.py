class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i,j = 0,0
        l1,l2=len(word1),len(word2)
        strs = []
        while(i<l1 and j<l2):
            strs.append(word1[i])
            i+=1
            strs.append(word2[j])
            j+=1
        while(i<l1):
            strs.append(word1[i])
            i+=1
        while(j<l2):
            strs.append(word2[j])
            j+=1
        return "".join(strs)

        