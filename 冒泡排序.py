list=[9,76,55,98,76,1,78,94,-8,23]

def bubblesort(list):
    len1=len(list)
    count=1
    for j in range(len1-1):
        i=0
        for i in range(len1-count):
            if list[i]>list[i+1] :
                c=list[i]
                list[i]=list[i+1]
                list[i+1]=c
            else:
                pass
        count=count+1
    return(list)
y=bubblesort(list)
print(y)