class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = []
        word = ""
        for i in s.strip():
            if i.isalnum():
                word+=str(i)
            else:
                if word!="":
                    lst.append(word) 
                word = ""
        lst.append(word)
        return " ".join(reversed(lst))

                
