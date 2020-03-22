def fac(n):
    if n==1 or n==0:
        return 1
    return n*fac(n-1)
    
n=int(input("请输入一个整数"))
if n<0:
    print('负数没有阶乘，请重新输入')
else:
    y=fac(n)
    print(y)