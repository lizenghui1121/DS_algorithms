"""

@Author: Li Zenghui
@Date: 2020-04-15 17:20
"""

keyword, raw_str = input().split()
str_list = raw_str.split("]")
res = []
for item in str_list:
    temp = item
    if len(item) > 0:
        if item[0] == ',':
            temp = item[1:]
        processed_list = temp.split("[")
        if processed_list[0] == keyword:
            temp_res = []
            target_str_list = processed_list[-1].split(",")
            addr = target_str_list[0][5:]
            mask = target_str_list[1][5:]
            val = target_str_list[2][4:]
            temp_res.append(addr)
            temp_res.append(mask)
            temp_res.append(val)
            res.append(temp_res)
if not res:
    print('FAIL')
else:
    for item in res:
        print(" ".join(item))
