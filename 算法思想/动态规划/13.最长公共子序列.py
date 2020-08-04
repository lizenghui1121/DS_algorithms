"""
给定两个长度分别为N和M的字符串A和B，求既是A的子序列又是B的子序列的字符串长度最长是多少。

输入格式
第一行包含两个整数N和M。
第二行包含一个长度为N的字符串，表示字符串A。
第三行包含一个长度为M的字符串，表示字符串B。
字符串均由小写字母构成。
输出格式
输出一个整数，表示最大长度。
数据范围
1≤N,M≤1000
输入样例：
4 5
acbd
abedc
输出样例：
3
@Author: Li Zenghui
@Date: 2020-08-04 15:27
"""

def max_length(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if s1[i-1] == s2[j-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
    print(dp)
    return dp[n][m]


if __name__ == '__main__':
    print(max_length("acbd", "abedc"))