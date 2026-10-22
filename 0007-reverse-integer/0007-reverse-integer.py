class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x = str(x)
            res = x[-1::-1]
            res = int(res)

            if res > 2**31 - 1:
                return 0
            return res

        elif x < 0:
            x = str(x)
            a = x[1:]
            res = '-' + a[-1::-1]
            res = int(res)

            if res < -(2**31):
                return 0
            return res

        else:
            return 0