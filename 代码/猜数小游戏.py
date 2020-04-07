from random import randint
name = input("Please enter your name:")

f=open('game.txt',encoding='utf-8')
lines=f.readlines()
f.close()

scores={}
for line in lines:
    s=line.split()
    scores[s[0]]=s[1:] #文本中第一项name作为key，其他为value

score= scores.get(name)
if score is None:        #新用户
    score=[0,0,0]

game_times=int(score[0])
min_times=int(score[1])
total_times=int(score[2])

if game_times>0:
    avg_times=total_times/game_times
else:
    avg_times=0

print('%s, you have already played %d times, the min_times are %d, the avg_times are %.2f.' %(name,total_times,min_times,avg_times))
#游戏主体
num =randint(1,100)
time = 0
print('Guess what I am think')
bingo =False
while bingo== False:
    time+=1
    answer=int(input())
    if answer<num:
        print('too small')
    elif answer>num:
        print('too big')
    else:
        print('BINGO')
        bingo=True

#更新数据
if game_times==0 or time<min_times:
    min_times=time
total_times+=time
game_times+=1
scores[name]=[str(game_times),str(min_times),str(total_times)]
result = ''
for n in scores:
   line = n + ' ' + ' '.join(scores[n]) + '\n'
   result += line

f=open('game.txt','w',encoding='utf-8')
f.write(result)
f.close


