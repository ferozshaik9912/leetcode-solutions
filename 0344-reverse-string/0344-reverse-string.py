class Solution:
    def reverseString(self, s: list[str]) -> None:
        l=[]
        for i in range(len(s)-1,-1,-1):
            l.append(s[i])
        
        s[:]= l
       
    
        