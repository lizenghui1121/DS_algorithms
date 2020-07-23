"""
买最少的东西
5件商品，价格分别是1, 3, 7, 11, 13，给定钱和各商品数量，务必将钱花完，求购买最少商品的数量。
示例：
输入：
1 2 3 4 5
30
输出：
4
2 * 13 + 1 * 3 + 1 * 1 = 30
2 + 1 + 1 = 4
@Author: Li Zenghui
@Date: 2020-07-23 10:23
"""


def minimal_goods(count, money):
    price = [1, 3, 7, 11, 13]
    ans = 0
    total = 0
    j = 0
    temp_money = money
    while temp_money:
        temp_money = money
        ans = 0
        for i in range(4 - j, -1, -1):
            temp = min(count[i], temp_money // price[i])
            ans += temp
            temp_money -= temp * price[i]
            if temp_money <= 0:
                break
        if temp_money != 0:
            j += 1
    return ans


if __name__ == '__main__':
    coins_count = [1, 2, 3, 4, 5]
    print(minimal_goods(coins_count, 18))  # 4





