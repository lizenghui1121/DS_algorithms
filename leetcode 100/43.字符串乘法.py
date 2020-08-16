"""

@Author: Li Zenghui
@Date: 2020-08-13 11:54
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)
        ans = "0"
        for i in range(n - 1, -1, -1):
            y = int(num2[i])
            curr = ["0"] * (n - i - 1)
            carry = 0
            for j in range(m - 1, -1, -1):
                cur = y * int(num1[j]) + carry
                curr.append(str(cur % 10))
                carry = cur // 10
            if carry > 0:
                curr.append(str(carry))
            curr = "".join(curr[::-1])
            ans = self.add_string(ans, curr)
        return ans

    def add_string(self, s1, s2):
        print(s1, s2)
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0
        ans = []
        while i >= 0 or j >= 0 or carry != 0:
            a = int(s1[i]) if i >= 0 else 0
            b = int(s2[j]) if j >= 0 else 0
            result = a + b + carry
            ans.append(str(result % 10))
            carry = result // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])


if __name__ == '__main__':
    s = Solution()
    print(s.multiply('12', '12'))