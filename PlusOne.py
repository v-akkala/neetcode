class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        cursum = digits[-1] + 1 % 10
        if digits[-1] + 1 >= 10:
            ans.append(0)
            carry = 1
        else:
            ans.append(cursum)
            carry = 0
        for i in range(len(digits) - 2, -2, -1):
            if i == -1:
                ans.append(carry)
                break
            cursum = digits[i] + carry
            if cursum >= 10:
                carry = 1
                ans.append(0)
            else:
                carry = 0
                ans.append(cursum)
        if ans[-1] == 0:
            ans.pop()
        return ans[::-1]
