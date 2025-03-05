import sys
import json
import csv

with open(sys.argv[1],"r",encoding="utf-8") as file:
    data=json.load(file)
n=int(sys.argv[2])
count=0
stu=[]
exist=0
ls_data=sorted(list(data.values()),reverse=True)
for i in ls_data:
    if(count>=n):
        break
    key=[k for k,v in data.items() if v==i]
    for ele in key:
        if ele in stu:
            exist=1
    if exist:
        exist=0
        continue
        
    
    stu.extend(key)
    count+=len(key)

with open("output.csv",'w',newline='',encoding='utf-8') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(set(stu))
