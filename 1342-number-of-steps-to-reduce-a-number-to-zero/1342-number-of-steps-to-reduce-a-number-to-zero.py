class Solution:
    def numberOfSteps(self, num: int) -> int:
        sum=0
        while num:
            if num&1:
                num-=1
            else:
                num>>=1
            sum+=1
        return sum
        