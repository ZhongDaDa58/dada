import sys

def sort_line(line):
    ls=[str(s) for s in line if s.isdigit()]
    str_ls="".join(ls)
    if(len(str_ls)>=9):
        lin=str_ls[0:3]+"-"+str_ls[3:6]+"-"+str_ls[6:9]+"\n"
        return lin
    else:
        return line

result=""
with open(sys.argv[1],'r') as read:
    for line in read.readlines():
        newline=sort_line(line)
        result+=newline
result=result[:-1]
with open(sys.argv[2],'w') as write:
    write.write(result)
