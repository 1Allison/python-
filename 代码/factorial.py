def fac(n):
    fac=1
    if n==0:
        fac=1
    else:
        for i in range(1,n+1):
            fac=fac*(i)
    return fac
    
n=int(input("请输入一个整数"))
if n<0:
    print('负数没有阶乘，请重新输入')
else:
    y=fac(n)
    print(y)