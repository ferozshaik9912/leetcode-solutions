class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        result = x[-1::-1]
        result = int(result.replace("-", "")) * (-1 if x.startswith("-") else 1)

        if result > 2**31 - 1 or result < -(2**31):
            return 0

        return result
