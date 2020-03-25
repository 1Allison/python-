#判断输入的值是否合法
nterms= int(input("请输入n维斐波那契数列的值:\n"))
n1=0
n2=1
count=2
if nterms <= 0:
    print("请输入一个正整数。")
elif nterms==1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列")
    print(n1,",",n2,end=",")
    while count < nterms:
        nth =n1+n2
        print(n1+n2, end=",")
        #更新值
        n1=n2
        n2=nth
        count+=1