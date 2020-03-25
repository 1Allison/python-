year = int(input("请输入一个年份"))
num=2
if (year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("{0}是闰年".format(year))
        else:
            print("{0}不是闰年".format(year))

    else:
        print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))


#还可以调用python自带的库
import calendar

year= int( input("请输入年份："))
check_year= calendar.isleap(year)
if check_year == True:
    print("%d是闰年"%year)
else:
    print("%d是平年"%year)
