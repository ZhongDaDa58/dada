import sys
import json

with open(sys.argv[1],"r+",encoding="utf-8") as file:
    data=json.load(file)
highest_num=[data[0]]
highest_count=data.count(data[0])
for n in data:
    if highest_count<data.count(n):
        highest_count=data.count(n)
        highest_num.clear()
        highest_num.append(n)
    elif highest_count==data.count(n) and n not in highest_num:
        highest_num.append(n)
with open("output.txt","w") as file:
    file.write(",".join([str(n) for n in highest_num]))

