f = open('testexcel.csv', encoding='utf-8')
lines = f.readlines()
print(lines)
f.close()

results = []
 
for line in lines:
   print (line)
   data = line.split(',')
   print (data)

   sum = 0
   score_list = data[1:]
   for score in score_list:
       point=int(score)
       if point < 60:
           break
       sum += point
   result = '%s \t: %d\n' % (data[0], sum)
   print (result)
   
   results.append(result)

print (results)
output = open('resultexcel1.csv', 'w', encoding='utf-8')
output.writelines(results)
output.close()