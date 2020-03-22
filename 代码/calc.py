def calc (numbers) :
    sum=0
    for i in range(numbers):
        sum=sum+i*i
    return(sum)

y=calc(5)
print(y)