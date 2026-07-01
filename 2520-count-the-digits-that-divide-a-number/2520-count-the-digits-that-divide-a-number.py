class Solution:
    def countDigits(self, num: int) -> int:
        sum=0
        num=str(num)
        for i in range(len(num)):
            if int(num)%int(num[i])==0:
                sum=sum+1
            else:
                sum=sum+0
        return sum
        