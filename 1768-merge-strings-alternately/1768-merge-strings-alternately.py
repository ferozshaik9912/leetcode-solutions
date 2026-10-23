class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        if len(word1)==len(word2):
            for i in range(len(word1)):
                res=res+word1[i]  
                res=res+word2[i]
            return res  
        elif len(word1)>len(word2):
            s=""
            for i in range(len(word2)):
                s=s+word1[i]
            for i in range(len(word2)):
                res=res+s[i]
                res=res+word2[i]
            return res+word1[len(word2):]
        elif len(word2)>len(word1):
            s=""
            for i in range(len(word1)):
                s=s+word2[i]
            for i in range(len(word1)):
                res=res+word1[i]
                res=res+s[i]
            return res+word2[len(word1):]


        