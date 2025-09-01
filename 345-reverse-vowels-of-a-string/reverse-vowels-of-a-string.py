class Solution(object):
    def reverseVowels(self, s):
       vowels = ['a','e','i','o','u','A','E','I','O','U']
       low = 0
       high = len(s)-1
       strList = list(s)
       while(low<high):
         if(s[low] in vowels and s[high] in vowels):
            strList[low] = s[high]
            strList[high] = s[low]
            low+=1
            high-=1
         elif(s[low] in vowels):
            high-=1
         else:
            low+=1
       return "".join(strList)

        

 