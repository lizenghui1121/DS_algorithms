"""
小Q在周末的时候和他的小伙伴来到大城市逛街，一条步行街上有很多高楼，共有n座高楼排成一行。
小Q从第一栋一直走到了最后一栋，小Q从来都没有见到这么多的楼，所以他想知道他在每栋楼的位置处能看到多少栋楼呢？
（当前面的楼的高度大于等于后面的楼时，后面的楼将被挡住）

输入描述:
输入第一行将包含一个数字n，代表楼的栋数，接下来的一行将包含n个数字wi(1<=i<=n)，代表每一栋楼的高度。
1<=n<=100000;
1<=wi<=100000;

输出描述:
输出一行，包含空格分割的n个数字vi，分别代表小Q在第i栋楼时能看到的楼的数量。

示例1
输入
6
5 3 8 3 2 5
输出
3 3 5 4 4 4
@Author: Li Zenghui
@Date: 2020-03-21 19:25
"""

n = int(input())
w_arr = list(map(int, input().split(' ')))

a = []
b = []
s1 = []
s2 = []
left = 0
right = n-1
for i in range(n):
    s1 = []
    for j in range(i+1, n):
        if not s1:
            s1.append(w_arr[j])
        else:
            if s1[-1] < w_arr[j]:
                s1.append(w_arr[j])
    a.append(len(s1))

for i in range(n-1, -1, -1):
    s2 = []
    for j in range(i-1, -1, -1):
        if not s2:
            s2.append(w_arr[j])
        else:
            if s2[-1] < w_arr[j]:
                s2.append(w_arr[j])
    b.append(len(s2))
res = []
for i in range(n):
    temp = a[i] + b[n-1-i] + 1
    res.append(str(temp))
print(' '.join(res))
