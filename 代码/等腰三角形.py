num = int(input())
n = 1
while n <= num:
    num_space = num - n
    num_star = 2*n - 1
    print(' ' * num_space,end="")
    print('*'*num_star)# 不加end会换行
    n += 1
    print()

