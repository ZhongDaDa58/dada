import sys

def IsPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

args=sys.argv[1:]

ls=[str(n) for n in range(int(args[0]),int(args[1])+1) if IsPrime(n) and n>1]

with open("output.txt","w") as file:
    file.write(str(len(ls))+"\n")
    file.write(",".join(ls))
        

