class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit=""
        for i in range(len(digits)):
            digit+=str(digits[i])
        plus=int(digit)+1
        plus=str(plus)
        list=[]
        for i in range(len(plus)):
            list.append(int(plus[i]))
        return list