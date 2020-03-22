list=[9,76,55,98,76,1,78,94,-8,23]

def bubblesort(list):
    len1=len(list)
    for j in range(len1-1):
        i=0
        for i in range(len1-j-1):
            if list[i]>list[i+1] :
                list[i],list[i+1]=list[i+1],list[i]
            else:
                pass
    return list
y=bubblesort(list)
print(y)