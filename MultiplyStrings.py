class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def strtoint(string) -> int:
            if string == "0":
                return 0
            elif string == "1":
                return 1
            elif string == "2":
                return 2
            elif string == "3":
                return 3
            elif string == "4":
                return 4
            elif string == "5":
                return 5
            elif string == "6":
                return 6
            elif string == "7":
                return 7
            elif string == "8":
                return 8
            elif string == "9":
                return 9

        num1list = []
        num2list = []
        ans = 0

        num1 = num1[::-1]
        num2 = num2[::-1]

        for idx, digit in enumerate(num1):
            if idx != 0:
                num1list.append(strtoint(digit) * (pow(10, idx)))
            else:
                num1list.append(strtoint(digit))
        for idx, digit in enumerate(num2):
            if idx != 0:
                num2list.append(strtoint(digit) * (pow(10, idx)))
            else:
                num2list.append(strtoint(digit))

        for i in num1list:
            for j in num2list:
                ans += i * j

        return str(ans)
