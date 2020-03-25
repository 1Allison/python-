#定义加法运算
def add (x,y):
    return x+y
#定义减法运算
def subtract(x,y):
    return x-y
#定义乘法运算
def multiply(x,y):
    return x*y
def devide(x,y):
    return x/y

#用户输入
print("选择运算：")
print("1 相加")
print("2 相减")
print("3 相乘")
print("4 相除")

choice = int(input("请输入你的选择："))
num1 = int(input("输入第一个数字："))
num2 = int(input("输入第二个数字："))
result = 0
if choice==1:
    print(num1,"+",num2,"=",add(num1,num2))
elif choice==2:
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice==3:
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice==4:
    if num2!= 0:
        print(num1,"/",num2,"=",devide(num1,num2))
    else:
        print("分母不能为0")
else:
    print("请重新输入")