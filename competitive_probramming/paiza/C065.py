# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

num_list = list(range(1,101))

def calc_division(num_list, num_div):
    result = []
    for i in num_list:
        if i % num_div == 0:
            result.append(i)
    return result

def calc_small(num_list, num):
    result =[]
    for i in num_list:
        if i < num:
            result.append(i)
    return result

def calc_large(num_list, num):
    result =[]
    for i in num_list:
        if i > num:
            result.append(i)
    return result

N = int(input())
for i in range(N):
    ox = input().split()
    o = ox[0]
    x = int(ox[1])
    if o == "/":
        num_list = calc_division(num_list, x)
    if o == "<":
        num_list = calc_small(num_list, x)
    if o == ">":
        num_list = calc_large(num_list, x)
print(num_list[0])