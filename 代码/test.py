# num=["harden","lampard",3,34,45,56,76,87,78,45,3,3,3,3,87687,98,76]
# len1=len(num)

# for i in range(len1):
#     if num[i]==3:
#         num[i]='3a'
#     else:
#         pass

# print(num)
# num=["harden","lampard",3,34,45,56,76,87,78,45,3,3,3,3,87687,98,76]
# for i in range(num.count(3)):
#     ele_index = num.index(3)
#     num[ele_index]="3a"
# print(num)

# list1 =[2,3,8,4,9,5,6]
# list2 =[5,6,10,17,11,2]
# list3 =list1+list2
# print(list3)
# print(set(list3))
# print (list(set(list3)))
#计算平方根
# num=int(input('请输入一个值'))
# num_sqrt = num ** 0.5
# print('%0.2f 的平方根为 %0.2f' %(num,num_sqrt))
#判断奇偶数
# num = int(input('请输入一个数字：'))
# if (num%2) == 0:
#     print("{0}是偶数".format(num))
#     # print( "%d是奇数" %num)  
# else:
#     print( "%d是奇数" %num)

# #生成日历
# import calendar
# #输入指定年月
# yy= int(input("输入年份："))
# mm= int(input("输入月份："))
# #显示日历
# print(calendar.month(yy,mm))

# #写文件
# with open ("test.txt","wt") as out_file:
#     out_file.write("该文本会写入到文件中\n看到我了吧！")
# #读文件
# with open("test.txt","rt") as in_file:
#     text = in_file.read()

# # print(text)

# #字符串判断
# print("测试实例一")
# str = "runoob.com"
# print(str.isalnum())
# print(str.isalpha())
# print(str.isdigit())
# print(str.islower())
# print(str.isupper())
# print(str.istitle())
# print(str.isspace())

# import calendar
# monthRange = calendar.monthrange(2016,2)
# print(monthRange)
# #获取昨天的日期 今天-1
# import datetime
# def getYesterday():
#     today=datetime.date.today()
#     oneday=datetime.timedelta(days=1)
#     yesterday=today-oneday
#     return yesterday

# print(getYesterday())

# import datetime
# def gettomorrow():
#     today=datetime.date.today()
#     oneday=datetime.timedelta(days=1)
#     tomorrow=today+oneday
#     return tomorrow

# print(gettomorrow())
# sum=0
# for i in range(1,100):
#     sum+=i
#     i=i+1

# print(sum)
# a= True
# b=not a
# print(b)
# print(not b)
# print(a!=b)
# print(a and b)
# print(a or b)
# print(1<2 and b==True)

# print('this is the \n same line')

# for i in range (0,5):
#     for j in range(0,i+1):
#         print('*',end=' ')
#     print()  

# # print(bool(' '))

# for i in range(1,10):
#     print(i,end=' ')
# print(list(range(1,10)))
# from random import choice
# score_you = 0
# score_com = 0
# dir_you = input("请输入一个方向射门")
# dir_com = choice(list['左'，'中','右'])
# for i in range(0,5):
#     if(dir_you!=dir_com):
#         print("Goal!")
#             score=score+1
#     else:
#        print("Oops...")(
#     print('score:%(you)-%d(com)\n' %(score_you,score_com)))
#     if (score>=3):
#         break

# sum=0
# for i in range(1,101):
#     sum=sum+i

# print(sum)
# i = 0
# while i < 5:
#    i += 1
#    for j in range(3):
#        print (j)
#        if j == 2:
#            break
#    for k in range(3):
#        if k == 2:
#            continue
#        print (k)
#    if i > 3:
#        break
#    print (i)
# q = int(input())
# n = 1
# an = 1
# while n <= 10:
#     print(an)
#     an *= q
#     n += 1
# from math import pi
# print (pi)

# def feibo(n):
#         print(1)
#     if n==0:
#         pass
#     elif n==1:  
#         print(1)
#     else:
#         for i in range(n):
#             return feibo(i)+feibo(i+1)
            

# feibo(3)

n = int(input())
x = 3
a1 = 1
a2 = 1
print(a1)
print(a2)

while x <= n:
   a3 = a1 + a2
   print(a3)
   a1 = a2
   a2 = a3
   x += 1