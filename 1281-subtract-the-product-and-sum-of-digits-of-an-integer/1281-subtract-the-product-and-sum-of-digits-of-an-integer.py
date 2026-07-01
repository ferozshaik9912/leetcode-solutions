class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        mul=1
        n=str(n)
        for i in range(len(n)):
            sum=sum+(int(n[i]))
            mul=mul*int(n[i])
        return mul-sum    


