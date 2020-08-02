"""

@Author: Li Zenghui
@Date: 2020-08-01 21:01
"""


class Solution:
    def Encode(self, key, s):
        import collections
        arr = [[None] * 5 for _ in range(5)]
        index = 0
        key_set = set()
        dic = collections.defaultdict(list)
        for c in key:
            if c not in key_set:
                arr[index // 5][index % 5] = c if c != "j" else "i"
                dic[c].append(index // 5)
                dic[c].append(index % 5)
                index += 1
                key_set.add(c)
        for i in range(97, 123):
            if chr(i) not in key_set and chr(i) != "j":
                arr[index // 5][index % 5] = chr(i)
                dic[chr(i)].append(index // 5)
                dic[chr(i)].append(index % 5)
                index += 1
        # print(dic)
        s_pairs = []
        for i in range(0, len(s), 2):
            s_pairs.append(tuple(s[i:i+2]))
        res = ""
        for pair in s_pairs:
            if len(pair) == 2:
                c1, c2 = pair
                row1 = dic[c1][0]
                col1 = dic[c1][1]
                row2 = dic[c2][0]
                col2 = dic[c2][1]
                if c1 == c2:
                    res += c1
                    res += c2

                elif row1 == row2:
                    res += arr[row1][(col1 + 1) % 5]
                    res += arr[row1][(col2 + 1) % 5]

                elif col1 == col2:

                    res += arr[(row1 + 1) % 5][col1]
                    res += arr[(row2 + 1) % 5][col1]

                else:
                    res += arr[row1][col2]
                    res += arr[row2][col1]
            else:
                c3 = pair[0]
                res += c3
        return res
        # print(s_pairs)
        # print(arr)
        # print(res)


if __name__ == '__main__':
    s = Solution()
    s.Encode("nowcoder", "iloveyouk")
