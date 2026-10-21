class Solution:
    def finalValueAfterOperations(self, operation: List[str]) -> int:
        count1=0
        
        for i in range(len(operation)):
            if operation[i]=="++X" or operation[i]=="X++":
                count1+=1
            elif operation[i]=="--X"or operation[i]=="X--":
                count1-=1
        return count1 
       
      