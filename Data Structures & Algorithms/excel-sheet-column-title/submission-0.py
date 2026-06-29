class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        def numToChar(columnNumber):
            columnNumber -= 1
            if columnNumber > 26:
                res.append(chr(ord('A') + columnNumber % 26))
                numToChar(columnNumber // 26)
                return 

            res.append(chr(ord('A') + columnNumber))
            return

        numToChar(columnNumber)
        return "".join(reversed(res))