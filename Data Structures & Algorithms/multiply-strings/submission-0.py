class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        num1 = num1[::-1]
        num2 = num2[::-1]        

        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += int(num1[i]) * int(num2[j])
                carry = res[i + j] // 10
                res[i + j + 1] += carry
                res[i + j] %= 10
        # print(res)
        i = len(res) - 1
        while res[i] == 0:
            i -= 1
        res = res[:i + 1]
        # print(res)
        res = map(str, res[::-1])
        
        return "".join(res)