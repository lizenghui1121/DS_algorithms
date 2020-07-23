"""
牛牛截获了一段由凯撒密码加密过的密文，凯撒密码指的是将字符偏移一定的单位，
例如若偏移量为2，则a替换为c，b替换为d，c替换为e，...，z替换为b。若加密nowcoder，则密文为pqyeqfgt。
现在牛牛发现对方加密包括数字、大写字母、小写字母，即0-9、A-Z、a-z的排列顺序进行偏移，
现在牛牛截获了对方的一段密文以及偏移量，你能帮助牛牛破解密文吗。即给定一段密文str和偏移量d，求对应的明文。
@Author: Li Zenghui
@Date: 2020-07-23 21:04
"""


class Solution:
    def decode(self, s, d):
        if not s:
            return ""
        raw_list = [str(i) for i in range(10)] + [chr(j) for j in range(65, 65 + 26)] + [chr(k) for k in
                                                                                         range(97, 97 + 26)]
        l = [i for i in range(len(raw_list))]
        dic = dict(zip(raw_list, l))

        s_list = list(s)
        for i in range(len(s_list)):
            s_list[i] = raw_list[dic[s_list[i]] - d]
        return "".join(s_list)


if __name__ == '__main__':
    s = Solution()
    print(s.decode("pqyeqfgt", 27))
